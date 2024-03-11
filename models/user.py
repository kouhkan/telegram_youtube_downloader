from datetime import datetime

from sqlalchemy import Column, Integer, DateTime

from models.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return f"{self.id}"
