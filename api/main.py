from fastapi.responses import FileResponse, StreamingResponse
from fastapi import FastAPI, HTTPException, BackgroundTasks
from api.services import stories
import logging
from api.models import request
from fastapi.middleware.cors import CORSMiddleware
from api.writers.writerfactory import Format, get_media_type
from api.helper.async_tasks import remove_file_async
from api.celery_worker.tasks import sum_async, app as celery_app

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://epubs-simple-reader.netlify.app/",
]


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.get("/sum-async-process")
def get_sum_async():
    result = sum_async.delay(10, 20)
    return {"task_id": result.id}


@app.get("/sum-async-result/status/{task_id}")
def get_sum_async_result(task_id: str):
    result = celery_app.AsyncResult(task_id)
    if result.ready():
        return {"result": result.result}
    else:
        return {"status": result.state}


@app.post("/stories/")
async def create_story(story: request.StoryRequest, background_tasks: BackgroundTasks):
    format_file = story.format

    try:
        book_buffer, filename = stories.create_story(story)
        headers_response = {
            "Content-Disposition": f"attachment; filename={filename}",
            "X-File-Name": filename,
        }

        if not filename:
            error_message = "Failed to create the story"
            logging.error(error_message)
            raise HTTPException(status_code=500, detail=error_message)

        if format_file == Format.EPUB.value:
            background_tasks.add_task(remove_file_async, filename)

            return FileResponse(
                filename,
                status_code=200,
                media_type=get_media_type(format_file),
                headers=headers_response,
            )

        if format_file == Format.PDF.value:
            return StreamingResponse(
                content=book_buffer,
                status_code=200,
                media_type=get_media_type(format_file),
                headers=headers_response,
            )
    except Exception as e:
        logging.error(str(e))
        raise HTTPException(
            status_code=500, detail="Something went wrong. Try again later"
        ) from e
