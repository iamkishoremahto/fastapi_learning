from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    name:str
    email: str
    password: str



class showUser(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None

    class Config:
        orm_mode = True

class Note(BaseModel):
    note:Optional[str] = None
    user_id: Optional[int] = None
   
 

class showNote(BaseModel):
    note: Optional[str] = None
    author: Optional[showUser] = None

    class Config:
        orm_mode = True
 

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
