import pymysql
from app.util.connector.connector import get_connection
##TERMINAR FUNCIONES RESTANTES

def getAllUsers():
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM users"
                )
                resultados = cursor.fetchall()
             
                return resultados
def getUserById(id: int):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM users WHERE id = %s",(id)
                )
                resultados = cursor.fetchone()
                
               
                ## print(resultados)
                return resultados
