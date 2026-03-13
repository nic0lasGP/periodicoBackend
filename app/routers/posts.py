from fastapi import APIRouter
from app.services import *
import zlib
import json

app = APIRouter(tags=['Noticias'])

##maybe cambiar ruta


@app.get("/posts/get-all")
async def get_all_posts():
    results = getAllPost()

    for result in results:
        if result["body"]:
            body_decompressed = zlib.decompress(result["body"])
            result["body"] = json.loads(body_decompressed.decode("utf-8"))

    return results


@app.get("/posts/get-by-id")
async def get_all_posts(id:int):
    results = getPostbyId(id)


    if results and results["body"]:
       # Descomprimir el body al leerlo
        body_decompressed = zlib.decompress(results["body"])
        results["body"] = json.loads(body_decompressed.decode("utf-8"))
    return results


@app.get("/posts/get-all-by-section")
def get_post_by_seccion(section:str):
    """Proporciona todos los posts de una section"""
    idsection = getIdSectionByName(section)
    results =  getPostbySectionId(idsection)
    
    for result in results:
        if result["body"]:
            body_decompressed = zlib.decompress(result["body"])
            result["body"] = json.loads(body_decompressed.decode("utf-8"))

    return results


@app.get("/posts/{seccion}/{slug}")
def get_post(section:str,slug:str):

    section_id = getIdSectionByName(section)
    results = getExactPost (section_id,slug)
    if results and results["body"]:
       # Descomprimir el body al leerlo
        body_decompressed = zlib.decompress(results["body"])
        results["body"] = json.loads(body_decompressed.decode("utf-8"))
    return results



