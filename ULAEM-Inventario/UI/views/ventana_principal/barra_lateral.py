from components import BotonPersonalizado, LabelTituloSubtitulo, ContenedorPrincipal

from utils.utilidades_interfaz import UtilidadesParaInterfaz
from models.usuarios import UsuarioSingleton

class BarraLateral(ContenedorPrincipal):
    """""
    Clase que representa la barra lateral de la interfaz gráfica.
    Extiende la clase `ContenedorPrincipal` y contiene botones y elementos visuales 
    para interactuar con el sistema de inventario.
    """""
    RUTA_LOGO_ULEAM = r"assets\img\logo_uleam.png"  # Ruta al logo de la ULEAM
    DIMENSIONES_LOGO_ULEAM = (100, 80)  # Dimensiones del logo (ancho, alto)

    def __init__(self, root, contenedor_principal, *args, **kwargs) -> None:
        """""
        Constructor de la clase BarraLateral.

        Args:
            root: Elemento raíz de la interfaz gráfica.
            contenedor_principal: Contenedor donde se cargan las vistas principales.
            *args, **kwargs: Argumentos adicionales para personalizar el contenedor.
        """""
        super().__init__(
            root,
            border_width=2,  # Ancho del borde de la barra lateral
            width=500,  # Ancho de la barra lateral
            *args,
            **kwargs,
        )

        # Agrega un título y un subtítulo junto con el logo a la barra lateral
        LabelTituloSubtitulo(
            self,
            "Sistema de INVENTARIO",  # Título de la barra lateral
            UtilidadesParaInterfaz.cargar_imagen(BarraLateral.RUTA_LOGO_ULEAM, BarraLateral.DIMENSIONES_LOGO_ULEAM
            ),  # Carga la imagen del logo
        ).pack(side="top", padx=20, pady=20)  # Configuración del diseño

        # Llama al método que agrega los botones laterales
        self.__mostrar_botones_laterales(root, contenedor_principal)

    def __mostrar_botones_laterales(self, root, contenedor_principal):
        """""
        Método que crea y muestra los botones de la barra lateral.

        Args:
            root: Elemento raíz de la interfaz gráfica.
            contenedor_principal: Contenedor donde se cargan las vistas principales.
        """""
        from UI.controllers import ControladorBarraLateral  # Importación de los controladores necesarios

        usuario = UsuarioSingleton().get_instance()  # Obtiene la instancia única del usuario

        # Botón para acceder al perfil del usuario
        BotonPersonalizado(
            self,
            "Ver perfil",  # Etiqueta del botón
            lambda: ControladorBarraLateral.mostrar_interfaz_editar_perfil(contenedor_principal),  # Acción del botón
        ).pack(side="top", padx=10, pady=25)  # Configuración del diseño

        # Botón para ver las aulas disponibles
        BotonPersonalizado(
            self,
            "Ver aulas",
            lambda: ControladorBarraLateral.mostrar_interfaz_tabla_aulas(root, contenedor_principal),
        ).pack(side="top", padx=10, pady=25)

        # Opciones adicionales si el usuario es administrador
        if usuario.es_administrador():
            # Botón para ver la lista de usuarios
            BotonPersonalizado(
                self,
                "Ver usuarios",
                lambda: ControladorBarraLateral.mostrar_interfaz_tabla_usuarios(root, contenedor_principal),
            ).pack(side="top", padx=10, pady=25)

            # Botón para crear nuevas salas
            BotonPersonalizado(
                self,
                "Crear nuevas salas",
                lambda: ControladorBarraLateral.mostrar_interfaz_crear_nuevas_salas(contenedor_principal),
            ).pack(side="top", padx=10, pady=25)

            # Botón para registrar un nuevo usuario
            BotonPersonalizado(
                self,
                "Crear nuevo usuario",
                lambda: ControladorBarraLateral.mostrar_interfaz_register(
                    contenedor_principal
                ),
            ).pack(side="top", padx=10, pady=25)

        # Botón para cerrar la sesión
        BotonPersonalizado(
            self,
            "Cerrar sesión",
            lambda: ControladorBarraLateral.confirmar_cerrar_sesion(root),
        ).pack(side="bottom", padx=10, pady=25)

    @staticmethod
    def passss():
        """""
        Método vacío. Puede ser utilizado como un placeholder.
        """""
        pass
