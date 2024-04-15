from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


#get______

@app.get('/')
def index():
    return {"message":"Testing GET request"}

# get___ path params

@app.get('/path/{path}')
def pathParams(path):
    return {"message":f"Path Params : {path}"}

# params with type

@app.get('/type/{count}')
def getParamsWithType(count : int):
    return {"count": count}

#Query Params

@app.get('/fullname')
def queryParams(f_name,l_name):
    return {"fullname":f"{f_name} {l_name}"}

#Optinal Params

@app.get('/get-fullname')
def optionalQuery(f_name, l_name ,m_name : Optional[str] = ""):
    return {"fullname":f"{f_name} {m_name} {l_name}"}


#create model for blog

class Blog(BaseModel):
    title :str
    content : str
    isFree : Optional[bool] = False


#Post method
@app.post('/blog')
def createBlog(request: Blog):

    return {"message":f"Blog created successfully , Title: {request.title}"}

if __name__ == "__main__":
    uvicorn.run(app)





