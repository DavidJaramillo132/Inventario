import customtkinter as ctk
from assets import Colores,FuentesTexto

class ComboBoxPersonalizado(ctk.CTkComboBox):
    def __init__(self, frame, valores, *args, **kwargs):
        super().__init__(
            frame,
            values=valores,
            height=50,
            width=200,
            font=FuentesTexto.get_fuente_texto(),
            fg_color=Colores.get_color_principal(),
            border_width=10,
            border_color=Colores.get_border_color(),
            *args,
            **kwargs
        )
    

    
