from UI.gestores import GestorErrores, GestorAutentificacion, GestorNotificaciones
from UI.views.inicio_sesion import InterfazLogin
from utils.validador import Validador
from models.usuarios import UsuarioSingleton


class ControladorRegister:
    @staticmethod
    @GestorErrores.decorador("Error al crear la cuenta")
    def manejar_crear_cuenta(
        root,
        cedula,
        nombre,
        email,
        contrasena,
        confirmar_contrasena,
        ocupacion,
        privilegios,
    ):
        Validador.validar_todos_campos_cuenta(
            cedula, nombre, email, contrasena, ocupacion, privilegios
        )

        if contrasena != confirmar_contrasena:
            raise Exception("Las contraseñas no coinciden")

        if GestorAutentificacion.registrar_usuario(  # tengo duda con esto
            cedula, nombre, email, contrasena, ocupacion, privilegios
        ):
            GestorNotificaciones.mostrar_info(
                "Cuenta creada exitosamente", "Usuario registrado con éxito"
            )
            usuario = UsuarioSingleton.get_instance()
            if not usuario.es_administrador():
                InterfazLogin.mostrar_interfaz_login(root)

    @staticmethod
    @GestorErrores.decorador("Error al mostrar el login")
    def mostrar_interfaz_register(root):
        from UI.views.inicio_sesion import InterfazRegister

        InterfazRegister.mostrar_interfaz_register(root)
