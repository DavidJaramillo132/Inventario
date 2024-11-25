import customtkinter as ctk

from PIL import Image

class UtilidadesParaInterfaz:
    """
    Esta clase proporciona métodos estáticos para la gestión de widgets en una interfaz gráfica.
    Incluye funciones para limpiar un contenedor, configurar su diseño en la cuadrícula, 
    y cargar imágenes con dimensiones específicas.
    """

    @staticmethod
    def limpiar_frame_principal(root):
        """
        Limpia todos los widgets del contenedor principal (`root`) y restablece la configuración del grid.
        
        Args:
            root: Contenedor principal de la interfaz gráfica.
        """
        for widget in root.winfo_children():
            widget.destroy()  # Destruye todos los widgets hijos en el contenedor.
        UtilidadesParaInterfaz.limpiar_grid(root)  # Restablece el grid del contenedor.

    @staticmethod
    def limpiar_grid(root):
        """
        Restablece la configuración del grid de un contenedor (`root`), eliminando pesos de columnas y filas.
        
        Args:
            root: Contenedor cuyo grid se va a restablecer.
        """
        for i in range(root.grid_size()[0]):
            root.grid_columnconfigure(i, weight=0)  # Elimina el peso de cada columna en el grid.
        for i in range(root.grid_size()[1]):
            root.grid_rowconfigure(i, weight=0)  # Elimina el peso de cada fila en el grid.

    @staticmethod
    def configurar_grid(widget, row, column, padx=10, pady=10, columnspan=1, sticky="nsew"):
        """
        Configura un widget en un grid con los parámetros especificados.

        Args:
            widget: El widget a configurar.
            row (int): Fila en la que se colocará el widget.
            column (int): Columna en la que se colocará el widget.
            padx (int): Margen horizontal alrededor del widget. Por defecto es 10.
            pady (int): Margen vertical alrededor del widget. Por defecto es 10.
            columnspan (int): Número de columnas que ocupará el widget. Por defecto es 1.
            sticky (str): Define cómo debe expandirse el widget dentro de su celda. Por defecto es "nsew".
        """
        widget.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)

    @staticmethod
    def cargar_imagen(ruta, dimensiones):
        """
        Carga una imagen desde una ruta especificada y la adapta a las dimensiones dadas.

        Args:
            ruta (str): Ruta del archivo de imagen.
            dimensiones (tuple): Tamaño al que se debe ajustar la imagen (ancho, alto).

        Returns:
            CTkImage: Una instancia de imagen adaptada para su uso en una interfaz gráfica personalizada.
        """
        imagenctk = Image.open(ruta)  # Abre la imagen desde la ruta especificada.
        return ctk.CTkImage(imagenctk, size=dimensiones)  # Ajusta la imagen a las dimensiones especificadas.
