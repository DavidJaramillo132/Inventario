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

    def get_datos(self):
        return (
            self.idElemento,
            self.nombre,
            self.tipo,
            self.estado,
            self.fecha_adquisicion,
            self.cantidad,
            self.idAula,
        )

    def update_datos(
        self, idElemento, nombre, tipo, estado, fecha_adquisicion, cantidad, idAula
    ):
        pass
