import os

from dotenv import load_dotenv

load_dotenv()

settings = dict()
settings["TELEGRAM_TOKEN"] = os.getenv("TELEGRAM_TOKEN")
settings["DB_URI"] = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
    os.getenv('POSTGRES_USER'),
    os.getenv('POSTGRES_PASSWORD'),
    os.getenv('POSTGRES_HOST'),
    os.getenv('POSTGRES_PORT'),
    os.getenv('POSTGRES_DB')
)
settings["CELERY_BROKER_URI"] = os.getenv("CELERY_BROKER_URI")
settings["CELERY_BACKEND"] = os.getenv("CELERY_BACKEND")
