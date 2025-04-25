from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Data.DBContext import Base

DATABASE_URL = 'sqlite:///centros.db'

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def crear_tablas():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    crear_tablas()