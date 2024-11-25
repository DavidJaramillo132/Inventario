from abc import ABC, abstractmethod
from components import LabelTituloSubtitulo


class Formulario(ABC):

    @classmethod
    def _crear_campo(cls, frame, campo, index):
        pass

    @classmethod
    def _crear_campos(cls, frame, campos):
        """
        Crea los componentes de los campos en el formulario usando los valores del Enum.
        """
        componentes = {}
        for index, campo in enumerate(campos, start=1):
            LabelTituloSubtitulo(frame, campo).grid(
                row=index, column=0, padx=10, pady=10, sticky="w"
            )
            componentes[campo] = cls._crear_campo(frame, campo, index)
            componentes[campo].grid(row=index, column=1, padx=10, pady=10)
        return componentes

    @abstractmethod
    def _crear_botones():
        pass
