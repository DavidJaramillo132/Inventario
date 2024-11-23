import customtkinter as ctk

from PIL import Image

class UtilidadesParaInterfaz:
    @staticmethod
    def limpiar_frame_principal(root):
        # Limpia el frame principal de widgets existentes
        for widget in root.winfo_children():
            widget.destroy()
        UtilidadesParaInterfaz.limpiar_grid(root)
        
    @staticmethod
    def limpiar_grid(root):
        for i in range(root.grid_size()[0]):  # Resetear columnas
            root.grid_columnconfigure(i, weight=0)
        for i in range(root.grid_size()[1]):  # Resetear filas
            root.grid_rowconfigure(i, weight=0)
       
    @staticmethod     
    def configurar_grid(widget, row, column, padx=10, pady=10, columnspan=1, sticky="nsew"):
        widget.grid(row=row, column=column, padx=padx, pady=pady, columnspan=columnspan, sticky=sticky)


    @staticmethod
    def cargar_imagen(ruta, dimensiones):
        imagenctk = Image.open(ruta)
        return ctk.CTkImage(imagenctk, size=dimensiones)


