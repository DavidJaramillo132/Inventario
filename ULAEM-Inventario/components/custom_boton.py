import customtkinter as ctk
from assets import Colores,FuentesTexto

class BotonPersonalizado(ctk.CTkButton):
    def __init__(self, frame, texto, comando, *args, **kwargs):
        super().__init__(
            frame,
            text=texto,
            command=comando,
            font=FuentesTexto.get_fuente_texto(),
            fg_color=Colores.get_color_principal(),
            hover_color=Colores.get_color_botones(),
            *args,
            **kwargs
        )