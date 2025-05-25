from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from . import db


class User(db.Model): 
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String(16), unique = True)
    password: Mapped[str] = mapped_column(String(30), nullable=False)

    # Class Method: Find a user by name
    @classmethod
    def find_by_name(cls, username):
        return db.session.query(cls).filter_by(username=username).first()

    # Class Method: Get all users
    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()
    
    @classmethod
    def create_user(cls,username,password):
        return db.session.query(cls).add(username=username,password=password)

