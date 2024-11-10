from abc import ABC, abstractmethod
from datetime import datetime

# Clase base abstracta Elemento
class Elemento(ABC):
    def __init__(self, nombre, estado, fecha_adquisicion, cantidad, idElemento):
        self.nombre = nombre
        self.estado = estado
        self.fecha_adquisicion = fecha_adquisicion
        self.cantidad = cantidad
        self.idElemento = idElemento

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def categoria(self):
        pass

# Subclase para elementos de tipo equipo electrónico
class EquipoElectronico(Elemento):
    def descripcion(self):
        return f"Equipo electrónico: {self.nombre}, Estado: {self.estado}, Adquirido en: {self.fecha_adquisicion}, Cantidad: {self.cantidad}"

    def categoria(self):
        return "Electrodomestico"  # Implementación específica para el tipo

# Subclase para elementos de tipo mobiliario
class EquipoMuebles(Elemento):
    def descripcion(self):
        return f"Mobiliario: {self.nombre}, Estado: {self.estado}, Adquirido en: {self.fecha_adquisicion}, Cantidad: {self.cantidad}"

    def categoria(self):
        return "Mueble"  # Implementación específica para el tipo

# Fábrica de elementos
class ElementoFactory:
    
    @staticmethod
    def crear_elemento(tipo, nombre, estado, fecha_adquisicion, cantidad, idElemento):
        if tipo == "Electrodomestico":
            return EquipoElectronico(nombre, estado, fecha_adquisicion, cantidad, idElemento)
        elif tipo == "Mueble":
            return EquipoMuebles(nombre, estado, fecha_adquisicion, cantidad, idElemento)
        else:
            raise ValueError(f"Tipo de elemento desconocido: {tipo}")
