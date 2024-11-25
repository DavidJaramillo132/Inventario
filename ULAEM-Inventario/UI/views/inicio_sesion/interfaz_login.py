from utils.utilidades_interfaz import UtilidadesParaInterfaz
from UI.gestores import GestorErrores
from enums import UsuarioNombreDatos as UND

from components import (
    EntryContrasena,
    EntryLabel,
    LabelTituloSubtitulo,
    ContenedorBotones,
    ContenedorPrincipal
)


class InterfazLogin:
    """
    Clase encargada de manejar la interfaz gráfica del login en la aplicación.
    Proporciona métodos para mostrar la interfaz y configurar sus elementos visuales.
    """

    @classmethod
    @GestorErrores.decorador("Error al mostrar el login")
    def mostrar_interfaz_login(cls, root):
        """
        Muestra la interfaz de inicio de sesión.
        
        Este método limpia el frame principal, crea un contenedor para la interfaz de login,
        y configura sus elementos.

        Args:
            root: Contenedor principal de la interfaz gráfica.
        """
        UtilidadesParaInterfaz.limpiar_frame_principal(root)  # Limpia el contenedor principal.

        # Crea el contenedor principal para la interfaz de login.
        frame_login = ContenedorPrincipal(root)
        frame_login.pack(expand=True)  # Configura para que se expanda.

        # Llama al método privado para construir los elementos del login.
        cls.__crear_login(root, frame_login)

    @staticmethod
    def __crear_login(root, frame_login):
        """
        Configura y agrega los elementos gráficos de la interfaz de login.

        Args:
            root: Contenedor principal de la interfaz gráfica.
            frame_login: Frame donde se colocarán los elementos del login.
        """
        from UI.controllers import ControladorLogin, ControladorRegister

        # Ruta de la imagen del login.
        RUTA_IMAGEN_LOGIN = r"assets\img\login.png"

        # Crea un título con una imagen representativa.
        LabelTituloSubtitulo(
            frame_login,
            "Iniciar Sesión",
            UtilidadesParaInterfaz.cargar_imagen(RUTA_IMAGEN_LOGIN, (180, 160)),
        ).pack(pady=50, padx=10)

        # Campo para introducir la cédula.
        cedula_frame = EntryLabel(frame_login, UND.CEDULA.value)
        cedula_frame.pack(pady=10)

        # Campo para introducir la contraseña.
        password_frame = EntryContrasena(frame_login)
        password_frame.pack(pady=10)

        # Frame que contendrá los botones.
        frame_botones = ContenedorBotones(frame_login)
        frame_botones.pack(pady=10)

        # Botón para iniciar sesión.
        frame_botones.agregar_boton(
            "Iniciar Sesión",
            lambda: ControladorLogin.manejar_login(
                root, cedula_frame.entry.get(), password_frame.entry.get()
            ),
            columna=0,
        )

        # Botón para crear una cuenta.
        frame_botones.agregar_boton(
            "Crear Cuenta aqui",
            lambda: ControladorRegister.mostrar_interfaz_register(root),
            columna=1,
        )
