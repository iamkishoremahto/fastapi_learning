from fastapi import APIRouter, HTTPException, status, Depends
from .. import schemas, database, models
from ..CONTROLLERS.USER import user
from ..CONTROLLERS.generics import methods
from typing import List
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["Users"],
    prefix="/user"
)

@router.post('/', status_code = status.HTTP_201_CREATED, response_model = schemas.showUser)
def create_user(request:schemas.User, db:Session = Depends(database.get_db)):
    return user.create_new_user(request= request, db = db)

@router.get('/',status_code = status.HTTP_200_OK, response_model= List[schemas.showUser])
def all(db: Session = Depends(database.get_db)):
    return methods.show_list(db= db, model= models.Users)

@router.get('/{id}',status_code = status.HTTP_200_OK, response_model = schemas.showUser)
def retrieve_user(id:int, db:Session = Depends(database.get_db)):
    return methods.retrieve(db= db,id = id, model = models.Users)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_user(request:schemas.showUser,id:int, db: Session = Depends(database.get_db)):
    return methods.update(db= db, id= id, request = request, model = models.Users)

@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_user(id:int,db: Session = Depends(database.get_db)):
    return methods.delete(db = db, id= id, model = models.Users)



