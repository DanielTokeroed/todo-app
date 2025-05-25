from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from . import db


class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement=True)
    task: Mapped[str] = mapped_column(String(256),nullable=False)
    
    