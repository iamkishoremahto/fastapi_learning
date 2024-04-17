from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas
from . import models,hashing
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List



app = FastAPI()

models.Base.metadata.create_all(bind= engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code = status.HTTP_201_CREATED,tags = ["Blog"])
def createBlog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog', status_code= status.HTTP_200_OK, response_model = List[schemas.showBlog],tags = ["Blog"])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code= status.HTTP_200_OK,response_model = schemas.showBlog,tags = ["Blog"])
def show(id:int, response: Response,  db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    return blog

@app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT,tags = ["Blog"])
def destroy(id:int, response:Response, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Blog is not found")
    
    blog.delete(synchronize_session= False)
    db.commit()
    return {"message": "Blog deleted successfully"}

@app.put('/blog/{id}', status_code = status.HTTP_202_ACCEPTED,tags = ["Blog"])
def update(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    update_data = request.dict(exclude_unset=True)

    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Blog is not found")
    blog.update(update_data)
    db.commit()
   
    return {"message": "updated"}




@app.post('/user', status_code= status.HTTP_201_CREATED, response_model = schemas.showUser, tags = ["User"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
  
    new_user = models.User(name = request.name, email = request.email, password = hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/user/{id}',response_model= schemas.showUser ,tags = ["User"])
def get_user(id:int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "User not found")
    
    return user
    