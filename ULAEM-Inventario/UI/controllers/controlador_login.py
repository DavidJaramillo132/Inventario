from UI.gestores import GestorErrores, GestorAutentificacion
from utils.validador import Validador

class ControladorLogin:
    
    @staticmethod
    @GestorErrores.decorador("Error al mostrar la ventana de inicio de sesión")
    def mostrar_interfaz_login(root):
        from UI.views.inicio_sesion import InterfazLogin

        InterfazLogin.mostrar_interfaz_login(root)
    
    @staticmethod
    @GestorErrores.decorador("Error al iniciar sesión")
    def manejar_login(root, cedula, contrasena):
        from UI.views.ventana_principal import InterfazVentanaPrincipal
        
        
        
        Validador.validar_campos_completos(cedula, contrasena)
        
        

        
        if GestorAutentificacion.login_usuario(cedula, contrasena):
            InterfazVentanaPrincipal.mostrar_interfaz_ventana_principal(root)
        else:
            raise Exception("Credenciales ingresadas no son válidas")