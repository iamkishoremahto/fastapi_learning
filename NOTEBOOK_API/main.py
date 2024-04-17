from fastapi import FastAPI
from . import models, database
from .ROUTERS import user,note



app = FastAPI()

models.Base.metadata.create_all(bind= database.engine)

app.include_router(user.router)
app.include_router(note.router)