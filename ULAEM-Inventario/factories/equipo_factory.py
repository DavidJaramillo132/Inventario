from models.equipos.equipo_electronico import EquipoElectronico
from models.equipos.equipo_mueble import EquipoMueble
from enums import TipoEquipo

# Fábrica de elementos
class ElementoFactory:

    @staticmethod
    def crear_elemento(tipo:TipoEquipo,datos:dict):
        
        if tipo == TipoEquipo.ELECTRONICO:
            return EquipoElectronico.diccionario_a_instancia(datos)
        elif tipo == TipoEquipo.MUEBLE:
            return EquipoMueble.diccionario_a_instancia(datos)
        else:
            raise ValueError(f"Tipo de elemento desconocido: {tipo}")
