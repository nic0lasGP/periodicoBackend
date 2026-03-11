import app.services.user as user
import app.routers as routers

from fastapi import FastAPI
from app.services.sections import *
from app.services.posts import *
import app.security.validates as val
import app.security.encrypt_passwords as ecrypt

app = FastAPI(tags=["Main"])


app.include_router(routers.posts_router)
app.include_router(routers.admin_router)
app.include_router(routers.users_router)



@app.get("/User/{id}")
async def get_post(id: int):
    show = user.getUserById(id)
    return {"show":show}


