import pymysql
from app.util import get_connection


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
                    "SELECT id FROM sections WHERE name = %s ",(seccionNombre,)
                )
                results = cursor.fetchone()
                return results["id"]


def getSectionById(id:int):
     with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM sections WHERE id = %s ",(id,)
                )
                results = cursor.fetchone()
                return results
            

def getSectionByName(name:str):
     with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM sections WHERE name = %s ",(name,)
                )
                results = cursor.fetchone()
                return results
        

def deleteSection(section_id: int):
    try:    
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM sections WHERE id = %s",
                    (section_id,)
                )
            connection.commit()
            return cursor.rowcount
    except Exception as e:
         raise e
    

def createSection(name: str):
    try:    
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO sections (name) VALUES (%s)",
                    (name,)
                )
            connection.commit()
            return cursor.lastrowid
    except Exception as e:
         raise e