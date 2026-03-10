import pymysql
from app.util.connector.connector import get_connection

## Cambiar nombre de tabla en la base de datos 
def getAllNoticias():
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM posts"
                )
                resultados = cursor.fetchall()
                return resultados
def getNoticiasbySeccion(seccion_id:int):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM posts WHERE section_id = %s ",(seccion_id,)
                )
                resultados = cursor.fetchall()
                return resultados
def getExactNoticia(seccion_id:int,slug:str):
     """Se le introduce el id de la seccio y el slug de la noticia desada a encontrar"""
     with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM posts WHERE section_id = %s AND slug = %s", (seccion_id, slug)                )
                resultados = cursor.fetchone()
                return resultados