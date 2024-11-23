import customtkinter as ctk
from assets import FuentesTexto, Colores


class TextBoxPersonalizado(ctk.CTkTextbox):
    def __init__(self, master, *args, **kwargs):
        super().__init__(
            master,
            font=FuentesTexto.get_fuente_texto(),
            height=200,
            width=500,
            *args,
            **kwargs
        )