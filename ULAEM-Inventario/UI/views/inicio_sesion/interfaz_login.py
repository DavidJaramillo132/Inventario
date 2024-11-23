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

    @classmethod
    @GestorErrores.decorador("Error al mostrar el login")
    def mostrar_interfaz_login(cls, root):
        UtilidadesParaInterfaz.limpiar_frame_principal(root)


        frame_login = ContenedorPrincipal(root)
        frame_login.pack(expand=True)

        cls.__crear_login(
            root,frame_login
        )

    @staticmethod
    def __crear_login(root,frame_login):
        from UI.controllers import ControladorLogin, ControladorRegister
        

        RUTA_IMAGEN_LOGIN = r"assets\img\login.png"

        LabelTituloSubtitulo(
            frame_login,
            "Iniciar Sesión",
            UtilidadesParaInterfaz.cargar_imagen(RUTA_IMAGEN_LOGIN, (180, 160)),
        ).pack(pady=50, padx=10)

        cedula_frame = EntryLabel(frame_login, UND.CEDULA.value)
        cedula_frame.pack(pady=10)

        password_frame = EntryContrasena(frame_login)
        password_frame.pack(pady=10)

        frame_botones = ContenedorBotones(frame_login)
        frame_botones.pack(pady=10)

        frame_botones.agregar_boton(
            "Iniciar Sesión",
            lambda: ControladorLogin.manejar_login(
                root, cedula_frame.entry.get(), password_frame.entry.get()
            ),
            columna=0,
        )
        frame_botones.agregar_boton(
            "Crear Cuenta aqui",
            lambda: ControladorRegister.mostrar_interfaz_register(root),
            columna=1,
        )
