from UI.gestores import GestorErrores, GestorAutentificacion
from utils.validador import Validador

class ControladorLogin:
    """
    Clase que actúa como controlador para manejar las acciones relacionadas con el inicio de sesión.
    Contiene métodos estáticos para mostrar la interfaz de login y procesar el inicio de sesión.
    """
    
    @staticmethod
    @GestorErrores.decorador("Error al mostrar la ventana de inicio de sesión")
    def mostrar_interfaz_login(root):
        """
        Muestra la interfaz de inicio de sesión.

        Args:
            root: Contenedor principal de la interfaz gráfica.
        """
        from UI.views.inicio_sesion import InterfazLogin  # Importa la clase encargada de la interfaz de login.

        InterfazLogin.mostrar_interfaz_login(root)  # Llama al método para mostrar la interfaz de login.

    @staticmethod
    @GestorErrores.decorador("Error al iniciar sesión")
    def manejar_login(root, cedula, contrasena):
        """
        Maneja el proceso de inicio de sesión verificando las credenciales proporcionadas.

        Args:
            root: Contenedor principal de la interfaz gráfica.
            cedula (str): Cédula ingresada por el usuario.
            contrasena (str): Contraseña ingresada por el usuario.

        Raises:
            Exception: Si las credenciales son inválidas.
        """
        from UI.views.ventana_principal import InterfazVentanaPrincipal  # Importa la clase para la ventana principal.
        
        # Valida que los campos de cédula y contraseña no estén vacíos.
        Validador.validar_campos_completos(cedula, contrasena)

        # Intenta autenticar al usuario con las credenciales proporcionadas.
        if GestorAutentificacion.login_usuario(cedula, contrasena):
            InterfazVentanaPrincipal.mostrar_interfaz_ventana_principal(root)  # Muestra la ventana principal.
        else:
            raise Exception("Credenciales ingresadas no son válidas")  # Lanza una excepción si las credenciales no son válidas.
