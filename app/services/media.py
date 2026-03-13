from app.util import get_connection

#Video

def uploadVideo(post_id:int,filename:str,mime_type:str,data:bytes,size:int):

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """ INSERT INTO videos (post_id, filename, mime_type, data, size)
                    VALUES (%s, %s, %s, %s, %s)""",(post_id,filename,mime_type,data,size)
                )
                connection.commit
                
        return "Video Guardada"
    except Exception as e:
        raise e


def getVideosByPost(post_id: int):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, post_id, filename, mime_type, size, created_at FROM videos WHERE post_id = %s",
                    (post_id,)
                )
                return cursor.fetchall()
    except Exception as e:
        raise e
def getVideosById(id: int):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id, post_id, filename, mime_type,data, size, created_at FROM videos WHERE id = %s",
                    (id,)
                )
                return cursor.fetchone()
    except Exception as e:
        raise e

