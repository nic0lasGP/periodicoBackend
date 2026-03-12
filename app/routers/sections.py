from fastapi import APIRouter,HTTPException
from app.services import *
from app.models.admin import PostCreate


app = APIRouter(tags=['Sections'])


@app.get("/sections/get-all")
async def get_all_sections():
    results = getAllSections()
    return results


@app.get("/sections/get-by-id")
async def get_section_by_id(id:int):
    results = getSectionById(id)
    return results
