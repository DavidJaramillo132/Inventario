import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog
from Database.querySQL import operacionSQL
from UI.notificaciones import Notificaciones_aviso

# Clase para configuración de colores
class ConfigurarColores:
    def __init__(self):
        self.color_principal = "#111317"
        self.color_botones = "#0E4A6B"
        self.border_color = "#0D1822"
    
    def obtener_color_principal(self):
        return self.color_principal
    
    def obtener_color_botones(self):
        return self.color_botones
    def obtener_color_bordes(self):
        return self.border_color
    

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
    def __init__(self):
        self.operacionesSQL = operacionSQL()
        self.notificacion = Notificaciones_aviso()

    
    def limpiar_frame_principal(self,frame_principal):
        # Limpia el frame principal de widgets existentes
        for widget in frame_principal.winfo_children():
            widget.destroy()
    
    def cargar_imagen(self, ruta, dimensiones):
        imagen = Image.open(ruta)
        imagen = imagen.resize(dimensiones)
        return ImageTk.PhotoImage(imagen)
    
    def habilitar_edicion(self, entry_nombre, entry_email, entry_contraseña, entry_rango):
        entry_nombre.configure(state="normal")
        entry_email.configure(state="normal")
        entry_contraseña.configure(state="normal")
        entry_rango.configure(state="normal")
        self.notificacion.show_info("Perfil", "Ya puede editar el perfil")


    def guardar_cambios(self, entry_nombre, entry_email, entry_contraseña, entry_rango, cedula):
        nuevo_nombre = entry_nombre.get()
        nuevo_email = entry_email.get()
        nueva_contraseña = entry_contraseña.get()
        nuevo_rango = entry_rango.get()
        try:
            self.operacionesSQL.actualizar_valores(nuevo_nombre, nuevo_email, nueva_contraseña, nuevo_rango, cedula)
            self.notificacion.show_info("Datos actualizados", "Usuario modificado correctamente")
        except Exception as e:
            self.notificacion.show_error("Error", f"No se pudo modificar el usuario: {e}")