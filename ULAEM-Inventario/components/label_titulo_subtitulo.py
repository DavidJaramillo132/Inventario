import customtkinter as ctk
from assets import FuentesTexto

class LabelTituloSubtitulo(ctk.CTkLabel):
    def __init__(self, frame, texto, imgCTK=None, *args, **kwargs):
        super().__init__(
            frame,
            text=texto,
            font=FuentesTexto.get_fuente_titulo_subtitulo(),
            image=imgCTK,
            compound=ctk.BOTTOM,
            *args,
            **kwargs
        )
