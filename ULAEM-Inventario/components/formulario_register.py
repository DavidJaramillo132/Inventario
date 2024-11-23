from enums import PrivilegiosUsuario, OcupacionesUsuario,UsuarioNombreDatos as UND
from abc import abstractmethod

from components import (
    EntryContrasena,
    EntryLabel,
    
    ComboBoxPersonalizado,
)
from .formulario import Formulario


class FormularioRegister(Formulario):
    @classmethod
    def _crear_campo(cls, frame, campo, index):
        if campo == UND.CONTRASENA.value or campo == UND.CONFIRMAR_CONTRASENA.value:
            return EntryContrasena(frame, campo, grid=True, row=index)
        elif campo == UND.OCUPACION.value:
            ocupaciones = [ocupacion.value for ocupacion in OcupacionesUsuario]
            return ComboBoxPersonalizado(frame, ocupaciones)
        elif campo == UND.PRIVILEGIOS.value:
            privilegios = [privilegio.value for privilegio in PrivilegiosUsuario]
            return ComboBoxPersonalizado(frame, privilegios)
        else:
            return EntryLabel(frame, campo, grid=True, row=index)

    @abstractmethod
    def _crear_botones():
        pass
