


class Regional:
    def __init__(self, id: int, codigo: str, nombre: str):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre


class Distrito:
    def __init__(self, id: int, codigo: str, codigo_regional: str, nombre: str):
        self.id = id
        self.codigo = codigo
        self.codigo_regional = codigo_regional
        self.nombre = nombre

    
class Centro:
    def __init__(
        self,
        id: int,
        codigo: str,
        codigo_regional: str,
        codigo_distrito: str,
        nombre: str,
        sector: str,
        nivel: str,
        cord_latitud: int,
        cord_longitud: int,
        matricula: str,
        planta_fisica: str,
        provincia: str,
        municipio: str
    ):
        self.id = id
        self.codigo = codigo
        self.codigo_regional = codigo_regional
        self.codigo_distrito = codigo_distrito
        self.nombre = nombre
        self.sector = sector
        self.nivel = nivel
        self.cord_latitud = cord_latitud
        self.cord_longitud = cord_longitud
        self.matricula = matricula
        self.planta_fisica = planta_fisica
        self.provincia = provincia
        self.municipio = municipio

    
    
    