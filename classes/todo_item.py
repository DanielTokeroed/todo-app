import pyodbc
from models import db
from sqlalchemy import select, insert, delete, update, text
from models.tasks import Task


class todo_manager:

    @staticmethod
    def complete(id: int):
        db.session.execute(update(Task).where(Task.id == id).values(status = True)) # type: ignore
        db.session.commit() # type: ignore

    @staticmethod
    def create(task: str|None):
       db.session.execute(insert(Task).values(task = task))
       db.session.commit() # type: ignore
    
    @staticmethod
    def delete(id: int):
        db.session.execute(delete(Task).where(Task.id == id)) # type: ignore
        db.session.commit() # type: ignore

    @staticmethod
    def delete_all():
        db.session.execute(delete(Task))
        db.session.commit() # type: ignore
    
    @staticmethod
    def truncate():
        response = db.session.execute(text('truncate table pagination.tasks'))
        return response


    @staticmethod
    def get_all():
        response = db.session.execute(select(Task)).scalars().all()
        return response
    



