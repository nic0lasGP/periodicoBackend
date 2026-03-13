import app.services.user as user
import app.routers as routers
from fastapi.middleware.cors import CORSMiddleware
from fastapi import  Depends, FastAPI
from app.services import *
from app.security.authToken import *


app = FastAPI(tags=["Main"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)





app.include_router(routers.posts_router)
app.include_router(routers.admin_router)
app.include_router(routers.users_router)
app.include_router(routers.sections_router)
app.include_router(routers.media_router)