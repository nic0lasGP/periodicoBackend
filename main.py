import app.services.user as user
from fastapi import FastAPI
from app.routers.noticias import app as noticias_router
#quitar despues
from app.services.sections import *
from app.services.noticias import *


app = FastAPI()
app.include_router(noticias_router)
print(getIdSectionByName("Viajes"))
@app.get("/")
def read_root():
    return {"Hello": "World"}




@app.get("/User/{id}")
async def get_post(id: int):
    show = user.getUserById(id)
    return {"show":show}
    