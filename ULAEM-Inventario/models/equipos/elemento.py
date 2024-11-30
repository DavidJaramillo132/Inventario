from ..baseAbstractClass import BaseAbstractClass


# Clase base abstracta Elemento
class Equipo(BaseAbstractClass):
    def __init__(
        self, idElemento, nombre, tipo, estado, fecha_adquisicion, cantidad, idAula
    ):
        self.idElemento = idElemento
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado
        self.fecha_adquisicion = fecha_adquisicion
        self.cantidad = cantidad
        self.idAula = idAula

    def get_datos(self, formato="tuple"):
        if formato == "dict":
            return {
                "idElemento": self.idElemento,
                "nombre": self.nombre,
                "tipo": self.tipo,
                "estado": self.estado,
                "fecha_adquisicion": self.fecha_adquisicion,
                "cantidad": self.cantidad,
                "idAula": self.idAula,
            }

        return (
            self.idElemento,
            self.nombre,
            self.tipo,
            self.estado,
            self.fecha_adquisicion,
            self.cantidad,
            self.idAula,
        )

    def get_tipo(self):
        return self.tipo

    def update_datos(
        self, idElemento, nombre, tipo, estado, fecha_adquisicion, cantidad
    ):
        pass

    def get_idElemento(self):
        return self.idElemento

    def get_idAula(self):
        return self.idAula
