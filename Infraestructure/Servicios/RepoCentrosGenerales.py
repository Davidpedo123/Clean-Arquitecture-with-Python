# Infraestructure/Repositorios/RegionalRepositorio.py
from sqlmodel import Session
from Infraestructure.Data.DBContext import RegionalDB, DistritoDB, CentroDB
from Infraestructure.Repositorio.engine import get_session

class RegionalRepositorio:
    def __init__(self):
        pass

    def mostrar_regionales(self, session: Session):
        """ Mostrar todas las regionales """
        return session.query(RegionalDB).all()

    def agregar_regional(self, session: Session, codigo: str, nombre: str):
        """ Agregar una nueva regional """
        nueva_regional = RegionalDB(codigo=codigo, nombre=nombre)
        session.add(nueva_regional)
        session.commit()
        return nueva_regional

class DistritoRepositorio:
    def __init__(self):
        pass

    def mostrar_distritos(self, session: Session):
        """ Mostrar todos los distritos """
        return session.query(DistritoDB).all()

    def agregar_distrito(self, session: Session, codigo: str, codigo_regional: str, nombre: str):
        """ Agregar un nuevo distrito """
        nuevo_distrito = DistritoDB(codigo=codigo, codigo_regional=codigo_regional, nombre=nombre)
        session.add(nuevo_distrito)
        session.commit()
        return nuevo_distrito
    

    def distritos_por_regional(self, session: Session, codigo_regional: str):
        """ Obtener distritos por código de regional """
        return session.query(DistritoDB).filter(DistritoDB.codigo_regional == codigo_regional).all()
    
    
class CentroRepositorio:
    def __init__(self):
        pass

    def mostrar_centros(self, session: Session):
        """ Mostrar todos los centros """
        return session.query(CentroDB).all()

    def agregar_centro(self, session: Session, codigo: str, codigo_regional: str, codigo_distrito: str, nombre: str, sector: str, nivel: str, cord_latitud: float, cord_longitud: float, matricula: str, planta_fisica: str, provincia: str, municipio: str):
        """ Agregar un nuevo centro """
        nuevo_centro = CentroDB(codigo=codigo, codigo_regional=codigo_regional, codigo_distrito=codigo_distrito, nombre=nombre, sector=sector, nivel=nivel, cord_latitud=cord_latitud, cord_longitud=cord_longitud, matricula=matricula, planta_fisica=planta_fisica, provincia=provincia, municipio=municipio)
        session.add(nuevo_centro)
        session.commit()
        return nuevo_centro
    
    def centros_por_distrito(self, session: Session, codigo_distrito: str):
        """ Obtener centros por código de distrito """
        return session.query(CentroDB).filter(CentroDB.codigo_distrito == codigo_distrito).all()
    
    def centros_por_provincia(self, session: Session, provincia: str):
        """ Obtener centros por provincia """
        return session.query(CentroDB).filter(CentroDB.provincia == provincia).all()
    
    def centros_por_municipio(self, session: Session, municipio: str):
        """ Obtener centros por municipio """
        return session.query(CentroDB).filter(CentroDB.municipio == municipio).all()
    
    def centros_por_sector(self, session: Session, sector: str):
        """ Obtener centros por sector """
        return session.query(CentroDB).filter(CentroDB.sector == sector).all()
    
    
    def buscar_por_parametros(self, session: Session, provincia: str = None, municipio: str = None, sector: str = None):
        """ Buscar centros por parámetros opcionales """
        query = session.query(CentroDB)
        if provincia:
            query = query.filter(CentroDB.provincia == provincia)
        if municipio:
            query = query.filter(CentroDB.municipio == municipio)
        if sector:
            query = query.filter(CentroDB.sector == sector)
        return query.all()