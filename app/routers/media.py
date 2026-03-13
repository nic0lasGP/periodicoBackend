from fastapi import APIRouter,HTTPException,File, UploadFile
from app.services.media import uploadImageCover,getCoverById,getCoverByIdPost
import os
import shutil

app = APIRouter(tags=['Media'])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_TYPES_IMG = {
    "image/jpeg", "image/png", "image/gif", "image/webp",
}
ALLOWED_TYPES_VIDEO = {
    "video/mp4", "video/webm"
}
MAX_SIZE = 100 * 1024 * 1024

@app.post("/upload/image-cover")
async def upload_image_cover(post_id:int,file: UploadFile = File(...)):
    # Validar tipo de archivo
    
    if file.content_type not in ALLOWED_TYPES_IMG:
        raise HTTPException(400, "Tipo de archivo no permitido")
    if file.size > MAX_SIZE:
        raise HTTPException(400, "Tamaño exedido de 100MB")
    
    content = await file.read()

    media = uploadImageCover(post_id,file.filename, file.content_type, content, len(content))
    
    return {"filename": file.filename, "result": media}
@app.get("/media/cover/by-id")
def get_cover_by_id(media_id: int):
    media= getCoverById(media_id)
    if not media:
        raise HTTPException(404, "Archivo no encontrado")

    return media
@app.get("/media/cover/by-id-post")
def get_cover_by_id_post(post_id: int):
    media= getCoverByIdPost(post_id)
    if not media:
        raise HTTPException(404, "Archivo no encontrado")

    return media
    