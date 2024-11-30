from components import BotonPersonalizado, LabelTituloSubtitulo, ContenedorPrincipal

from utils.utilidades_interfaz import UtilidadesParaInterfaz
from models.usuarios import UsuarioSingleton


class BarraLateral(ContenedorPrincipal):
    RUTA_LOGO_ULEAM = r"assets\img\logo_uleam.png"
    DIMENSIONES_LOGO_ULEAM = (100, 80)

    def __init__(self, root, contenedor_principal, *args, **kwargs) -> None:
        super().__init__(
            root,
            border_width=2,
            width=500,
            *args,
            **kwargs,
        )

        LabelTituloSubtitulo(
            self,
            "Sistema de INVENTARIO",
            UtilidadesParaInterfaz.cargar_imagen(
                BarraLateral.RUTA_LOGO_ULEAM, BarraLateral.DIMENSIONES_LOGO_ULEAM
            ),
        ).pack(side="top", padx=20, pady=20)

        self.__mostrar_botones_laterales(root, contenedor_principal)

    def __mostrar_botones_laterales(self, root, contenedor_principal):
        from UI.controllers import ControladorBarraLateral

        usuario = UsuarioSingleton().get_instance()

        BotonPersonalizado(
            self,
            "Ver perfil",
            lambda: ControladorBarraLateral.mostrar_interfaz_editar_perfil(contenedor_principal),
        ).pack(side="top", padx=10, pady=25)

        BotonPersonalizado(
            self,
            "Ver aulas",
            lambda: ControladorBarraLateral.mostrar_interfaz_tabla_aulas(root,contenedor_principal),
        ).pack(side="top", padx=10, pady=25)

        if usuario.es_administrador():

            BotonPersonalizado(
                self,
                "Ver usuarios",
                lambda: ControladorBarraLateral.mostrar_interfaz_tabla_usuarios(root,contenedor_principal),
            ).pack(side="top", padx=10, pady=25)

            BotonPersonalizado(
                self,
                "Crear nuevas salas",
                lambda: ControladorBarraLateral.mostrar_interfaz_crear_nuevas_salas(contenedor_principal),
            ).pack(side="top", padx=10, pady=25)

            BotonPersonalizado(
                self,
                "Crear nuevo usuario",
                lambda: ControladorBarraLateral.mostrar_interfaz_register(
                    contenedor_principal
                ),
            ).pack(side="top", padx=10, pady=25)

        BotonPersonalizado(
            self,
            "Cerrar sesión",
            lambda: ControladorBarraLateral.confirmar_cerrar_sesion(root),
        ).pack(side="bottom", padx=10, pady=25)

    @staticmethod
    def passss():
        pass
