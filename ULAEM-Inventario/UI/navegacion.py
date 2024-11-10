from PIL import Image, ImageTk
import customtkinter as ctk
from UI.tabla import Tabla
from utilidades.ConfiguraconApp import ConfigurarColores, ConfigararFuentesTexto, UtilidadesParaInterfaz
from UI.notificaciones import Notificaciones_aviso
import UI.Usuario as claseUsuario
from utilidades.singleton import UserSingleton
    
class Navegacion:
    def __init__(self):
        self.notificacion = Notificaciones_aviso()
        self.colores = ConfigurarColores()
        self.fuentes = ConfigararFuentesTexto()
        self.utilidades_interfaz = UtilidadesParaInterfaz()
        self.tablas = Tabla()
        # self.usuario = claseUsuario.Supervisor("1315844983", "admin", "admin@example.com", "contra", "admin")
        # self.admin = claseUsuario.Administrador("1315844983", "admin", "admin@example.com", "contra", "admin")


        
    def mostrar_botones_laterales(self, navegacion, contenido_principal, tipo_usuario):
        # UserSingleton.initialize()
        # Cargar y mostrar imagen
        imagen_tk = self.utilidades_interfaz.cargar_imagen(r"iconos\LOGO-ULEAM.png",(100, 80))
        label_imagen = ctk.CTkLabel(navegacion, image=imagen_tk, text="")
        label_imagen.image = imagen_tk  # Evitar que la imagen sea eliminada por el recolector de basura
        label_imagen.pack(side="top", padx=20, pady=10)
        usuario = UserSingleton.get_instance()




        # Instanciar usuario o administrador según el tipo
        if tipo_usuario == "usuario":
            # usuario = UserSingleton.get_instance()

            # Botones específicos para usuario
            ctk.CTkButton(navegacion, text="Ver perfil", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                          command=lambda: usuario.ver_perfil(contenido_principal)).pack(side="top", padx=10, pady=25)
            ctk.CTkButton(navegacion, text="Aulas", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                          command=lambda: self.tablas.supervisor_crear_tabla_aula(contenido_principal)).pack(side="top", padx=10, pady=25)

        elif tipo_usuario == "administrador":
            
            # admin = UserSingleton.get_instance()

            # Botones específicos para administrador
            ctk.CTkButton(navegacion, text="Aulas", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                          command=lambda: self.tablas.admin_crear_tabla_aula(contenido_principal)).pack(side="top", padx=10, pady=25)
            ctk.CTkButton(navegacion, text="Crear nueva sala", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                          command=lambda: usuario.crear_nueva_sala(contenido_principal)).pack(side="top", padx=10, pady=25)
            ctk.CTkButton(navegacion, text="Ingresar usuarios", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                          command=lambda: usuario.ingresar_usuario(contenido_principal)).pack(side="top", padx=10, pady=25)
            ctk.CTkButton(navegacion, text="Ver Usuarios", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                          command=lambda: usuario.ver_usuario(contenido_principal)).pack(side="top", padx=10, pady=25)