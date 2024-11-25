from UI.gestores import GestorErrores, GestorAutentificacion, GestorNotificaciones
from utils.validador import Validador
from models.usuarios import UsuarioSingleton


class ControladorEditarPerfil:

    @staticmethod
    @GestorErrores.decorador("Error al mostrar la interfaz de editar perfil")
    def mostrar_interfaz_editar_perfil(frame_editar_perfil):
        from UI.views.ventana_principal import InterfazEditarPerfil

        InterfazEditarPerfil.mostrar_editar_perfil(frame_editar_perfil)

    @staticmethod
    def poblar_campos(campos, componentes):
        """
        Pobla los campos con los datos de un usuario existente.
        """
        usuario = UsuarioSingleton.get_instance()
        datos_usuario = usuario.get_datos()

        for campo, valor in zip(campos, datos_usuario):
            componente = componentes.get(campo.value)
            if componente and hasattr(componente, "set"):
                componente.set(valor)
            else:
                print(
                    f"El componente para {campo} no tiene un método 'set' o no existe"
                )

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
            usuario.update_datos(
                cedula, nombre, email, contrasena, ocupacion, privilegios
            )
            GestorNotificaciones.mostrar_info(
                "Perfil actualizado", "Perfil actualizado con éxito"
            )
            ControladorEditarPerfil.mostrar_interfaz_editar_perfil(frame_editar_perfil)
