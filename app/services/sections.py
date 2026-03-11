import pymysql
from app.util.connector import get_connection

def getAllSections():
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM sections"
                )
                results = cursor.fetchall()
                return results
def getIdSectionByName(seccionNombre:str):
     with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id FROM sections WHERE name = %s ",(seccionNombre)
                )
                results = cursor.fetchone()
                return results["id"]