# fastapi-celery-template

## prequisition
```
pip install poetry
```
prepare a .env file in the root directory( BROKER/BACKEND options: redis, amqp, rpc, etc.)

if you use rabbitmq as broker use CELERY_BROKER_TYPE=amqp

if you use rabbitmq as backend use CELERY_RESULT_BACKEND_TYPE=rpc , both port use 5672

```
# Celery configuration
# BROKER options: redis, amqp, rpc, etc.
CELERY_BROKER_TYPE=amqp
CELERY_BROKER_USERNAME=username
CELERY_BROKER_PASSWORD=mypassword
CELERY_BROKER_HOST=10.8.0.1
CELERY_BROKER_PORT=5672

CELERY_RESULT_BACKEND_TYPE=redis
CELERY_RESULT_BACKEND_USERNAME=username
CELERY_RESULT_BACKEND_PASSWORD=mypassword
CELERY_RESULT_BACKEND_HOST=10.8.0.1
CELERY_RESULT_BACKEND_PORT=6379
```

if you use redis as broker, you need to install redis 
```
pip install redis
```

## create virtual env

```
poetry config virtualenvs.in-project true;
poetry install;
```

## start fastapt
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

## start celery worker
```
celery -A worker worker --loglevel=info
```

## go to http://localhost:8000
