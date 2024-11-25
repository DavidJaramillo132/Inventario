from .custom_boton import BotonPersonalizado
from .contenedor_principal import ContenedorPrincipal


class ContenedorBotones(ContenedorPrincipal):
    def __init__(self, parent,*args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def agregar_boton(self, texto, comando, columna, **kwargs):
        BotonPersonalizado(self, texto, comando).grid(
            row=0, column=columna, padx=10,pady=5,sticky="we", **kwargs
        )
