from sqlmodel import create_engine, Session
from Infraestructure.Data.DBContext import SQLModel


import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # <- apunta a Infraestructure/Repositorio
CONFIG_PATH = os.path.join(BASE_DIR, "appsettings.json")

with open(CONFIG_PATH, "r") as config_file:
    config = json.load(config_file)

DATABASE_URL = config["database"]["connection_string"]

engine = create_engine(DATABASE_URL, echo=True)

def get_session() -> Session:
    """ Función que retorna una sesión de base de datos """
    with Session(engine) as session:
        yield session