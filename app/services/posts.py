from app.util import get_connection
import json



def getAllPost():
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM posts ORDER BY created_at DESC"
                )
                results = cursor.fetchall()
                return results
            
            
def getPostbySectionId(seccion_id:int):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM posts WHERE section_id = %s ORDER BY created_at DESC",(seccion_id,)
                )
                results = cursor.fetchall()
                return results
            

def getExactPost(seccion_id:int,slug:str):
     """Se le introduce el id de la seccio y el slug de la noticia desada a encontrar"""
     with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM posts WHERE section_id = %s AND slug = %s", (seccion_id, slug)                )
                results = cursor.fetchone()
                return results


def getPostbyId(id:int):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM posts WHERE id = %s ",(id)
                )
                results = cursor.fetchone()
                return results


## Mirar si se recibe el slug o hay que crearlo automaticamente 
def createPost(title:str,body:dict,user_id:int,section_id:int,slug:str):

    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO posts (title, slug, body, user_id, section_id)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (title, slug, body, user_id, section_id)

                )
                connection.commit()            
                return True
    except Exception as e:
        raise e


def updatePost(post_id: int, title: str, body: dict, section_id: int, slug: str):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    UPDATE posts 
                    SET title = %s, slug = %s, body = %s, section_id = %s
                    WHERE id = %s
                    """,
                    (title, slug, body, section_id, post_id)
                )
                connection.commit()
                return cursor.rowcount > 0
    except Exception as e:
        raise e
    

def publishState(post_id: int):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT published FROM posts WHERE id = %s",
                (post_id,)
            )
            result = cursor.fetchone()

            if result is None:
                return None  # No existe el post

            return result["published"]



def publishAlternate(post_id:int,state:int):
    try:
        with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE posts
                        SET published = %s
                        WHERE id = %s;
                        """,
                        (state,post_id,)

                    )
                    connection.commit()           
                    return True
    except Exception as e:
         raise e
    

def deletePost(id: int):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM posts
                    WHERE id = %s
                    """,
                    (id,)
                )

            connection.commit()
            return cursor.rowcount > 0  # True si se eliminó algo

    except Exception as e:
        print("Error", e)
        raise e