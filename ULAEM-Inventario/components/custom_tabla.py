from abc import ABC, abstractmethod
from components import LabelTextoNormal, BotonPersonalizado

class TablaComponente(ABC):

    @classmethod
    def _crear_fila_encabezado(cls, frame, columns):
        for index, name_column in enumerate(columns):
            label = LabelTextoNormal(frame, name_column)
            label.grid(row=0, column=index, padx=5, pady=5)

    @classmethod
    def _crear_fila_data(cls, frame, fila, objeto):
        data = objeto.get_datos()
        for col, item in enumerate(data):
            label = LabelTextoNormal(frame, item)
            label.grid(row=fila, column=col, padx=5, pady=5)

    @abstractmethod
    def _crear_botones():
        pass