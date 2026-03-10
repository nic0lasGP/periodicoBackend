import pymysql
from app.util.connector.connector import get_connection

def getAllSections():
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM sections"
                )
                resultados = cursor.fetchall()
                return resultados
def getIdSectionByName(seccionNombre:str):
     with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM sections WHERE name = %s ",(seccionNombre)
                )
                resultado = cursor.fetchone()
                return resultado["id"]