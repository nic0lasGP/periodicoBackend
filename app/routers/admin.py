from fastapi import APIRouter,HTTPException
from app.services import *
from app.models.admin import PostCreate


app = APIRouter(tags=['Admin'])





@app.patch("/admin/alternate-publish-state-post")
async def alternate_publish(id:int):
    try:
        new_state = publishState(id)
            
        if new_state == 0:
            print("error aqui")
            publishAlternate(id,1)

            return {"status": new_state, "message": "Post publicado correctamente"}
        else:
            print("error aqui")
            publishAlternate(id,0)
        
            return {"status": new_state, "message": "Post despublicado correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.delete("/admin/delete-post")
async def delete_post(id:int):

    try:
        deletePost(id)
        return {"status": "ok", "message": "Post borrado correctamente"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))



@app.post("/admin/create-post")
async def create_post(data: PostCreate):
    body_json = data.body.model_dump_json()
    
    try:
        createPost(
            title=data.title,
            body=body_json,
            user_id=data.user_id,
            section_id=data.section_id,
            slug=data.slug
        )
        return {"status": "ok", "message": "Post creado correctamente"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
    

@app.post("/admin/create-section")
async def create_section(name:str):

    new_id = createSection(name)

    return {
        "status": "ok",
        "message": "Sección creada correctamente",
        "id": new_id
    }


@app.delete("/admin/delete-section")
async def delete_section(section_id: int):

    deleted = deleteSection(section_id)

    if deleted == 0:
        raise HTTPException(status_code=404, detail="La sección no existe")

    return {
        "status": "ok",
        "message": f"Sección con ID {section_id} eliminada correctamente"
    }



