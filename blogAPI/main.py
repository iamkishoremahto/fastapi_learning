from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas
from . import models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(bind= engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.post("/blog", status_code = status.HTTP_201_CREATED)
def createBlog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog', status_code= status.HTTP_200_OK)
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}', status_code= status.HTTP_200_OK)
def show(id:int, response: Response,  db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with id {id} not found")
    return blog

@app.delete('/blog/{id}', status_code = status.HTTP_204_NO_CONTENT)
def destroy(id:int, response:Response, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session= False)
    
    db.commit()

@app.put('/blog/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, response:Response, db: Session = Depends(get_db)):

    blog = db.query(models.Blog).filter(models.Blog.id == id).update({"title":"updated title"}, synchronize_session= False)
    db.commit()
    db.refresh(blog)
    return blog

    