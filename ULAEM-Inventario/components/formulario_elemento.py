from enums import EquipoNombreDatos as END, TipoEquipo,  EquipoEstados
from abc import abstractmethod

from components import (
    EntryContrasena,
    EntryLabel,
    
    ComboBoxPersonalizado,
)
from .formulario import Formulario


class FormularioCrearElementos(Formulario):
    
    @classmethod
    def _crear_campo(cls, frame, campo, index):
        if campo == END.TIPO.value:
            tipos = [tipo.value for tipo in TipoEquipo]
            return ComboBoxPersonalizado(frame, tipos)
        elif campo == END.ESTADO.value:
            estados = [estado.value for estado in EquipoEstados]
            return ComboBoxPersonalizado(frame, estados)
        else:
            return EntryLabel(frame, campo, grid=True, row=index)

    @abstractmethod
    def _crear_botones():
        pass
