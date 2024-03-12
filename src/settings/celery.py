from celery import Celery

from src.settings.config import settings

celery_app = Celery(
    "proj",
    broker=settings["CELERY_BROKER_URI"],
    backend=settings["CELERY_BACKEND"],
)

celery_app.conf.update(
    result_expires=3600,
)

celery_app.autodiscover_tasks()
celery_app.conf.result_backend = settings["CELERY_BACKEND"]
celery_app.conf.result_serializer = "json"
