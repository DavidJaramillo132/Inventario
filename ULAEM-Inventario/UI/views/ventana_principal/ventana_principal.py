from utils.utilidades_interfaz import UtilidadesParaInterfaz
from components import ContenedorPrincipal


class InterfazVentanaPrincipal:
    """
    Clase encargada de gestionar y mostrar la interfaz gráfica de la ventana principal de la aplicación.
    """

    @classmethod
    def mostrar_interfaz_ventana_principal(cls, root):
        """
        Muestra la ventana principal, configurando el layout del root y creando sus elementos principales.

        Args:
            root: Contenedor principal de la interfaz gráfica.
        """
        UtilidadesParaInterfaz.limpiar_frame_principal(root)  # Limpia el frame principal.

        # Configuración del grid del root para la ventana principal.
        root.grid_rowconfigure(0, weight=1)  # La fila 0 ocupa el espacio vertical disponible.
        root.grid_columnconfigure(0, weight=0)  # La columna 0 no se expande.
        root.grid_columnconfigure(1, weight=1)  # La columna 1 se expande para llenar el espacio horizontal restante.

        cls.__crear_ventana_principal(root)  # Llama al método para configurar los elementos de la ventana principal.

    @staticmethod
    def __crear_ventana_principal(root):
        """
        Configura y añade los elementos visuales de la ventana principal, como la barra lateral y el contenedor principal.

        Args:
            root: Contenedor principal de la interfaz gráfica.
        """
        from UI.views.ventana_principal import BarraLateral  # Importa la clase para crear la barra lateral.

        # Crea y posiciona el contenedor principal.
        contenedor_principal = ContenedorPrincipal(root)
        contenedor_principal.grid(row=0, column=1, sticky="nsew")  # Se coloca en la columna derecha, ocupando el espacio disponible.

        # Crea y posiciona la barra lateral.
        barraLateral = BarraLateral(root, contenedor_principal)
        barraLateral.grid(row=0, column=0, sticky="ns")  # Se coloca en la columna izquierda, expandiéndose verticalmente.
