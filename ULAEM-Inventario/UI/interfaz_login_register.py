import customtkinter as ctk
import customtkinter as ctk
# from Database.conexionDB import ConexionBD
from Database.gestion_usuario import ServiciosUsuario
from  utilidades.validaciones import validaciones
from utilidades.ConfiguraconApp import ConfigurarColores, ConfigararFuentesTexto, UtilidadesParaInterfaz
from UI.notificaciones import Notificaciones_aviso
from UI.navegacion import Navegacion
from utilidades.singleton import UserSingleton

class LoginRegister:
    def __init__(self):
        self.gestion_user = ServiciosUsuario()
        self.validar = validaciones()
        self.notificacion = Notificaciones_aviso()
        self.barra_lateral = Navegacion()
        self.colores = ConfigurarColores()
        self.fuentes = ConfigararFuentesTexto()
        self.utilidades_interfaz = UtilidadesParaInterfaz()
        self.frame_principal = None
        self.imagen_ctk_login = None
        self.imagen_ctk_register = None

    def interfaz(self, navegacion, contenido_principal):
        # Crea un frame principal para login y registro
        self.frame_principal = ctk.CTkFrame(contenido_principal, fg_color="#0D1822")
        self.frame_principal.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)
        
        # Inicia en la pantalla de login
        self.mostrar_login(navegacion, contenido_principal)
        
    def mostrar_login(self, navegacion, contenido_principal):
        self.utilidades_interfaz.limpiar_frame_principal(self.frame_principal)

        # Configuración visual y fuentes
        # fuente_textos, fuente_titulos_subtitulos, _ = fuente_Letras(contenido_principal)
        
        # Imagen de login
        self.imagen_ctk_login = self.utilidades_interfaz.cargar_imagen(r"iconos\login.png", (180, 160))
        
        # Frame de login
        frame_login = ctk.CTkFrame(self.frame_principal, fg_color=self.colores.obtener_color_principal())
        frame_login.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)
        
        # Componentes del login
        self.crear_login(frame_login, navegacion, contenido_principal)
    
    def mostrar_register(self, navegacion, contenido_principal):
        self.utilidades_interfaz.limpiar_frame_principal(self.frame_principal)
        
        # fuente para los texto
        # fuente_textos, fuente_titulos_subtitulos, _ = fuente_Letras(contenido_principal)
        
        # imagen para el registro
        self.imagen_ctk_register = self.utilidades_interfaz.cargar_imagen(r"iconos\login.png", (180, 160))

        # Frame de registro
        frame_registro = ctk.CTkFrame(self.frame_principal, fg_color=self.colores.obtener_color_principal())
        frame_registro.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)
        
        # Componentes del registro
        self.crear_register(frame_registro, navegacion, contenido_principal)


    def crear_login(self, frame, navegacion, contenido_principal):
        # Componentes visuales de la pantalla de login
        ctk.CTkLabel(frame, image=self.imagen_ctk_login, text="").pack(pady=40)
        ctk.CTkLabel(frame, text="Iniciar Sesión", font=self.fuentes.obtener_fuente_titulos_subtitulos()).pack(pady=10)
        
        # campos de entrada y botones
        ctk.CTkLabel(frame, text="Cedula: ", font=self.fuentes.obtener_fuente_titulos_subtitulos()).pack(pady=10)
        entry_cedula = ctk.CTkEntry(frame, height=50, width=200, fg_color=self.colores.obtener_color_principal(), border_width=10, border_color="#0D1822")
        entry_cedula.pack(pady=10)
        
        ctk.CTkLabel(frame, text="Contraseña", font=self.fuentes.obtener_fuente_titulos_subtitulos()).pack(pady=10)
        entry_password = ctk.CTkEntry(frame, show="*", height=50, width=200, fg_color=self.colores.obtener_color_principal(), border_width=10, border_color="#0D1822")
        entry_password.pack(pady=10)
        
        # botones de login
        frame_botones = ctk.CTkFrame(frame, fg_color=self.colores.obtener_color_principal())
        frame_botones.pack(pady=20)

        button_login = ctk.CTkButton(frame_botones, text="Iniciar Sesión", font=self.fuentes.obtener_fuente_textos(), fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                                     command=lambda: self.validar_y_gestionar("login", navegacion, contenido_principal, entry_cedula, entry_password))
        button_login.grid(row=0, column=0, padx=10)

        button_register = ctk.CTkButton(frame_botones, text="Crear Cuenta aqui", font=self.fuentes.obtener_fuente_textos(), fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                                        command=lambda: self.mostrar_register(navegacion, contenido_principal))
        button_register.grid(row=0, column=1, padx=10)

    def crear_register(self, frame, navegacion, contenido_principal):
        # Componentes de registro
        ctk.CTkLabel(frame, image=self.imagen_ctk_register, text="").pack(pady=20)
        ctk.CTkLabel(frame, text="Registrar Nuevo Usuario", font=self.fuentes.obtener_fuente_textos()).pack(pady=10)

        # Formulario para el registro
        frame_formulario = ctk.CTkFrame(frame, fg_color=self.colores.obtener_color_principal())
        frame_formulario.pack(pady=20, padx=10)

        campos = [("Ingrese su Cedula:", 0), ("Ingrese su Nombre:", 1), ("Ingrese su Email:", 2), ("Ingrese su Contraseña:", 3), ("Ingrese su rol:", 4)]
        entradas_de_valores = {}
        
        for label_texto, fila in campos:    
            label = ctk.CTkLabel(frame_formulario, text=label_texto, font=self.fuentes.obtener_fuente_textos())
            label.grid(row=fila, column=0, padx=10, pady=10, sticky="w")
            
            entry = ctk.CTkEntry(frame_formulario, height=50, width=200, fg_color=self.colores.obtener_color_principal(), border_width=10, border_color="#0D1822")
            entry.grid(row=fila, column=1, padx=10, pady=10)
            entradas_de_valores[label_texto] = entry
            
        rango = ["Software", "IT", "Profesor"]
        entry_rango = ctk.CTkComboBox(frame_formulario, values=rango, height=50, width=200, fg_color=self.colores.obtener_color_principal(), border_width=10, border_color="#0D1822")
        entry_rango.grid(row=4, column=1, padx=10, pady=10)

        button_register = ctk.CTkButton(frame_formulario, text="Agregar", font=self.fuentes.obtener_fuente_textos(), fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
            command=lambda: self.validar_y_gestionar("registro", navegacion, contenido_principal, entradas_de_valores["Ingrese su Cedula:"],entradas_de_valores["Ingrese su Contraseña:"],
                                                     entradas_de_valores["Ingrese su Nombre:"], entradas_de_valores["Ingrese su Email:"], entry_rango))
                                                                
        button_register.grid(row=5, column=1, padx=10, pady=10, sticky="w")
    
        
    def validar_y_gestionar(self, accion, navegacion, contenido_principal, entry_cedula, entry_password, entry_nombre=None, entry_email=None, entry_rango=None):
        singleton = UserSingleton.get_instance()

        # Validar y gestionar el inicio de sesión o registro
        cedula = entry_cedula.get()
        password = entry_password.get()
        # Verifica si validarLogin es None para evitar el error de desempaquetado


        # Desempaqueta los valores si validarLogin no es None

        # Verificación de campos
        if not cedula or not password:
            self.notificacion.show_info("Error", "Cedula y contraseña son obligatorios.")
            return

        if accion == "login":
            self.validar.validar_cedula(cedula)
            self.validar.validar_contrasena(password)
            validarLogin = self.gestion_user.obtener_usuario(cedula)
            sqlcedula , sqlnombre, sqlemail, sqlpassword, sqlrango = validarLogin
            if sqlcedula == "1111111111": 
                # Llamada correcta sin el argumento `cedula`
                self.barra_lateral.mostrar_botones_laterales(navegacion, contenido_principal, "administrador")
                singleton.initialize("Administrador", sqlcedula, sqlnombre, sqlemail, sqlpassword, sqlrango)
            else:
                self.barra_lateral.mostrar_botones_laterales(navegacion, contenido_principal, "usuario")
                singleton.initialize("Supervisor", sqlcedula, sqlnombre, sqlemail, sqlpassword, sqlrango)

        elif accion == "registro":
            nombre = entry_nombre.get()
            email = entry_email.get()
            rango = entry_rango.get()

            # Verificar campos obligatorios para registro
            if not all([cedula, nombre, email, password, rango]):
                self.notificacion.show_info("Error", "Todos los campos son obligatorios.")
                return

            # Validaciones adicionales
            self.validar.validar_texto(nombre)
            self.validar.validar_email(email)
            self.validar.validar_texto(rango)
            validarRegistro = self.gestion_user.registrar_usuario(cedula, nombre, email, password, rango)
            
            if validarRegistro: 
                singleton.initialize("Supervisor", cedula, nombre, email, password, rango)
                self.barra_lateral.mostrar_botones_laterales(navegacion, contenido_principal, "usuario")