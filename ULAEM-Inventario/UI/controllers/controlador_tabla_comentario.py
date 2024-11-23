from UI.gestores import GestorNotificaciones
from database import GestorServicioSQL


class ControladorTablaComentario:
    @staticmethod
    def mostrar_interfaz_tabla_comentarios(root,idAula):
        from UI.views.ventana_principal import TablaComentario

        TablaComentario.mostrar_interfaz_tabla_comentarios(root, idAula)

    @staticmethod
    def manejar_eliminar_comentario(frame, idComentario):

        if GestorNotificaciones.mostrar_confirmacion("Eliminar comentario", "¿Está seguro que desea eliminar este comentario?"):

            GestorServicioSQL.eliminar_comentario(idComentario)
            GestorNotificaciones.mostrar_info("Comentario eliminado", "El comentario ha sido eliminado con éxito")
        frame.destroy()
