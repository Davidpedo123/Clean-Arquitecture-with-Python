from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import Request, Response
from fastapi import Depends
from sqlmodel import Session
from Infraestructure.Repositorio.engine import get_session
from Application.Servicios.ServiciosCentrosGenerales import ServicioCentro, ServicioDistrito, ServicioRegional
from Application.DTOs.DTOCentros import CentroDTO, RegionalDTO, DistritoDTO


router = APIRouter()

@router.get("/centros", tags=["Centros"])
async def mostrar_centros(request: Request, response: Response, session: Session = Depends(get_session)):
    """ Endpoint para mostrar todos los centros """
    servicio_centro = ServicioCentro()
    centros = servicio_centro.mostrar_centros(session)
    return JSONResponse(content=[centro.dict() for centro in centros], status_code=200)


@router.post("/centros", tags=["Centros"])
async def agregar_centro(request: Request, response: Response, session: Session = Depends(get_session)):
    """ Endpoint para agregar un nuevo centro """
    data = await request.json()
    centro_dto = CentroDTO(**data)
    servicio_centro = ServicioCentro()
    nuevo_centro = servicio_centro.agregar_centro(session, centro_dto)
    return JSONResponse(content=nuevo_centro.dict(), status_code=201)

@router.get("/centros/distrito/{codigo_distrito}", tags=["Centros"])
async def centros_por_distrito(request: Request, response: Response, codigo_distrito: str, session: Session = Depends(get_session)):
    """ Endpoint para obtener centros por código de distrito """
    servicio_centro = ServicioCentro()
    centros = servicio_centro.centros_por_distrito(session, codigo_distrito)
    return JSONResponse(content=[centro.dict() for centro in centros], status_code=200)

@router.get("/centros/provincia/{provincia}", tags=["Centros"])
async def centros_por_provincia(request: Request, response: Response, provincia: str, session: Session = Depends(get_session)):
    """ Endpoint para obtener centros por provincia """
    servicio_centro = ServicioCentro()
    centros = servicio_centro.centros_por_provincia(session, provincia)
    return JSONResponse(content=[centro.dict() for centro in centros], status_code=200)

@router.get("/centros/municipio/{municipio}", tags=["Centros"])
async def centros_por_municipio(request: Request, response: Response, municipio: str, session: Session = Depends(get_session)):
    """ Endpoint para obtener centros por municipio """
    servicio_centro = ServicioCentro()
    centros = servicio_centro.centros_por_municipio(session, municipio)
    return JSONResponse(content=[centro.dict() for centro in centros], status_code=200)


@router.get("/centros/sector/{sector}", tags=["Centros"])
async def centros_por_sector(request: Request, response: Response, sector: str, session: Session = Depends(get_session)):
    """ Endpoint para obtener centros por sector """
    servicio_centro = ServicioCentro()
    centros = servicio_centro.centros_por_sector(session, sector)
    return JSONResponse(content=[centro.dict() for centro in centros], status_code=200) 

@router.get("/centros/buscar", tags=["Centros"])
async def buscar_centros(request: Request, response: Response, provincia: str = None, municipio: str = None, sector: str = None, session: Session = Depends(get_session)):
    """ Endpoint para buscar centros por parámetros """
    servicio_centro = ServicioCentro()
    centros = servicio_centro.buscar_por_parametros(session, provincia, municipio, sector)
    return JSONResponse(content=[centro.dict() for centro in centros], status_code=200)

@router.get("/distritos", tags=["Distritos"])
async def mostrar_distritos(request: Request, response: Response, session: Session = Depends(get_session)):
    """ Endpoint para mostrar todos los distritos """
    servicio_distrito = ServicioDistrito()
    distritos = servicio_distrito.mostrar_distritos(session)
    return JSONResponse(content=[distrito.dict() for distrito in distritos], status_code=200)

@router.post("/distritos", tags=["Distritos"])
async def agregar_distrito(request: Request, response: Response, session: Session = Depends(get_session)):
    """ Endpoint para agregar un nuevo distrito """
    data = await request.json()
    distrito_dto = DistritoDTO(**data)
    servicio_distrito = ServicioDistrito()
    nuevo_distrito = servicio_distrito.agregar_distrito(session, distrito_dto)
    return JSONResponse(content=nuevo_distrito.dict(), status_code=201)

@router.get("/distritos/regional/{codigo_regional}", tags=["Distritos"])
async def distritos_por_regional(request: Request, response: Response, codigo_regional: str, session: Session = Depends(get_session)):
    """ Endpoint para obtener distritos por código de regional """
    servicio_distrito = ServicioDistrito()
    distritos = servicio_distrito.obtener_distritos_por_regional(session, codigo_regional)
    return JSONResponse(content=[distrito.dict() for distrito in distritos], status_code=200)

@router.get("/regionales", tags=["Regionales"])
async def mostrar_regionales(request: Request, response: Response, session: Session = Depends(get_session)):
    """ Endpoint para mostrar todas las regionales """
    servicio_regional = ServicioRegional()
    regionales = servicio_regional.obtener_regionales(session)
    return JSONResponse(content=[regional.dict() for regional in regionales], status_code=200)

@router.post("/regionales", tags=["Regionales"])
async def agregar_regional(request: Request, response: Response, session: Session = Depends(get_session)):
    """ Endpoint para agregar una nueva regional """
    data = await request.json()
    regional_dto = RegionalDTO(**data)
    servicio_regional = ServicioRegional()
    nueva_regional = servicio_regional.agregar_regional(session, regional_dto)
    return JSONResponse(content=nueva_regional.dict(), status_code=201)

