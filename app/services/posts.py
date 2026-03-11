from app.util.connector import get_connection
import json
import app.services as init


def getAllPost():
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM posts"
                )
                results = cursor.fetchall()
                return results
            
            
def getPostbySectionId(seccion_id:int):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM posts WHERE section_id = %s ",(seccion_id,)
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
                results = cursor.fetchaone()
                return results


## Mirar si se recibe el slug o hay que crearlo automaticamente 
def createPost(title:str,body:json,user_id:int,section_id:int,slug:str):

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


def publishState(post_id:int):
    try:
        with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """SELECT published FROM posts WHERE id = %s """,(post_id)
                    )
                    results = cursor.fetchaone()
                    return results
    except Exception as e:
         raise e


def publishPost(post_id:int):
    try:
        with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE posts
                        SET published = 1
                        WHERE id = %s;
                        """,
                        (post_id)

                    )
                    connection.commit()           
                    return True
    except Exception as e:
         raise e
    

def unPublishPost(post_id:int):
    try:
        with get_connection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE posts
                        SET published = 0
                        WHERE id = %s;
                        """,
                        (post_id)

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