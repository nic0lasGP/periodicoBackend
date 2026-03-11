import os
from contextlib import contextmanager
import pymysql
from pymysql.cursors import DictCursor


@contextmanager
def get_connection():
    connection = None
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            user=os.getenv("DB_USER", "root"),
            port=int(os.getenv("DB_PORT", "3306")),
            password=os.getenv("DB_PASSWORD", "password"),
            database=os.getenv("DB_NAME", "periodicodb"),
            autocommit=True,
            cursorclass=DictCursor,
        )
        yield connection
        connection.commit()
    except Exception as e:
        print("[get_connection] Error durante la conexión o transacción: %s", e)
        if connection:
            connection.rollback()
        raise e
    finally:
        if connection:
            try:
                connection.close()
            except Exception as e:
                print("[get_connection] Error al cerrar la conexión: %s", e)