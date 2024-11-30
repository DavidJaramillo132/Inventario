from .elemento import Equipo

class EquipoDecorativo(Equipo):
    def __init__(
        self, idElemento, nombre, tipo, estado, fecha_adquisicion, cantidad, idAula
    ):
        super().__init__(idElemento, nombre,tipo,estado, fecha_adquisicion, cantidad, idAula)


    
