from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from DB.database import engine
from DB import models
from routers import (
    user, post, login
)

models.Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(login.router)
app.include_router(user.router)
app.include_router(post.router)

app.mount("/public/images", StaticFiles(directory='public/images'), name="images")
