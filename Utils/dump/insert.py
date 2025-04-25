import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Infraestructure.Data.DBContext import Base
from Infraestructure.Data.DBContext import RegionalDB, DistritoDB, CentroDB

import os
import sys


excel_path = os.path.join(
    'C:/Users/david/OneDrive - Instituto Tecnológico de Las Américas (ITLA)/Documentos/Aprendizaje/Regionales_centros_educativos/src/Infraestructure/Data/Repositorios/centrosModif.xlsx'
)


print(f"Ruta del archivo Excel: {excel_path}")


try:
    df = pd.read_excel(excel_path, dtype={
    'codigo_regional': str,
    'codigo_distrito': str,
    'codigo_centro': str
    })
    df.fillna('No encontrado', inplace=True)
except FileNotFoundError:
    print(f"El archivo no se encuentra en la ruta especificada: {excel_path}")
    sys.exit(1)


excel_dir = os.path.dirname(excel_path)


db_path = os.path.join(excel_dir, 'centros.db')
DATABASE_URL = f'sqlite:///{db_path}'

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

def insertar_datos():
    
    Base.metadata.create_all(engine)

    session = SessionLocal()
    session.query(CentroDB).delete()
    session.query(DistritoDB).delete()
    session.query(RegionalDB).delete()
    session.commit()

    try:
        for _, row in df.iterrows():
            
            try:
                lat = float(str(row['Coordenadas Latitud']).replace(',', '.'))
                lon = float(str(row['Coordenadas Longitud']).replace(',', '.'))
            except ValueError:
                print(f"Error en coordenadas en la fila:\n{row}")
                continue  

            regional = RegionalDB(
                codigo=str(row['codigo_regional']),
                nombre=str(row['nombre_regional'])
            )
            session.add(regional)

            distrito = DistritoDB(
                codigo=str(row['codigo_distrito']),
                codigo_regional=str(row['codigo_regional']),
                nombre=str(row['nombre_distrito'])
            )
            session.add(distrito)
            codigo_centro = row['codigo_centro']
            try:
                codigo_centro = str(int(float(codigo_centro)))  
            except:
                codigo_centro = str(codigo_centro)
            centro = CentroDB(
                codigo=codigo_centro,
                codigo_regional=str(row['codigo_regional']),
                codigo_distrito=str(row['codigo_distrito']),
                nombre=str(row['nombre_centro']),
                sector=str(row['Sector']),
                nivel=str(row['Nivel']),
                cord_latitud=lat,
                cord_longitud=lon,
                matricula=int(row['Matricula']),  
                planta_fisica=str(row['Planta Fisica']),
                provincia=str(row['Provincia']),
                municipio=str(row['Municipio'])
            )
            session.add(centro)



        session.commit()
        print(f"Datos insertados correctamente en la base de datos:\n{db_path}")

    except Exception as e:
        print(f"Error al insertar los datos: {e}")
        session.rollback()
    
    finally:
        session.close()

if __name__ == '__main__':
    insertar_datos()
