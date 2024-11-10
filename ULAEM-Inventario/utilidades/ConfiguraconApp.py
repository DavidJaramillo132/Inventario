import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog

# Clase para configuración de colores
class ConfigurarColores:
    def __init__(self):
        self.color_principal = "#111317"
        self.color_botones = "#0E4A6B"
    
    def obtener_color_principal(self):
        return self.color_principal
    
    def obtener_color_botones(self):
        return self.color_botones

# Clase para configuración de fuentes
class ConfigararFuentesTexto:
    def __init__(self):
        self.fuente_textos = ctk.CTkFont(family="Arial", size=18)
        self.fuente_titulos_subtitulos = ctk.CTkFont(family="Playfair Display", size=30, weight="bold")
        self.fuente_sinopsis = ctk.CTkFont(family="Arial", size=24)
    
    def obtener_fuente_textos(self):
        return self.fuente_textos
    
    def obtener_fuente_titulos_subtitulos(self):
        return self.fuente_titulos_subtitulos
    
    def obtener_fuente_sinopsis(self):
        return self.fuente_sinopsis

# Clase para manejo de imágenes y limpieza de frames
class UtilidadesParaInterfaz:
    # def __init__(self, ):
    #     self.frame_principal = frame_principal
    
    def limpiar_frame_principal(self,frame_principal):
        # Limpia el frame principal de widgets existentes
        for widget in frame_principal.winfo_children():
            widget.destroy()
    # def limpiar_frame_principal(self, frame_principal, ignore_count=0):
    #     # Limpia el frame principal de widgets existentes, ignorando los primeros 'ignore_count' widgets
    #     for widget in frame_principal.winfo_children()[ignore_count:]:
    #         widget.destroy()
    
    def cargar_imagen(self, ruta, dimensiones):
        imagen = Image.open(ruta)
        imagen = imagen.resize(dimensiones)
        return ImageTk.PhotoImage(imagen)

