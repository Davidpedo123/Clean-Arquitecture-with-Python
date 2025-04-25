# Application/Servicios/ServicioCentro.py

from Application.Interfaces.ICentrosGenerales import ICentroServicio, IDistritoServicio, IRegionalServicio
from Application.CasosDeUso.CasoCentrosGenerales import CentroCasoDeUso, RegionalCasoDeUso, DistritoCasoDeUso
from Application.DTOs.DTOCentros import CentroDTO, RegionalDTO, DistritoDTO
from sqlmodel import Session



class ServicioCentro(ICentroServicio):
    def __init__(self):
        self.centro_caso_de_uso = CentroCasoDeUso()  
    
    def agregar_centro(self, session: Session, centro_dto: CentroDTO):
        """ Implementación del método de agregar un centro """
        return self.centro_caso_de_uso.agregar_centro(session, centro_dto)
    
    def mostrar_centros(self, session: Session):
        """ Implementación del método para mostrar todos los centros """
        return self.centro_caso_de_uso.mostrar_centros(session)
    
    def centros_por_distrito(self, session: Session, codigo_distrito: str):
        """ Implementación del método para obtener centros por código de distrito """
        return self.centro_caso_de_uso.centros_por_distrito(session, codigo_distrito)
    
    def centros_por_provincia(self, session: Session, provincia: str):
        """ Implementación del método para obtener centros por provincia """
        return self.centro_caso_de_uso.centros_por_provincia(session, provincia)
    
    def centros_por_municipio(self, session: Session, municipio: str):
        """ Implementación del método para obtener centros por municipio """
        return self.centro_caso_de_uso.centros_por_municipio(session, municipio)
    
    def centros_por_sector(self, session: Session, sector: str):
        """ Implementación del método para obtener centros por sector """
        return self.centro_caso_de_uso.centros_por_sector(session, sector)
    
    
    def buscar_por_parametros(self, session: Session, provincia: str = None, municipio: str = None, sector: str = None):
        """ Implementación del método para buscar centros por parámetros """
        return self.centro_caso_de_uso.buscar_por_parametros(session, provincia, municipio, sector)

class ServicioDistrito(IDistritoServicio):
    def __init__(self):
        self.distrito_caso_de_uso = DistritoCasoDeUso()  
    
    def obtener_distritos_por_regional(self, session: Session, codigo_regional: str):
        """ Implementación del método para obtener distritos por código de regional """
        return self.distrito_caso_de_uso.distritos_por_regional(session, codigo_regional)
    
    def mostrar_distritos(self, session: Session):
        """ Implementación del método para mostrar todos los distritos """
        return self.distrito_caso_de_uso.mostrar_distritos(session)
    
    def agregar_distrito(self, session: Session, distrito_dto: DistritoDTO):
        """ Implementación del método para agregar un nuevo distrito """
        return self.distrito_caso_de_uso.agregar_distrito(session, distrito_dto)  

class ServicioRegional(IRegionalServicio):
    def __init__(self):
        self.regional_caso_de_uso = RegionalCasoDeUso()  
    
    def obtener_regionales(self, session: Session):
        """ Implementación del método para obtener todas las regionales """
        return self.regional_caso_de_uso.obtener_regionales(session)
    
    def agregar_regional(self, session: Session, regional_dto: RegionalDTO):
        """ Implementación del método para agregar una nueva regional """
        return self.regional_caso_de_uso.agregar_regional(session, regional_dto)  
    
    def mostrar_regionales(self, session: Session):
        """ Implementación del método para mostrar todas las regionales """
        return self.regional_caso_de_uso.mostrar_regionales(session) 
    
 
    
    