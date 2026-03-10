from fastapi import APIRouter
from app.services.sections import *
from app.services.noticias import *


app = APIRouter(tags=['Noticias'])


@app.get("/secciones")
async def get_secciones():
    resultados= getAllSections()

    return resultados


@app.get("/noticias/{seccion}")
def get_noticias_by_seccion(seccion:str):
    """test"""
    idseccion = getIdSectionByName(seccion)
    resultados =  getNoticiasbySeccion(idseccion)
    
    return resultados


@app.get("/noticias/{seccion}/{slug}")
def get_noticia(seccion:str,slug:str):

    seccion_id = getIdSectionByName(seccion)
    resultados = getExactNoticia (seccion_id,slug)
    return resultados