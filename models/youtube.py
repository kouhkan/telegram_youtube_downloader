from datetime import datetime

from sqlalchemy import ForeignKey, String, DateTime, Column, Integer

from models.base import Base


class YouTube(Base):
    __tablename__ = "youtube_urls"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    user_id = Column(Integer(), ForeignKey("users.id"))
    url = Column(String(256), nullable=False, index=True)
    local_url = Column(String(256), nullable=True, index=True)
    created_at = Column(DateTime(), default=datetime.now)

    def __repr__(self):
        return f"{self.user_id} -> {self.url}"
