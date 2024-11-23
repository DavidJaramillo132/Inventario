from UI.gestores import GestorErrores, GestorAutentificacion, GestorNotificaciones
from utils.validador import Validador
from models.usuarios import UsuarioSingleton


class ControladorEditarPerfil:

    @staticmethod
    @GestorErrores.decorador("Error al mostrar la interfaz de editar perfil")
    def mostrar_interfaz_editar_perfil(frame_editar_perfil):
        from UI.views.inicio_sesion import InterfazEditarPerfil

        InterfazEditarPerfil.mostrar_editar_perfil(frame_editar_perfil)

    @staticmethod
    def poblar_campos(componentes):
        """
        Pobla los campos con los datos de un usuario existente.
        """
        datos_usuario = UsuarioSingleton.get_instance().get_datos_usuario()
        print(datos_usuario)

        for campo, componente in componentes.items():
            valor = datos_usuario.get(campo, "")
            if hasattr(componente, "set"):
                componente.set(valor)
            else:
                print(f"El componente para {campo} no tiene un método 'set'")

    @staticmethod
    @GestorErrores.decorador("Error al actualizar el perfil")
    def manejar_actualizar_perfil(
        frame_editar_perfil, cedula, nombre, email, contrasena, ocupacion, privilegios
    ):
        Validador.validar_todos_campos_cuenta(
            cedula, nombre, email, contrasena, ocupacion, privilegios
        )
        print(cedula, nombre, email, contrasena, ocupacion, privilegios)

        if GestorAutentificacion.actualizar_usuario(
            cedula, nombre, email, contrasena, ocupacion, privilegios
        ):
            usuario = UsuarioSingleton.get_instance()
            usuario.update_usuario(
                cedula, nombre, email, contrasena, ocupacion, privilegios
            )
            GestorNotificaciones.mostrar_info(
                "Perfil actualizado", "Perfil actualizado con éxito"
            )
            ControladorEditarPerfil.mostrar_interfaz_editar_perfil(frame_editar_perfil)
