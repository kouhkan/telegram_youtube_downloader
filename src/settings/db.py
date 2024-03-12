from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.settings.config import settings

# Create the Database engine
engine = create_engine(settings["DB_URI"])

# Create session local factory (for thread-safe sessions)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    yield db
    db.close()


db_context = contextmanager(get_db)
