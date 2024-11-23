import customtkinter as ctk
from assets import FuentesTexto

class LabelTextoNormal(ctk.CTkLabel):
    def __init__(self, frame, contenido, *args, **kwargs):
        super().__init__(
            frame, text=contenido, font=FuentesTexto.get_fuente_texto(), *args, **kwargs
        )
