from utils.utilidades_interfaz import UtilidadesParaInterfaz
from UI.controllers import ControladorEditarPerfil

from enums import UsuarioNombreDatos as UND
from models.usuarios import UsuarioSingleton

from components import (
    ContenedorPrincipal,
    LabelTituloSubtitulo,
    ContenedorBotones,
    FormularioRegister,
)


class InterfazEditarPerfil(FormularioRegister):
    @classmethod
    def mostrar_editar_perfil(cls, root):
        """
        Muestra la interfaz para editar el perfil de un usuario.
        """
        UtilidadesParaInterfaz.limpiar_frame_principal(root)

        # Configurar el grid de root para expansión
        root.grid_columnconfigure(0, weight=1)
        root.grid_rowconfigure(0, weight=1)

        frame_editar_perfil = ContenedorPrincipal(root)
        frame_editar_perfil.grid(row=0, column=0, padx=10, pady=10)

        cls._crear_editar_perfil(root, frame_editar_perfil)

    @classmethod
    def _crear_editar_perfil(cls, root, frame_editar_perfil):
        RUTA_IMAGEN_EDITAR_PERFIL = r"ULAEM-Inventario\assets\img\login.png"

        # Título
        LabelTituloSubtitulo(
            frame_editar_perfil,
            "Editar Perfil",
            UtilidadesParaInterfaz.cargar_imagen(RUTA_IMAGEN_EDITAR_PERFIL, (140, 120)),
        ).grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")
    
        privilegio = UsuarioSingleton.get_instance().es_administrador()
        # Campos a mostrar (usando el Enum)
        campos = [
            UND.CEDULA.value,
            UND.NOMBRE.value,
            UND.EMAIL.value,
            UND.CONTRASENA.value,
            UND.OCUPACION.value,
            UND.PRIVILEGIOS.value,
        ]

        componentes = cls._crear_campos(frame_editar_perfil, campos)

        ControladorEditarPerfil.poblar_campos(campos, componentes)
        componentes.get(UND.CEDULA.value).configure(state="disabled")
        if privilegio == False:
            componentes.get(UND.PRIVILEGIOS.value).configure(state="disabled")

        cls._crear_botones(root, frame_editar_perfil, componentes)

    @classmethod
    def _crear_botones(cls, root, frame_editar_perfil, componentes):
        # privilegio = UsuarioSingleton.get_instance().es_administrador()

        frame_botones = ContenedorBotones(frame_editar_perfil)
        frame_botones.grid(
            row=len(componentes) + 1, column=0, columnspan=2, padx=10, pady=20
        )
    
        frame_botones.agregar_boton(
            "Actualizar Perfil",
            lambda: ControladorEditarPerfil.manejar_actualizar_perfil(
                frame_editar_perfil,
                componentes[UND.CEDULA.value].get(),
                componentes[UND.NOMBRE.value].get(),
                componentes[UND.EMAIL.value].get(),
                componentes[UND.CONTRASENA.value].get(),
                componentes[UND.OCUPACION.value].get(),
                componentes[UND.PRIVILEGIOS.value].get(),
            ),
            columna=0,
        )

        frame_botones.agregar_boton(
            "Cancelar",
            lambda: cls.mostrar_editar_perfil(root),
            columna=1,
        )
