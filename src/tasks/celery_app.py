from celery import Celery

from src.config import settings

# from src.tasks.config import CeleryConfig

# celery_instance = Celery()
# celery_instance.config_from_object(CeleryConfig)


celery_instance = Celery(
    broker=settings.REDIS_URL.unicode_string(),
    include="src.tasks.tasks",
)
