from .elemento import Equipo

class EquipoEscritorio(Equipo):
    def __init__(
        self, idElemento, nombre, tipo, estado, fecha_adquisicion, cantidad, idAula
    ):
        super().__init__(idElemento, nombre, tipo, estado, fecha_adquisicion, cantidad, idAula)


    