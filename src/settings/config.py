import os

from dotenv import load_dotenv

load_dotenv()

settings = dict()
settings["TELEGRAM_TOKEN"] = os.getenv("TELEGRAM_TOKEN")
settings["DB_URI"] = "postgresql+psycopg2://{0}:{1}@{2}:{3}/{4}".format(
    os.getenv('DB_USER'),
    os.getenv('DB_PASS'),
    os.getenv('DB_HOST'),
    os.getenv('DB_PORT'),
    os.getenv('DB_DB')
)
settings["CELERY_BROKER_URI"] = os.getenv("CELERY_BROKER_URI")
settings["CELERY_BACKEND"] = os.getenv("CELERY_BACKEND")
