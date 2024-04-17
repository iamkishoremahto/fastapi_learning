from sqlalchemy.orm import Session
from ... import models, schemas
from ...UTILITIES import hashing
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
import re


def isEmail(email):
    pattern = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
    return re.match(pattern, email, re.IGNORECASE)



def create_new_user(request:schemas.User,db: Session):

    if isEmail(request.email):
        new_user = models.Users(**request.dict())
        new_user.password = hashing.hashPassword(request.password)
        db.add(new_user)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already in use")
        db.refresh(new_user)
        return new_user
    else:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Invalid email address")



