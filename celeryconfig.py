import os

from dotenv import load_dotenv

load_dotenv()

broker_type = os.getenv("CELERY_BROKER_TYPE", "amqp")
broker_username = os.getenv("CELERY_BROKER_USERNAME")
broker_password = os.getenv("CELERY_BROKER_PASSWORD")
broker_host = os.getenv("CELERY_BROKER_HOST")

result_backend_type = os.getenv("CELERY_RESULT_BACKEND_TYPE", "rpc")
result_backend_username = os.getenv("CELERY_RESULT_BACKEND_USERNAME")
result_backend_password = os.getenv("CELERY_RESULT_BACKEND_PASSWORD")
result_backend_host = os.getenv("CELERY_RESULT_BACKEND_HOST")

if broker_username and broker_password:
    broker_url = f"{broker_type}://{broker_username}:{broker_password}@{broker_host}"
else:
    broker_url = f"{broker_type}://{broker_host}"

if result_backend_username and result_backend_password:
    result_backend = f"{result_backend_type}://{result_backend_username}:{result_backend_password}@{result_backend_host}"
else:
    result_backend = f"{result_backend_type}://{result_backend_host}"

broker_transport_options = {
    "visibility_timeout": 3600,
    "fanout_prefix": True,
    "fanout_patterns": True,
}

result_backend_transport_options = {"visibility_timeout": 3600}
