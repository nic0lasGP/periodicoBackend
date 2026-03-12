from app.routers.admin import app as admin_router
from app.routers.posts import app as posts_router
from app.routers.users import app as users_router
from app.routers.sections import app as sections_router


__all__ =[
    "admin_router",
    "posts_router", 
    "users_router",
    "sections_router"
]   