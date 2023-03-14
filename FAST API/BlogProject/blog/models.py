from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    body= Column(String)
    user_id=Column(Integer,ForeignKey('users.id'))
    #is_active = Column(Boolean, default=True)
    creator= relationship("User",back_populates='blogs')

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)
    mail= Column(String, unique=True)
    password= Column(String)

    blogs=relationship("blog",back_populates="creator")