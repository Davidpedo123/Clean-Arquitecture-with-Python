# Application/CasosDeUso/RegionalCasoDeUso.py
from Infraestructure.Servicios.RepoCentrosGenerales import RegionalRepositorio, CentroRepositorio, DistritoRepositorio
from Infraestructure.Repositorio.engine import get_session
from Application.DTOs.DTOCentros import CentroDTO, RegionalDTO, DistritoDTO
from sqlmodel import Session



# Importar la función get_session desde el módulo engine
class CentroCasoDeUso:
    def __init__(self, centro_dto: CentroDTO = None):
        self.centro_repo = CentroRepositorio()
        self.centro_dto = centro_dto if centro_dto else CentroDTO()

    def mostrar_centros(self, session: Session):
        """ Lógica de negocio para mostrar todos los centros """
        return self.centro_repo.mostrar_centros(session)

    def agregar_centro(self, session: Session):
        """ Lógica de negocio para agregar un nuevo centro """
        return self.centro_repo.agregar_centro(
            session,
            self.centro_dto.codigo,
            self.centro_dto.codigo_regional,
            self.centro_dto.codigo_distrito,
            self.centro_dto.nombre,
            self.centro_dto.sector,
            self.centro_dto.nivel,
            self.centro_dto.cord_latitud,
            self.centro_dto.cord_longitud,
            self.centro_dto.matricula,
            self.centro_dto.planta_fisica,
            self.centro_dto.provincia,
            self.centro_dto.municipio
        )

    def centros_por_distrito(self, session: Session):
        """ Lógica de negocio para obtener centros por código de distrito """
        return self.centro_repo.centros_por_distrito(session, self.centro_dto.codigo_distrito)

    def centros_por_provincia(self, session: Session):
        """ Lógica de negocio para obtener centros por provincia """
        return self.centro_repo.centros_por_provincia(session, self.centro_dto.provincia)

    def centros_por_municipio(self, session: Session):
        """ Lógica de negocio para obtener centros por municipio """
        return self.centro_repo.centros_por_municipio(session, self.centro_dto.municipio)

    def centros_por_sector(self, session: Session):
        """ Lógica de negocio para obtener centros por sector """
        return self.centro_repo.centros_por_sector(session, self.centro_dto.sector)

    def buscar_por_parametros(self, session: Session):
        """ Lógica de negocio para buscar centros por parámetros """
        return self.centro_repo.buscar_por_parametros(
            session,
            self.centro_dto.provincia,
            self.centro_dto.municipio,
            self.centro_dto.sector
        )


class DistritoCasoDeUso:
    def __init__(self, distrito_dto: DistritoDTO = None):
        self.distrito_repo = DistritoRepositorio()
        self.distrito_dto = distrito_dto if distrito_dto else DistritoDTO()

    def mostrar_distritos(self, session: Session):
        """ Lógica de negocio para mostrar todos los distritos """
        return self.distrito_repo.mostrar_distritos(session)

    def mostrar_distritos_por_regional(self, session: Session):
        """ Lógica de negocio para mostrar distritos por código de regional """
        return self.distrito_repo.distritos_por_regional(session, self.distrito_dto.codigo_regional)

    def agregar_distrito(self, session: Session):
        """ Lógica de negocio para agregar un nuevo distrito """
        return self.distrito_repo.agregar_distrito(
            session,
            self.distrito_dto.codigo,
            self.distrito_dto.codigo_regional,
            self.distrito_dto.nombre
        )


class RegionalCasoDeUso:
    def __init__(self, regional_dto: RegionalDTO = None):
        self.regional_repo = RegionalRepositorio()
        self.regional_dto = regional_dto if regional_dto else RegionalDTO()

    def mostrar_regionales(self, session: Session):
        """ Lógica de negocio para mostrar todas las regionales """
        return self.regional_repo.mostrar_regionales(session)

    def agregar_regional(self, session: Session):
        """ Lógica de negocio para agregar una nueva regional """
        return self.regional_repo.agregar_regional(
            session,
            self.regional_dto.codigo,
            self.regional_dto.nombre
        )
