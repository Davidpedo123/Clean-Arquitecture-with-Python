# Infraestructure/Data/DBContext.py
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List


class RegionalDB(SQLModel, table=True):
    __tablename__ = 'regionales'

    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(unique=True, nullable=False)
    nombre: str

  
    distritos: List["DistritoDB"] = Relationship(back_populates="regional")
    centros: List["CentroDB"] = Relationship(back_populates="regional")


class DistritoDB(SQLModel, table=True):
    __tablename__ = 'distritos'

    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(unique=True, nullable=False)
    codigo_regional: str = Field(foreign_key="regionales.codigo", nullable=False)
    nombre: str

    
    regional: "RegionalDB" = Relationship(back_populates="distritos")
    centros: List["CentroDB"] = Relationship(back_populates="distrito")


class CentroDB(SQLModel, table=True):
    __tablename__ = 'centros'

    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str
    codigo_regional: str = Field(foreign_key="regionales.codigo", nullable=False)
    codigo_distrito: str = Field(foreign_key="distritos.codigo", nullable=False)
    nombre: str
    sector: str
    nivel: str
    cord_latitud: float
    cord_longitud: float
    matricula: str
    planta_fisica: str
    provincia: str
    municipio: str

    
    regional: "RegionalDB" = Relationship(back_populates="centros")
    distrito: "DistritoDB" = Relationship(back_populates="centros")
