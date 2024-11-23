import customtkinter as ctk
from assets import Colores
from utils.utilidades_interfaz import UtilidadesParaInterfaz
from .custom_entry import EntryPersonalizado
from .contenedor_principal import ContenedorPrincipal
from .label_titulo_subtitulo import LabelTituloSubtitulo

RUTA_IMAGEN_OCULTAR_CONTRASENA = r"assets\img\boton_contrasena\ocultar_oscuro.png"
RUTA_IMAGEN_MOSTRAR_CONTRASENA = r"assets\img\boton_contrasena\mostrar_oscuro.png"
TAMANO_BOTON_MOSTRAR_CONTRASENA = (20, 20)

class EntryContrasena(ContenedorPrincipal):
    
    def __init__(self, parent, texto="Contraseña", grid=False,row=0, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.IMAGENCTK_OCULTAR_CONTRASENA = UtilidadesParaInterfaz.cargar_imagen(
            RUTA_IMAGEN_OCULTAR_CONTRASENA, TAMANO_BOTON_MOSTRAR_CONTRASENA
        )
        self.IMAGENCTK_MOSTRAR_CONTRASENA = UtilidadesParaInterfaz.cargar_imagen(
            RUTA_IMAGEN_MOSTRAR_CONTRASENA, TAMANO_BOTON_MOSTRAR_CONTRASENA
        )

        self.label = LabelTituloSubtitulo(self, texto)

        self.frame_botones_contrasena = ContenedorPrincipal(self)
        if grid:
            self.frame_botones_contrasena.grid(row=row, column=1)
        else:
            self.label.pack(pady=5)
            self.frame_botones_contrasena.pack(pady=5)
            

        # Entry para la contraseña
        self.entry = EntryPersonalizado(self.frame_botones_contrasena)
        self.entry.configure(show="*", width=170)
        self.entry.pack(side="left", pady=5)

        # Botón para mostrar/ocultar contraseña
        self.boton_manejar_visibilidad = ctk.CTkButton(
            self.frame_botones_contrasena,
            fg_color="transparent",
            image=self.IMAGENCTK_MOSTRAR_CONTRASENA,
            hover_color=Colores.get_color_botones(),
            text="",
            width=20,
            command=self.__manejar_visibilidad_contrasena,
        )
        self.boton_manejar_visibilidad.pack(pady=5,side="left")

    def __manejar_visibilidad_contrasena(self):
        if self.entry.cget("show") == "*":
            self.entry.configure(show="")
            self.boton_manejar_visibilidad.configure(
                image=self.IMAGENCTK_OCULTAR_CONTRASENA
            )
        else:
            self.entry.configure(show="*")
            self.boton_manejar_visibilidad.configure(
                image=self.IMAGENCTK_MOSTRAR_CONTRASENA
            )

    def get(self):
        return self.entry.get()
    
    def set(self, valor):
        self.entry.insert(0, valor)
    
    def clear(self):
        self.entry.delete(0, "end")
