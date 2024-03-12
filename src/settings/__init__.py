from src.utils.downloader import download
from .celery import celery_app

__all__ = ("celery_app",)


@celery_app.task
def push_download_into_queue(url: str) -> str:
    file_path = download(url)
    return file_path
