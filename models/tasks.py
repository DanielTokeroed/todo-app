from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from models import db


class Task(db.Model):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement=True)
    task: Mapped[str] = mapped_column(String(256),nullable=False)
    status: Mapped[bool] = mapped_column(Boolean, default=False) # type: ignore
    
    def __repr__(self): # type: ignore
        return f"{self.id} {self.task!r}"