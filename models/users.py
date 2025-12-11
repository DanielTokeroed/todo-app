from sqlalchemy import Integer, String, Select, Insert 
from sqlalchemy.orm import Mapped, mapped_column
from models import db
import hashlib


class User(db.Model): 
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key = True)
    username: Mapped[str] = mapped_column(String(256), unique = True)
    password: Mapped[str] = mapped_column(String(256), nullable=False)

    # Class Method: Find a user by name
    @classmethod
    def find_by_name(cls, username):
        return Select.where(username=username)

    # Class Method: Get all users
    @classmethod
    def get_all(cls):
        stmt = Select(User)
        result = db.session.execute(stmt).scalars().all()
        return result
    
    @classmethod
    def create_user(cls,username,password):
    
        passw = password.encode('utf-8')
        password = hashlib.sha256(passw).hexdigest()

        user = User(username = username,password=password)
        db.session.add(user)
        db.session.commit()

