from fastapi import APIRouter, status, HTTPException,Depends
from .. import schemas,models, database
from sqlalchemy.orm import Session
from ..CONTROLLERS.generics import methods
from ..CONTROLLERS.NOTE import note
from typing import List

router = APIRouter(
    
    tags=["Note"],
    prefix = "/note"
)

@router.post('/',status_code = status.HTTP_200_OK,response_model = schemas.showNote)
def create_note(request:schemas.Note, db: Session = Depends(database.get_db)):
   
    return methods.create(request= request, db= db, model = models.Notes)

@router.get('/',status_code = status.HTTP_200_OK, response_model= List[schemas.showNote])
def all(db: Session = Depends(database.get_db)):

    return methods.show_list(db= db, model = models.Notes)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model= schemas.showNote)
def get(id:int, db: Session = Depends(database.get_db)):
    return methods.retrieve(db= db, id = id, model = models.Notes)

@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def put(id:int,request:schemas.Note, db: Session = Depends(database.get_db)):
    return methods.update(db= db, id = id, request = request, model = models.Notes)

@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def delete(id:int, db: Session = Depends(database.get_db)):
    return methods.delete(db= db, id= id, model = models.Notes)

@router.get('/user/{user_id}', status_code = status.HTTP_200_OK, response_model = List[schemas.showNote])
def get_user_notes(user_id:int, db: Session = Depends(database.get_db)):
    return note.get_user_notes(user_id = user_id, db= db, model = models.Notes)