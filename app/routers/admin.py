from fastapi import APIRouter,HTTPException
from app.services.posts import *
from app.models.admin import PostCreate


app = APIRouter(tags=['Admin'])



###Mirar si hace falta juntar estas 3 endpoints en uno 
@app.get("/admin-hub-posts")
async def get_allposts():
    results = getAllPost()
    return results


@app.patch("/admin/alternar-publicar")
async def alternate_publish(id:int):
    try:
        new_state = publishState(id)
            
        if new_state == 0:
            print("error aqui")
            publishPost(id)

            return {"status": new_state, "message": "Post publicado correctamente"}
        else:
            print("error aqui")
            unPublishPost(id)
        
            return {"status": new_state, "message": "Post despublicado correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




@app.delete("/admin/borrar")
async def remove_post(id:int):

    try:
        deletePost(id)
        return {"status": "ok", "message": "Post borrado correctamente"}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
###



@app.post("/admin/crear-noticia")
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