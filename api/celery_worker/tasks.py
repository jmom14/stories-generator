from celery import Celery


app = Celery("tasks", broker="redis://redis/0", backend="redis://redis/0")


@app.task
def sum_async(a, b):
    for i in range(a, b):
        print(i)
    return {"number": a + b}
