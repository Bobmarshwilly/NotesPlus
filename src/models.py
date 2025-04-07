from sqlalchemy import Column, Integer, String, DateTime
from src.database import Base
from datetime import datetime


class Note(Base):
    """
    Класс таблицы заметок в базе данных.

    id - первичный ключ, идентификатор заметки.
    content - содержание заметки.
    created_at - время добавления заметки.
    """

    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.now())

    def __repr__(self):
        return f"<Note(id={self.id}, content={self.content})>"
