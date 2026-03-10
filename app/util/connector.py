from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/periodicodb"

def connectDB():
    
    try:
        engine = create_engine(DATABASE_URL, echo=True)
        connection = engine.connect()

        print("Conexion realizada exitosamente a la base de datos")
    except Exception as e:  
        print("Error:",e)