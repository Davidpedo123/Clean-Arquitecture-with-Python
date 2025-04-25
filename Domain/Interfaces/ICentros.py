# domain/repositories/distrito_repository_interface.py
from abc import ABC, abstractmethod
from typing import List
from Entities.CentrosDomain import Regional, Distrito, Centro



class RegionalRepositoryInterface(ABC):
    @abstractmethod
    def mostrar_regionales(self) -> List[Regional]:
        pass




class DistritoRepositoryInterface(ABC):
    @abstractmethod
    def mostrar_distritos(self) -> List[Distrito]:
        pass

    @abstractmethod
    def distritos_por_regional(self, codigo: str) -> List[Distrito]:
        pass
    
    


class CentroRepositoryInterface(ABC):
    @abstractmethod
    def mostrar_centros(self) -> List[Centro]:
        pass

    @abstractmethod
    def mostrar_centros_distritos(self, codigo_distrito: str) -> List[Centro]:
        pass

    @abstractmethod
    def mostrar_centros_provincia(self, provincia: str) -> List[Centro]:
        pass

    @abstractmethod
    def mostrar_centros_municipio(self, municipio: str) -> List[Centro]:
        pass

    @abstractmethod
    def mostrar_centros_sector(self, sector: str) -> List[Centro]:
        pass