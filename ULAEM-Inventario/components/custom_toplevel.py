import customtkinter as ctk
from assets import Colores

class TopLevelPersonalizado(ctk.CTkToplevel):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, fg_color=Colores.get_color_principal(),*args, **kwargs)
        self.transient(root)
        self.resizable(False,False)
