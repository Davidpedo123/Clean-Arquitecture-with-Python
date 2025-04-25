# Application/Interfaces/ICentroServicio.py

from Application.DTOs.DTOCentros import CentroDTO
from sqlmodel import Session
from typing import List

class ICentroServicio:
    def agregar_centro(self, session: Session, centro_dto: CentroDTO) -> None:
        """ Método para agregar un centro """
        pass
    
    def mostrar_centros(self, session: Session) -> List[CentroDTO]:
        """ Método para mostrar todos los centros """
        pass
    
    def centros_por_distrito(self, session: Session, codigo_distrito: str) -> List[CentroDTO]:
        """ Método para obtener centros por código de distrito """
        pass
    
    def centros_por_provincia(self, session: Session, provincia: str) -> List[CentroDTO]:
        """ Método para obtener centros por provincia """
        pass
    
    def centros_por_municipio(self, session: Session, municipio: str) -> List[CentroDTO]:
        """ Método para obtener centros por municipio """
        pass
    
    def centros_por_sector(self, session: Session, sector: str) -> List[CentroDTO]:
        """ Método para obtener centros por sector """
        pass
    
    def buscar_por_parametros(self, session: Session, provincia: str = None, municipio: str = None, sector: str = None) -> List[CentroDTO]:
        """ Método para buscar centros por parámetros """
        pass
    
class IDistritoServicio:
    def obtener_distritos_por_regional(self, session: Session, codigo_regional: str) -> List[CentroDTO]:
        """ Método para obtener distritos por código de regional """
        pass
    
    def mostrar_distritos(self, session: Session) -> List[CentroDTO]:
        """ Método para mostrar todos los distritos """
        pass
    
    def agregar_distrito(self, session: Session, distrito_dto: CentroDTO) -> None:
        """ Método para agregar un nuevo distrito """
        pass

class IRegionalServicio:
    def obtener_regionales(self, session: Session) -> List[CentroDTO]:
        """ Método para obtener todas las regionales """
        pass
    
    def agregar_regional(self, session: Session, regional_dto: CentroDTO) -> None:
        """ Método para agregar una nueva regional """
        pass
    
    def mostrar_regionales(self, session: Session) -> List[CentroDTO]:
        """ Método para mostrar todas las regionales """
        pass
    
