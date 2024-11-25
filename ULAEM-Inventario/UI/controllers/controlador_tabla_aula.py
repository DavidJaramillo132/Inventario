from UI.gestores import GestorErrores, GestorNotificaciones, GestorReportes


class ControladorTablaAula:
    @staticmethod
    def mostrar_interfaz_tabla_aulas(root, frame_principal):
        from UI.views.ventana_principal.tablas import TablaAula

        TablaAula.mostrar_interfaz_tabla_aulas(root, frame_principal)

    @staticmethod
    def mostrar_interfaz_agregar_elemento_aula(root, aula):
        from UI.controllers import ControladorAgregarElemento

        ControladorAgregarElemento.mostrar_interfaz_agregar_elemento(root, aula.idAula)

    @staticmethod
    def manejar_eliminar_aula(root, frame_principal, aula):
        from database import GestorServicioSQL
        from UI.controllers import ControladorTablaAula

        if GestorNotificaciones.mostrar_confirmacion(
            "Eliminar aula", "¿Está seguro que desea eliminar esta aula?"
        ):
            GestorServicioSQL.eliminar_aula(aula.idAula)
            GestorNotificaciones.mostrar_info(
                "Aula eliminada", "El aula ha sido eliminada con éxito"
            )
            ControladorTablaAula.mostrar_interfaz_tabla_aulas(root, frame_principal)

    @staticmethod
    def mostrar_interfaz_ver_comentarios(root, aula):
        from UI.controllers import ControladorTablaComentario

        ControladorTablaComentario.mostrar_interfaz_tabla_comentarios(root, aula.idAula)

    @staticmethod
    def mostrar_interfaz_ver_elementos(root, aula):
        from UI.controllers import ControladorTablaElemento

        ControladorTablaElemento.mostrar_interfaz_tabla_elementos(root, aula.idAula)

    @staticmethod
    def mostrar_interfaz_agregar_comentario(root, aula):
        from UI.controllers import ControladorAgregarComentario

        ControladorAgregarComentario.mostrar_interfaz_agregar_comentario(
            root, aula.idAula
        )

    @staticmethod
    @GestorErrores.decorador("Error al generar el reporte")
    def generar_reporte(aula):

        GestorReportes.generar_reporte_aula(aula.idAula)

