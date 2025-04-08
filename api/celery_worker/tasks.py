from celery import Celery
import asyncio


app = Celery("tasks", broker="redis://redis/0", backend="redis://redis/0")


@app.task()
def add(a, b):
    for i in range(a, b):
        print(i)
        asyncio.sleep(1)
    return {"number": a + b}
