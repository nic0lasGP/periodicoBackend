from fastapi import APIRouter
from app.services.sections import *
from app.services.posts import *


app = APIRouter(tags=['Noticias'])

##maybe cambiar ruta
@app.get("/")
async def get_allposts():
    results = getAllPost()
    return results

@app.get("/secciones")
async def get_section():
    results= getAllSections()

    return results


@app.get("/noticias/{seccion}")
def get_post_by_seccion(section:str):
    """Proporciona todos los posts de una section"""
    idsection = getIdSectionByName(section)
    results =  getPostbySectionId(idsection)
    
    return results


@app.get("/noticias/{seccion}/{slug}")
def get_post(section:str,slug:str):

    section_id = getIdSectionByName(section)
    results = getExactPost (section_id,slug)
    return results



