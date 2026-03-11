import pymysql
from app.util.connector import get_connection
from app.security.validates import validatePassword
##TERMINAR FUNCIONES RESTANTES

def getAllUsers():
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM users"
                )
                results = cursor.fetchall()
             
                return results
            

def getUserById(id: int):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM users WHERE id = %s",(id)
                )
                results = cursor.fetchone()
                
               
                ## print(results)
                return results
            

def getUserByName(name: str):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM users WHERE username = %s",(name)
                )
                results = cursor.fetchone()
                
               
                ## print(results)
                return results


## POR CAMBIAR !!!!!!!!!!!!!!!!!!! , encriptar la contraseña
def createUser(username:str,password:str):
    
    if not validatePassword(password):
        print("La contraseña no cumple los requisitos")
        return None
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, password)

            )
            results = cursor.fetchone()
                           
            return results
