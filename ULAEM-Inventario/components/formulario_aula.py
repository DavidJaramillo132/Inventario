from enums import AulaNombreDatos as AND, TipoAula
from abc import abstractmethod

from components import (
    EntryLabel,
    ComboBoxPersonalizado,
)
from .formulario import Formulario


class FormularioCrearAulas(Formulario):
    @classmethod
    def _crear_campo(cls, frame, campo, index):
        if campo == AND.TIPO.value:
            tipos = [tipo.value for tipo in TipoAula]
            return ComboBoxPersonalizado(frame, tipos)
        else:
            return EntryLabel(frame, campo, grid=True, row=index)

    @abstractmethod
    def _crear_botones():
        pass
