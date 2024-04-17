from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, index= True)
    name = Column(String)
    email = Column(String, unique= True)
    password = Column(String)
    created_at = Column(DateTime, default= datetime.utcnow )
    updated_at = Column(DateTime, default= datetime.utcnow, onupdate= datetime.utcnow)

class Notes(Base):

    __tablename__ = 'notes'

    id = Column(Integer, primary_key= True, index= True)
    note = Column(String, nullable= False)
    user_id = Column(Integer, ForeignKey("users.id"))
    author = relationship('Users')
    created_at = Column(DateTime, default= datetime.utcnow )
    updated_at = Column(DateTime, default= datetime.utcnow, onupdate= datetime.utcnow)





