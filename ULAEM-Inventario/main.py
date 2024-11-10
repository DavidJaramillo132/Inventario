import customtkinter as ctk
from utilidades.ConfiguraconApp import ConfigurarColores
from UI.interfaz_login_register import LoginRegister  
# import Database.conexionDB


# Clase principal de la aplicación
class App:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("1000x800")
        self.root.title("Sistema de inventario")
        self.color = ConfigurarColores()
        self.iniciarUI()
        
    def iniciarUI(self):
        # Contenedor de navegación
        navegacion = self.crear_contenedor_navegacion()
        
        # Contenedor principal de contenido
        contenido_principal = self.crear_contenedor_contenido()
        
        # Instancia de la clase LoginRegister 
        login_register = LoginRegister()
        login_register.interfaz(navegacion, contenido_principal)
    
    # Crea los contenedores donde se agregaran y quitaran los widget
    def crear_contenedor_navegacion(self):
        navegacion = ctk.CTkFrame(self.root, fg_color=self.color.color_principal, height=50)
        navegacion.pack(side="left", fill="y")
        return navegacion
    
    def crear_contenedor_contenido(self):
        contenido_principal = ctk.CTkFrame(self.root, fg_color=self.color.color_principal)
        contenido_principal.pack(fill="both", expand=True)
        return contenido_principal

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()



