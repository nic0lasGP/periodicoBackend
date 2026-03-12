import pymysql
from app.util.database import get_connection
from app.security.validates import validatePassword
from app.security.encrypt_passwords import hash_password
##TERMINAR FUNCIONES RESTANTES


def getAllUsers():
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id,username,gmail,created_at,admin FROM users"
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
def getUserByGmail(gmail:str):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM users WHERE gmail = %s",
                (gmail,)
            )
            results = cursor.fetchone()

            return results
def getUserById(id:int):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id,username,gmail,created_at,admin FROM users WHERE id = %s",
                (id,)
            )
            results = cursor.fetchone()

            return results  

## POR CAMBIAR !!!!!!!!!!!!!!!!!!! añadir verificacion de gmails  
def createUser(username:str,password:str,gmail:str):
    
    if not validatePassword(password):
        print("La contraseña no cumple los requisitos")
        return None
    hashed_password = hash_password(password)
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (username, password,gmail) VALUES (%s, %s,%s)",
                (username, hashed_password,gmail)

            )
            results = cursor.fetchone()
                           
            return results
def deleteUserbyId(id: int):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    DELETE FROM users
                    WHERE id = %s
                    """,
                    (id,)
                )

            connection.commit()
            return cursor.rowcount > 0  # True si se eliminó algo

    except Exception as e:
        print("Error", e)
        raise e


