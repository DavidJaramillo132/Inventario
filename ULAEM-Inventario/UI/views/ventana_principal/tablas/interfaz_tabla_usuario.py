from abc import ABC
from utils.utilidades_interfaz import UtilidadesParaInterfaz

from database import GestorServicioSQL
from enums import UsuarioNombreDatos as UND
from UI.controllers import ControladorTablaUsuario


from components import (

    LabelTituloSubtitulo,
    BotonPersonalizado,
    LabelTextoNormal,
    ScrollableFramePersonalizado,
    TablaComponente
)


class TablaUsuario(TablaComponente):

    @classmethod
    def mostrar_interfaz_tabla_usuarios(cls, root, frame_principal):
        UtilidadesParaInterfaz.limpiar_frame_principal(frame_principal)

        cls._crear_tabla_usuarios(root,frame_principal)

    @classmethod
    def _crear_tabla_usuarios(cls, root,frame_principal):

        # Crear label de título usando WidgetCtk
        LabelTituloSubtitulo(frame_principal, "Usuarios").pack(pady=10)

        # Frame para la tabla de datos usando WidgetCtk
        table_frame = ScrollableFramePersonalizado(frame_principal)
        table_frame.pack(
            side="top", fill="both", expand=True, padx=10, pady=10, anchor="center"
        )

        # Centrar correctamente
        frame_principal.pack_propagate(False)
        table_frame.pack_configure(anchor="center")

        # Encabezados de columna
        columns = [
            UND.CEDULA.value,
            UND.NOMBRE.value,
            UND.EMAIL.value,
            UND.CONTRASENA.value,
            UND.OCUPACION.value,
            UND.PRIVILEGIOS.value,
        ]
        cls._crear_fila_encabezado(table_frame,columns)

        resultados = GestorServicioSQL.obtener_usuarios()

        # Mostrar datos en la tabla
        for i, (cedula, nombre, email, contrasena, ocupacion, privilegios) in enumerate(
            resultados, start=1
        ):
            cls._crear_fila_data(table_frame,i,cedula, nombre, email, contrasena, ocupacion, privilegios)
            cls._crear_botones(table_frame,cedula,root,frame_principal,i)
            
    @classmethod
    def _crear_botones(cls, table_frame, cedula,root,frame_principal,fila):
            btn_eliminar_usuario = BotonPersonalizado(
                table_frame,
                "Eliminar",
                lambda cedula=cedula: ControladorTablaUsuario.manejar_eliminar_usuario(root,frame_principal,cedula),
            )
            btn_eliminar_usuario.grid(row=fila, column=6, padx=2)