from sqlalchemy.orm import sessionmaker

from src.models.youtube import YouTube


def get_youtube(*, db: sessionmaker, url: str) -> YouTube:
    if not (youtube := db.query(YouTube).filter(YouTube.url == url).first()):
        return None
    return youtube


def create_youtube(*, db: sessionmaker, user_id: int, url: str) -> YouTube:
    youtube = YouTube(user_id=user_id, url=url)
    db.add(youtube)
    db.commit()
    return youtube


def get_or_create_youtube(*, db: sessionmaker, user_id: int, url: str) -> YouTube:
    if not (youtube := get_youtube(db=db, url=url)):
        youtube = create_youtube(db=db, user_id=user_id, url=url)

    return youtube
