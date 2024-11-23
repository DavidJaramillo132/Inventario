from UI.gestores import GestorNotificaciones
from database import GestorServicioSQL
from models.usuarios import UsuarioSingleton


class ControladorTablaElemento:
    @staticmethod
    def mostrar_interfaz_tabla_usuarios(root,idAula):
        from UI.views.ventana_principal import TablaElemento

        TablaElemento.mostrar_interfaz_tabla_elementos(root, idAula)

    @staticmethod
    def manejar_eliminar_elemento(frame, idElemento):

        if GestorNotificaciones.mostrar_confirmacion("Eliminar elemento", "¿Está seguro que desea eliminar este elemento?"):

            GestorServicioSQL.eliminar_elemento_de_aula(idElemento)
            GestorNotificaciones.mostrar_info("Elemento eliminado", "El elemento ha sido eliminado con éxito")
        frame.destroy()
