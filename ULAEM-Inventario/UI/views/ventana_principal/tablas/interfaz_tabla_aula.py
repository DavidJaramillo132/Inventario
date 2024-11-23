from utils.utilidades_interfaz import UtilidadesParaInterfaz
from database import GestorServicioSQL
from UI.gestores import GestorErrores

from enums import AulaNombreDatos as AND
from components import (
    LabelTituloSubtitulo,
    ScrollableFramePersonalizado,
    BotonPersonalizado,
    TablaComponente,
)


class TablaAula(TablaComponente):

    @classmethod
    @GestorErrores.decorador("Error al mostrar la tabla de aulas")
    def mostrar_interfaz_tabla_aulas(cls, root, frame_principal):
        UtilidadesParaInterfaz.limpiar_frame_principal(frame_principal)
        cls._crear_tabla_aulas(root, frame_principal)

    @classmethod
    def _crear_tabla_aulas(cls, root, frame_principal):
        """Crea la tabla de aulas con la información obtenida de la base de datos."""

        # Crear label de título usando WidgetCtk
        LabelTituloSubtitulo(frame_principal, "Aulas").pack(pady=10)

        # Frame para la tabla de datos usando WidgetCtk
        table_frame = ScrollableFramePersonalizado(frame_principal)
        table_frame.pack(
            side="top", fill="both", expand=True, padx=10, pady=10, anchor="center"
        )

        # Centrar correctamente
        frame_principal.pack_propagate(False)
        table_frame.pack_configure(anchor="center")

        # Crear encabezado de la tabla
        columns = [AND.ID_AULA.value, AND.TIPO.value, AND.DIMENSIONES.value]
        cls._crear_fila_encabezado(table_frame, columns)

        # Obtener resultados de la base de datos
        resultados = GestorServicioSQL.obtener_aulas()

        # Construir filas de datos para la tabla
        for fila, (idAula, dimensiones, tipo) in enumerate(resultados, start=1):
            cls._crear_fila_data(
                table_frame, fila, idAula, tipo, f"{dimensiones}x{dimensiones}"
            )

            cls._crear_botones(table_frame, root, idAula, frame_principal, fila, 2)

    @classmethod
    def _crear_botones(cls, table_frame, root, idAula, frame_principal, i, columna):
        from UI.controllers import ControladorTablaAula
        from models.usuarios import UsuarioSingleton

        usuario = UsuarioSingleton.get_instance()

        if usuario.es_administrador():
            # Botón de "Agregar elemento a aula"
            BotonPersonalizado(
                table_frame,
                "Agregar elemento a aula",
                lambda idAula=idAula: ControladorTablaAula.mostrar_interfaz_agregar_elemento_aula(
                    root, idAula
                ),
            ).grid(row=i, column=columna + 1, padx=2)

            # Botón de "Eliminar Sala"
            BotonPersonalizado(
                table_frame,
                "Eliminar Sala",
                lambda idAula=idAula: ControladorTablaAula.mostrar_interfaz_eliminar_comentarios(
                    root, frame_principal, idAula
                ),
            ).grid(row=i, column=columna + 2, padx=2)

            # Botón de "Comentarios"
            BotonPersonalizado(
                table_frame,
                "Ver comentarios",
                lambda idAula=idAula: ControladorTablaAula.mostrar_interfaz_ver_comentarios(
                    root, frame_principal, idAula
                ),
            ).grid(row=i, column=columna + 3, padx=2)
            
            # Botón de "Ver Elementos"
        BotonPersonalizado(
            table_frame,
            "Ver Elementos",
            lambda idAula=idAula: ControladorTablaAula.mostrar_interfaz_ver_elementos(
                root, idAula
            ),
        ).grid(row=i, column=columna + 4, padx=2)


        # Botón de "Generar reporte"
        BotonPersonalizado(
            table_frame,
            "Generar reporte",
            lambda idAula=idAula: ControladorTablaAula.generar_reporte(idAula
            ),
        ).grid(row=i, column=columna + 6, padx=2)
        if not usuario.es_administrador():
            BotonPersonalizado(
                table_frame,
                "Agregar comentario",
                lambda idAula=idAula: ControladorTablaAula.mostrar_interfaz_agregar_comentario(
                    root, idAula
                ),
            ).grid(row=i, column=columna + 5, padx=2)
