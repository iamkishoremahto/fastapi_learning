from pydantic import BaseModel
from typing import List


class Blog(BaseModel):
    title: str
    body: str
    user_id:int
   

class User(BaseModel):
    name: str
    email: str
    password: str

class showUser(BaseModel):
    name:str
    email:str
    

    class Config():
        orm_mode = True

class showBlog(BaseModel):
    title: str
    body: str
    creator: showUser
    
    class Config():
        orm_mode = True