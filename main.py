from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get('/')
async def root():
    return {"message":"Hello, world!"}

#path with parameters

@app.get('/items/{item_id}')
async def items(item_id):
    return {"item_id": item_id}

#path with typed parameters

@app.get('/books/{id:int}')
async def books(id):
    return {"id": id}




class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None





@app.post("/items/")
async def create_item(item: Item):
    return item