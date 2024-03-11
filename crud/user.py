from sqlalchemy.orm import sessionmaker

from models.user import User


def get_user(*, db: sessionmaker, telegram_id: int):
    if not (user := db.query(User).filter(User.id == telegram_id).first()):
        return None
    return user


def create_user(*, db: sessionmaker, telegram_id: int) -> User:
    user = User(id=telegram_id)
    db.add(user)
    db.commit()
    return user


def get_or_create_user(*, db: sessionmaker, telegram_id: int) -> User:
    if not (user := get_user(db=db, telegram_id=telegram_id)):
        user = create_user(db=db, telegram_id=telegram_id)
    return user
