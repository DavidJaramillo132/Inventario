from database import GestorServicioSQL
from UI.gestores import GestorErrores
from enums import EquipoNombreDatos as END
from factories import EquipoFactory
from components import (
    LabelTituloSubtitulo,
    ScrollableFramePersonalizado,
    BotonPersonalizado,
    TablaComponente,
    TopLevelPersonalizado,
)


class TablaElemento(TablaComponente):

    @classmethod
    @GestorErrores.decorador("Error al mostrar la tabla de aulas")
    def mostrar_interfaz_tabla_elementos(cls, root, idAula):

        frame_tabla_elemento = TopLevelPersonalizado(root)
        frame_tabla_elemento.geometry("1400x500")

        frame_tabla_elemento.grid_columnconfigure(0, weight=1)
        frame_tabla_elemento.grid_rowconfigure(0, weight=1)

        cls._crear_tabla_elementos(root,frame_tabla_elemento, idAula)

    @classmethod
    def _crear_tabla_elementos(cls,root,frame_tabla_elemento, idAula):
        """Crea la tabla de aulas con la información obtenida de la base de datos."""

        # Crear label de título usando WidgetCtk
        LabelTituloSubtitulo(frame_tabla_elemento, f"Elementos del aula #{idAula}").pack(pady=10)

        # Frame para la tabla de datos usando WidgetCtk
        table_frame = ScrollableFramePersonalizado(frame_tabla_elemento)
        table_frame.pack(
            side="top", fill="both", expand=True, padx=10, pady=10, anchor="center"
        )

        # Centrar correctamente
        frame_tabla_elemento.pack_propagate(False)
        table_frame.pack_configure(anchor="center")

        # Crear encabezado de la tabla
        columns = [nombre.value for nombre in list(END)]
        cls._crear_fila_encabezado(table_frame, columns)

        # Obtener resultados de la base de datos
        resultados = GestorServicioSQL.obtener_elementos_por_idaula(idAula)
        # Construir filas de datos para la tabla
        for fila, data in enumerate(resultados, start=1):
            elemento = EquipoFactory.crear_objeto(*data)
            cls._crear_fila_data(table_frame, fila, elemento)

            cls._crear_botones(root, table_frame, frame_tabla_elemento, elemento, fila, len(data))

    @classmethod
    def _crear_botones(cls,root,table_frame,frame_tabla_elemento,elemento,fila,columna):
        from UI.controllers import ControladorTablaElemento
        from models.usuarios import UsuarioSingleton

        usuario = UsuarioSingleton.get_instance()

        if usuario.es_administrador():
       
            BotonPersonalizado(
                table_frame,
                "Eliminar elemento",
                lambda elemento=elemento: ControladorTablaElemento.manejar_eliminar_elemento(frame_tabla_elemento, elemento),).grid(row=fila, column=columna,padx=2)
            BotonPersonalizado(
                table_frame,"Modificar elemento",lambda elemento=elemento: ControladorTablaElemento.mostrar_interfaz_editar_elemento(root, frame_tabla_elemento, elemento)
            ).grid(row=fila,column= columna+1,padx=2)
