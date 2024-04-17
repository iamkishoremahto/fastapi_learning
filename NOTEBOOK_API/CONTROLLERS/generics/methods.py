from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


def create(request,db: Session,model):

    new_data = model(**request.dict())
    db.add(new_data)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already in use")
    db.refresh(new_data)
    return new_data

def show_list(db:Session,model):
    datas = db.query(model).all()
    if not datas:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "No notes are available")
    return datas



def retrieve(db: Session,id:int,model):
    data = db.query(model).filter(model.id == id).first()
    if not data:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = "No content")
    return data
    

def update(db: Session, id:int, request, model):
   
    data = db.query(model).filter(model.id == id)
    
    if not data.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = "No content")
    update_data = request.dict(exclude_unset=True)
    data.update(update_data)
   
    db.commit()
    # db.refresh(data)
    return {"message": "Updated content"}

def delete(db: Session, id:int,model):
    data = db.query(model).filter(model.id == id)
    
    if not data.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = "No content")
    data.delete()
    db.commit()
    return {"message": "Deleted content"}
