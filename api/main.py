from fastapi.responses import FileResponse, StreamingResponse
from fastapi import FastAPI, HTTPException
from services import stories
import logging
from models import request
from fastapi.middleware.cors import CORSMiddleware
from writers.writerfactory import Format, get_media_type

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
)


@app.get("/")
async def root():
    return {"Hello": "World"}


@app.post("/stories/")
async def create_story(story: request.StoryRequest):
    format_file = story.format

    try:
        book_buffer, filename = stories.create_story(story)

        if not filename:
            error_message = "Failed to create the story"
            logging.error(error_message)
            raise HTTPException(status_code=500, detail=error_message)

        if format_file == Format.EPUB.value:
            print("epub -> ", book_buffer)
            print(f"filename -> {filename}")
            return FileResponse(
                filename,
                filename=filename,
                status_code=200,
                media_type=get_media_type(format_file),
            )

        elif format_file == Format.PDF.value:
            headers_response = {
                "Content-Disposition": f"attachment; filename={filename}"
            }
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
