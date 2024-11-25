
from ..baseAbstractClass import BaseAbstractClass

class Aula(BaseAbstractClass):
    def __init__(self, idAula, dimensiones, tipo):
        self.idAula = idAula
        self.dimensiones = f"{dimensiones}x{dimensiones}"
        self.tipo = tipo
        
    def get_datos(self):
        return self.idAula, self.dimensiones, self.tipo

    def update_datos(self):
        pass