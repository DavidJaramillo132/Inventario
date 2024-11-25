from database import GestorServicioSQL
from UI.gestores import GestorErrores

from models import Comentario
from enums import ComentarioNombreDatos  as CND
from components import (
    LabelTituloSubtitulo,
    ScrollableFramePersonalizado,
    ContenedorBotones,
    TablaComponente,
    TopLevelPersonalizado,
)


class TablaComentario(TablaComponente):

    @classmethod
    @GestorErrores.decorador("Error al mostrar la tabla de aulas")
    def mostrar_interfaz_tabla_comentarios(cls, root, idAula):

        frame = TopLevelPersonalizado(root)
        frame.geometry("900x500")

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        cls._crear_tabla_comentarios(frame, idAula)

    @classmethod
    def _crear_tabla_comentarios(cls, frame, idAula):
        """Crea la tabla de aulas con la información obtenida de la base de datos."""

        # Crear label de título usando WidgetCtk
        LabelTituloSubtitulo(frame, f"Comentarios del aula #{idAula}").pack(pady=10)

        # Frame para la tabla de datos usando WidgetCtk
        table_frame = ScrollableFramePersonalizado(frame)
        table_frame.pack(
            side="top", fill="both", expand=True, padx=10, pady=10, anchor="center"
        )

        # Centrar correctamente
        frame.pack_propagate(False)
        table_frame.pack_configure(anchor="center")

        # Crear encabezado de la tabla
        columns = [nombre.value for nombre in list(CND)]
        print(columns)
        cls._crear_fila_encabezado(table_frame, columns)

        # Obtener resultados de la base de datos
        resultados = GestorServicioSQL.obtener_comentarios_por_aula(idAula)
        print(resultados)
        # Construir filas de datos para la tabla
        for fila, data in enumerate(resultados, start=1):
            comentario = Comentario(*data)
            cls._crear_fila_data(
                table_frame, fila, comentario
            )

            cls._crear_botones(table_frame, frame, comentario, fila)

    @classmethod
    def _crear_botones(cls, table_frame, frame, comentario, i, ):
        from UI.controllers import ControladorTablaComentario

        contenedor_botones = ContenedorBotones(table_frame)
        contenedor_botones.grid(row=i, column=6, padx=2)

        contenedor_botones.agregar_boton(
            "Eliminar un comentario",
            lambda comentario=comentario: ControladorTablaComentario.manejar_eliminar_comentario(
                frame, comentario  
            ),
            columna=0
        )
        