from utils.utilidades_interfaz import UtilidadesParaInterfaz
from UI.gestores import GestorErrores

from models.usuarios import UsuarioSingleton
from factories import UsuarioFactory
from enums import UsuarioNombreDatos as UND

from components import (
    ContenedorPrincipal,
    LabelTituloSubtitulo,
    ContenedorBotones,
    FormularioRegister
)


class InterfazRegister(FormularioRegister):


    @classmethod
    @GestorErrores.decorador("Error al mostrar el registro")
    def mostrar_interfaz_register(cls, root):
        UtilidadesParaInterfaz.limpiar_frame_principal(root)

        # Configurar el grid de root para expansión
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        frame_register = ContenedorPrincipal(root)
        frame_register.grid(row=0, column=0, padx=10, pady=10)

        cls.__crear_interfaz_register(root, frame_register)


    @classmethod
    def __crear_interfaz_register(cls, root, frame_register):

        RUTA_IMAGEN_REGISTER = r"ULAEM-Inventario\assets\img\login.png"

        # Título
        LabelTituloSubtitulo(
            frame_register,
            "Crear una cuenta",
            UtilidadesParaInterfaz.cargar_imagen(RUTA_IMAGEN_REGISTER, (140, 120)),
        ).grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")

        # Campos a mostrar
        campos = [campo.value for campo in list(UND)]
        privilegio = UsuarioSingleton.get_instance().es_administrador()
        if privilegio == True:
            componentes = cls._crear_campos(frame_register, campos)
        elif privilegio == False:
            componentes = cls._crear_campos(frame_register, campos[:6])

        cls._crear_botones(root, frame_register, componentes)

    @classmethod
    def _crear_botones(cls, root, frame_register, componentes):
        from UI.controllers import ControladorLogin, ControladorRegister
        
        frame_botones = ContenedorBotones(frame_register)
        frame_botones.grid(row=len(componentes) + 1, column=0, columnspan=2, padx=10, pady=5)
        
        privilegio = UsuarioSingleton.get_instance().es_administrador()
        
        if privilegio == False:
            frame_botones.agregar_boton(
                "Ir atras", lambda: ControladorLogin.mostrar_interfaz_login(root), columna=0
            )
            frame_botones.agregar_boton(
                "Agregar",
                lambda: ControladorRegister.manejar_crear_cuenta(
                    root,
                    componentes[UND.CEDULA.value].get(),
                    componentes[UND.NOMBRE.value].get(),
                    componentes[UND.EMAIL.value].get(),
                    componentes[UND.CONTRASENA.value].get(),
                    componentes[UND.CONFIRMAR_CONTRASENA.value].get(),
                    componentes[UND.OCUPACION.value].get(),
                    "Sin privilegios",
                ),
                columna=0 if privilegio else 1,
                columnspan=2 if privilegio else 1,
            )
        elif privilegio == True:
            frame_botones.agregar_boton(
                "Agregar",
                lambda: ControladorRegister.manejar_crear_cuenta(
                    root,
                    componentes[UND.CEDULA.value].get(),
                    componentes[UND.NOMBRE.value].get(),
                    componentes[UND.EMAIL.value].get(),
                    componentes[UND.CONTRASENA.value].get(),
                    componentes[UND.CONFIRMAR_CONTRASENA.value].get(),
                    componentes[UND.OCUPACION.value].get(),
                    componentes[UND.PRIVILEGIOS.value].get(),
                ),
                columna=0 if privilegio else 1,
                columnspan=2 if privilegio else 1,
            )
