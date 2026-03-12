from fastapi import APIRouter
from app.services import *


app = APIRouter(tags=['Noticias'])

##maybe cambiar ruta


@app.get("/posts/get-all")
async def get_all_posts():
    results = getAllPost()
    return results


@app.get("/posts/get-by-id")
async def get_all_posts(id:int):
    results = getPostbyId(id)
    return results


@app.get("/posts/get-all-by-section")
def get_post_by_seccion(section:str):
    """Proporciona todos los posts de una section"""
    idsection = getIdSectionByName(section)
    results =  getPostbySectionId(idsection)
    
    return results


@app.get("/posts/{seccion}/{slug}")
def get_post(section:str,slug:str):

    section_id = getIdSectionByName(section)
    results = getExactPost (section_id,slug)
    return results



