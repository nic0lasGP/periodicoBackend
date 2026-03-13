from fastapi import APIRouter,HTTPException,File, UploadFile,Depends
from fastapi.responses import StreamingResponse 
from app.services import *
from app.security import requireAdmin
import os
import shutil

app = APIRouter(tags=['Media'])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


ALLOWED_TYPES_VIDEO = {
    "video/mp4", "video/webm"
}
MAX_SIZE_VIDEO = 100 * 1024 * 1024


    

@app.post("/upload/video")
async def upload_video(post_id: int, file: UploadFile = File(...),current_user: dict = Depends(requireAdmin)):
    

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
    if not video:
        raise HTTPException(404, "Video no encontrado")

    data = video["data"]
    if isinstance(data, str):
        data = data.encode("latin-1")

    def video_stream():
        chunk_size = 1024 * 1024  
        for i in range(0, len(data), chunk_size):
            yield data[i:i + chunk_size]

    return StreamingResponse(
        video_stream(),
        media_type=video["mime_type"], 
        headers={
            "Content-Disposition": f"inline; filename={video['filename']}",
            "Content-Length": str(len(data)),
            "Accept-Ranges": "bytes"
        }
    )