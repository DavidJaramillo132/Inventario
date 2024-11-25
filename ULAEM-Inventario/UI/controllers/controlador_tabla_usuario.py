from UI.gestores import GestorNotificaciones
from database import GestorServicioSQL
from models.usuarios import UsuarioSingleton


class ControladorTablaUsuario:
    @staticmethod
    def mostrar_interfaz_tabla_usuarios(root, frame_principal):
        from UI.views.ventana_principal.tablas import TablaUsuario

        TablaUsuario.mostrar_interfaz_tabla_usuarios(root, frame_principal)

    @staticmethod
    def manejar_eliminar_usuario(root, frame_principal, usuario):
        from UI.controllers import ControladorLogin

        usuarioActual = UsuarioSingleton.get_instance()

        if usuarioActual.get_cedula() == usuario.cedula:
            if ControladorTablaUsuario._confirmar_eliminacion_cuenta_propia():
                ControladorTablaUsuario._eliminar_usuario_y_navegar(
                    usuarioActual.get_cedula(), lambda: ControladorLogin.mostrar_interfaz_login(root)
                )
        else:
            ControladorTablaUsuario._eliminar_usuario_y_navegar(
                usuario.cedula,
                lambda: ControladorTablaUsuario.mostrar_interfaz_tabla_usuarios(
                    root, frame_principal
                ),
            )

    @staticmethod
    def _confirmar_eliminacion_cuenta_propia():
        """Muestra una confirmación para la eliminación de la cuenta propia."""
        return GestorNotificaciones.mostrar_confirmacion(
            "Eliminar su cuenta",
            (
                "La cuenta que desea eliminar es la suya. ¿Está seguro que desea proseguir? "
                "Su sesión será cerrada y su cuenta eliminada."
            ),
        )

    @staticmethod
    def _eliminar_usuario_y_navegar(cedula, callback):
        """
        Elimina un usuario y ejecuta una acción adicional tras la eliminación.

        Args:
            cedula (str): Cédula del usuario a eliminar.
            callback (callable): Función a ejecutar tras la eliminación.
        """
        if GestorNotificaciones.mostrar_confirmacion("Eliminar cuenta", "¿Esta seguro que desea elimar esta cuenta?"):
            GestorServicioSQL.eliminar_usuario(cedula)  
            GestorNotificaciones.mostrar_info(
                "Cuenta eliminada exitosamente",
                "La cuenta ha sido eliminada exitosamente.",
            )
            callback()
