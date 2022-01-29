from fastapi import FastAPI
from DB.database import engine
from DB import models
from routers import (
    user
)

models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(user.router)


@app.get('/')
def indext():
    return
