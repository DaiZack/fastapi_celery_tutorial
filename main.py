import time

from celery import Celery
from celery.result import AsyncResult
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Initialize Celery
celery = Celery("tasks")
celery.config_from_object("celeryconfig")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/start_job")
async def start_job(request: Request, input_data: str = Form(...)):
    task = celery.send_task("main.run_job", args=[input_data])
    return templates.TemplateResponse(
        "job_started.html", {"request": request, "task_id": task.id}
    )


@app.get("/job_status/{task_id}")
async def job_status(request: Request, task_id: str):
    task_result = AsyncResult(task_id, app=celery)
    status = task_result.status
    if status == "SUCCESS":
        output = task_result.result
    else:
        output = None
    return templates.TemplateResponse(
        "job_status.html", {"request": request, "status": status, "output": output}
    )


@celery.task
def run_job(input_data):
    # Code to run the job with input_data
    # Return the output
    time.sleep(10)
    output = f"Output {input_data} processed"
    return output
