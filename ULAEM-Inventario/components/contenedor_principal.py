import customtkinter as ctk
from assets import Colores

class ContenedorPrincipal(ctk.CTkFrame):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, fg_color=Colores.get_color_principal(), *args, **kwargs)
