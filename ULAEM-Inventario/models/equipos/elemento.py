from abc import ABC, abstractmethod
from datetime import datetime


# Clase base abstracta Elemento
class Elemento(ABC):
    def __init__(self, idElemento, nombre, estado, fecha_adquisicion, cantidad):
        self.idElemento = idElemento
        self.nombre = nombre
        self.estado = estado
        self.fecha_adquisicion = fecha_adquisicion
        self.cantidad = cantidad

    @classmethod
    def diccionario_a_instancia(cls, datos):
        idElemento = datos["idElemento"]
        nombre = datos["nombre"]
        estado = datos["estado"]
        fecha_adquisicion = cls._convertir_fecha(datos["fecha_adquisicion"])
        cantidad = datos["cantidad"]

        return cls(idElemento,nombre, estado, fecha_adquisicion, cantidad)

    @staticmethod
    def _convertir_fecha(fecha_str):

        try:
            return datetime.strptime(fecha_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError(
                f"Formato de fecha inválido: {fecha_str}. Debe ser 'YYYY-MM-DD'."
            )

    @abstractmethod
    def getDescripcion(self):
        pass

    @abstractmethod
    def getCategoria(self):
        pass
