from main import celery, run_job

type(run_job)

if __name__ == "__main__":
    celery.worker_main(argv=["worker", "-l", "info"])
