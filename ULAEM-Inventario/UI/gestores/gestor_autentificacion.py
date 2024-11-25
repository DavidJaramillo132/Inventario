from database import GestorServicioSQL
from models.usuarios import UsuarioSingleton
# from enums import UsuarioNombreDatos as UND


class GestorAutentificacion:
    """
    Clase encargada de gestionar las operaciones relacionadas con la autenticación y registro de usuarios,
    incluyendo el manejo de registros, actualizaciones y validaciones de credenciales.
    """

    @staticmethod
    def registrar_usuario(cedula, nombre, email, contrasena, ocupacion, privilegio):
        """
        Registra un nuevo usuario en la base de datos a través del servicio SQL.

        Args:
            cedula (str): Cédula del usuario.
            nombre (str): Nombre del usuario.
            email (str): Email del usuario.
            contrasena (str): Contraseña del usuario.
            ocupacion (str): Ocupación del usuario.
            privilegio (str): Nivel de privilegio del usuario.

        Returns:
            bool: True si el registro se realiza correctamente.
        """
        GestorServicioSQL.registrar_usuario(
            cedula, nombre, email, contrasena, ocupacion, privilegio
        )
        return True

    @staticmethod
    def actualizar_usuario(cedula, nombre, email, contrasena, ocupacion, privilegio):
        """
        Actualiza los datos de un usuario existente en la base de datos.

        Args:
            cedula (str): Cédula del usuario.
            nombre (str): Nombre del usuario.
            email (str): Email del usuario.
            contrasena (str): Contraseña del usuario.
            ocupacion (str): Ocupación del usuario.
            privilegio (str): Nivel de privilegio del usuario.

        Returns:
            bool: True si la actualización se realiza correctamente.
        """
        GestorServicioSQL.actualizar_usuario(
            cedula, nombre, email, contrasena, ocupacion, privilegio
        )
        return True

    @staticmethod
    def autenticar_usuario(cedula, contrasena):
        """
        Verifica si las credenciales de un usuario coinciden con las almacenadas en la base de datos.

        Args:
            cedula (str): Cédula del usuario.
            contrasena (str): Contraseña del usuario.

        Returns:
            bool: True si las credenciales son válidas, False en caso contrario.
        """
        datosUsuarios = GestorServicioSQL.obtener_cedula_contrasena()  # Obtiene todas las cédulas y contraseñas registradas.
        for cedulaDB, contrasenaDB in datosUsuarios:
            if cedula == cedulaDB and contrasena == contrasenaDB:  # Compara las credenciales ingresadas con las almacenadas.
                return True
        return False

    @staticmethod
    def login_usuario(cedula, contrasena):
        """
        Realiza el proceso de inicio de sesión, autentica al usuario y carga sus datos en un singleton.

        Args:
            cedula (str): Cédula del usuario.
            contrasena (str): Contraseña del usuario.

        Returns:
            bool: True si el inicio de sesión es exitoso, False en caso contrario.
        """
        if GestorAutentificacion.autenticar_usuario(cedula, contrasena):  # Verifica las credenciales del usuario.
            datos_usuario = GestorServicioSQL.obtener_usuario_por_cedula(cedula)  # Obtiene los datos completos del usuario.
            
            UsuarioSingleton.initialize(datos_usuario)  # Inicializa el singleton con los datos del usuario autenticado.
            return True
        return False

