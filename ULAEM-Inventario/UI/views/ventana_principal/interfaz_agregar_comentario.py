from components import (
    TopLevelPersonalizado,
    TextBoxPersonalizado,
    LabelTituloSubtitulo,
    ContenedorBotones,
)
from UI.gestores import GestorErrores
from enums import ComentarioNombreDatos as CND


class InterfazAgregarComentario:

    @classmethod
    @GestorErrores.decorador("Error al mostrar la interfaz de crear comentario")
    def mostrar_interfaz_agregar_comentario(cls, root, idAula):

        frame = TopLevelPersonalizado(root)
        frame.geometry("500x500")

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        cls._crear_interfaz_agregar_comentario(frame, idAula)

    @classmethod
    def _crear_interfaz_agregar_comentario(cls, frame, idAula):
        LabelTituloSubtitulo(
            frame,
            "Agregar un comentario",
        ).pack(padx=10,pady=10,anchor="center")
        
        componentes = {}
        componentes[CND.CONTENIDO.value] = TextBoxPersonalizado(frame)
        componentes[CND.CONTENIDO.value].pack(padx=10,pady=10,anchor="center")
        
        

        # Crear botones
        cls._crear_botones(frame, componentes, idAula)

    @classmethod
    def _crear_botones(cls, frame, componentes, idAula):
        from UI.controllers import ControladorAgregarComentario

        frame_botones = ContenedorBotones(frame)
        frame_botones.pack(padx=10,pady=10,anchor="center")

        frame_botones.agregar_boton(
            "Agrega un comentario",
            lambda: ControladorAgregarComentario.manejar_agregar_comentario(
                frame,
                componentes[CND.CONTENIDO.value].get(1.0,"end"),
                idAula,
            ),
            columna=0,
            columnspan=2,
        )
