import customtkinter as ctk


# Clase para configuración de fuentes
class FuentesTexto:
    @staticmethod
    def get_fuente_texto():

            return ctk.CTkFont(family="Arial", size=18)
    
    @staticmethod
    def get_fuente_titulo_subtitulo():
            return ctk.CTkFont(family="Playfair Display", size=30, weight="bold")
    
    
    @staticmethod
    def get_fuente_sinopsis():
            return ctk.CTkFont(family="Arial", size=24)



