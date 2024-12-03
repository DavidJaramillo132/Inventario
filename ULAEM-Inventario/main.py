import customtkinter as ctk
from UI.controllers import ControladorLogin
from assets import Colores
from UI.gestores import GestorErrores


# Clase principal de la aplicación
class App:
    """Clase principal que ejecuta el programa entero"""
    def __init__(self):
        self.root = ctk.CTk()
        self.configurar_ventana_principal()
        self.iniciar_UI()

    def configurar_ventana_principal(self):
        self.ancho = self.root.winfo_screenwidth()
        self.alto = self.root.winfo_screenheight() 
        self.root.title("")
        self.root.state("zoomed")
        self.root.configure(fg_color=Colores.get_color_principal())

        self.root.geometry(f"{self.ancho}x{self.alto}")
        self.root.resizable(False, False)

    @GestorErrores.decorador("Error al iniciar la interfaz")
    def iniciar_UI(self):
        ControladorLogin.mostrar_interfaz_login(self.root)

    @GestorErrores.decorador("Error al iniciar la aplicación")
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
