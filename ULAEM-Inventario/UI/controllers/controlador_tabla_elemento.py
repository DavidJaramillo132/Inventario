from UI.gestores import GestorNotificaciones
from database import GestorServicioSQL



class ControladorTablaElemento:
    @staticmethod
    def mostrar_interfaz_tabla_elementos(root,idAula):
        from UI.views.ventana_principal import TablaElemento

        TablaElemento.mostrar_interfaz_tabla_elementos(root, idAula)

    @staticmethod
    def manejar_eliminar_elemento(frame, elemento):

        if GestorNotificaciones.mostrar_confirmacion("Eliminar elemento", "¿Está seguro que desea eliminar este elemento?"):

            GestorServicioSQL.eliminar_elemento_de_aula(elemento.idElemento)
            GestorNotificaciones.mostrar_info("Elemento eliminado", "El elemento ha sido eliminado con éxito")
        frame.destroy()

    @staticmethod
    def mostrar_interfaz_editar_elemento(root,frame_tabla_elemento,elemento):
        from UI.controllers import ControladorEditarElemento
        
        ControladorEditarElemento.mostrar_interfaz_editar_elemento(root,frame_tabla_elemento,elemento)
