from fastapi import APIRouter,HTTPException,File, UploadFile
from fastapi.responses import StreamingResponse 
from app.services.media import *
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
MAX_SIZE_VIDEO = 100 * 1024 * 1024

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
    

@app.post("/upload/video")
async def upload_video(post_id: int, file: UploadFile = File(...)):
    

    if file.content_type not in ALLOWED_TYPES_VIDEO:
        raise HTTPException(400, "Tipo de archivo no permitido")
    if file.size > MAX_SIZE_VIDEO:
        raise HTTPException(400, "Tamaño excedido de 500MB")

    content = await file.read()

    video = uploadVideo(post_id, file.filename, file.content_type, content, len(content))

    return {"filename": file.filename, "result": video}


@app.get("/media/video/{video_id}")
def get_video(video_id: int):

    video = getVideosById(video_id)
    print(video)
    if not video:
        raise HTTPException(404, "Video no encontrado")

    data = video["data"]
    if isinstance(data, str):
        data = data.encode("latin-1")

    def video_stream():
        chunk_size = 1024 * 1024  # 1MB por chunk
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]

    return StreamingResponse(
        video_stream(),
        media_type=video["mime_type"],  # ✅ que sea "video/mp4"
        headers={
            "Content-Disposition": f"inline; filename={video['filename']}",
            "Content-Length": str(len(data)),
            "Accept-Ranges": "bytes"
        }
    )