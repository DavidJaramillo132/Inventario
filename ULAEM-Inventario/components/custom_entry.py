import customtkinter as ctk
from assets import Colores, FuentesTexto

class EntryPersonalizado(ctk.CTkEntry):
    def __init__(self, frame, *args, **kwargs):
        super().__init__(
            frame,
            placeholder_text="",
            height=50,
            width=200,
            font=FuentesTexto.get_fuente_texto(),
            fg_color=Colores.get_color_principal(),
            border_width=10,
            border_color=Colores.get_border_color(),
            *args,
            **kwargs
        )