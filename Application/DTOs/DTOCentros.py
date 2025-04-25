from pydantic import BaseModel, Field
from typing import Optional



class RegionalDTO(BaseModel):
    

    id: Optional[int] = None
    codigo: Optional[str] = Field(None, max_length=2)
    nombre: Optional[str] = Field(None, max_length=70)


class DistritoDTO(BaseModel):
    

    id: int = Field(...)
    codigo: str = Field(..., max_length=4)
    codigo_regional: str = Field(..., max_length=2)
    nombre: str = Field(..., max_length=70)


class CentroDTO(BaseModel):
    

    id: int = Field(...)
    codigo: str = Field(..., max_length=7)
    codigo_regional: str = Field(..., max_length=2)
    codigo_distrito: str = Field(..., max_length=4)
    nombre: str = Field(..., max_length=70)
    sector: str = Field(..., max_length=70)
    nivel: str = Field(..., max_length=30)
    cord_latitud: float = Field(...)
    cord_longitud: float = Field(...)
    matricula: str = Field(...)
    planta_fisica: str = Field(...)
    provincia: str = Field(..., max_length=70)
    municipio: str = Field(..., max_length=70)
