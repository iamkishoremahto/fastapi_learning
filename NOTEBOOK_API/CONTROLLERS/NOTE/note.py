from sqlalchemy.orm import Session
from ... import models, schemas
from ...UTILITIES import hashing
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status


def get_user_notes(user_id, db:Session, model):

    notes = db.query(model).filter(model.user_id == user_id).all()
    if not notes:
        raise HTTPException(status_code = status.HTTP_204_NO_CONTENT, detail = "This user not having any notes")
    return notes