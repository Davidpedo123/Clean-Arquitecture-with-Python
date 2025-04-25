from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Infraestructure.Data.DBContext import Base
import os
from pathlib import Path


print("Iniciando script de creación de tablas...")  

db_path = os.path.join(os.path.dirname(__file__), 'centros.db')
DATABASE_URL = f"sqlite:///{db_path}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def crear_tablas():
    try:
        print("Creando tablas...")
        Base.metadata.create_all(engine)
        print("Tablas creadas.")
    except Exception as e:
        print(f"Error al crear tablas: {e}")

crear_tablas()