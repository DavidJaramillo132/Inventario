from utils.validador import Validador
from database import GestorServicioSQL
from UI.gestores import GestorErrores, GestorNotificaciones


class ControladorAgregarElemento:
    @staticmethod
    @GestorErrores.decorador("Error al mostrar la interfaz de agregar elemento")
    def mostrar_interfaz_agregar_elemento(frame_principal, idAula):
        from UI.views.ventana_principal import InterfazAgregarElemento

        InterfazAgregarElemento.mostrar_interfaz_agregar_elemento_aula(
            frame_principal, idAula
        )

    @staticmethod
    @GestorErrores.decorador("Error al agregar el elemento")
    def manejar_agregar_elemento_aula(
        frame, nombre, tipo, estado, fecha_adquisision, cantidad, idAula
    ):
        Validador.validar_todos_campos_elementos(
            nombre, tipo, estado, fecha_adquisision, cantidad, idAula
        )

        GestorServicioSQL.agregar_elemento_a_aula(
            nombre, tipo, estado, fecha_adquisision, cantidad, idAula
        )
        GestorNotificaciones.mostrar_info(
            "Elemento agregado", "El elemento ha sido agregado correctamente"
        )

        frame.destroy()
