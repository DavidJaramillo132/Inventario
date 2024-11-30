from models.usuarios import UsuarioAdministrador, UsuarioNormal
from enums import PrivilegiosUsuario, UsuarioNombreDatos as UND
from .factory import Factory


class UsuarioFactory(Factory):
    """
    Fábrica encargada de crear instancias de usuarios según sus privilegios.
    """

    @staticmethod
    def crear_objeto(datos):
        """
        Crea y devuelve una instancia de usuario basada en los datos proporcionados.

        Args:
            datos (list/tuple): Lista o tupla que contiene los datos del usuario. El último valor debe ser el privilegio.

        Returns:
            UsuarioAdministrador | UsuarioNormal: Instancia del usuario creada según su privilegio.

        Raises:
            Exception: Si el privilegio del usuario no es válido.
        """
        # print(datos)  # Imprime los datos para depuración.
        print(datos[-1])
        # Verifica el privilegio del usuario y retorna la instancia correspondiente.
        if datos[-1] == PrivilegiosUsuario.ADMINISTRADOR.value:
            return UsuarioAdministrador(*datos)  # Crea un usuario administrador.
        elif datos[-1] == PrivilegiosUsuario.SIN_PRIVILEGIOS.value:
            return UsuarioNormal(*datos)  # Crea un usuario normal.
        else:
            raise Exception("El usuario no tiene un privilegio válido.")  # Lanza excepción si el privilegio es inválido.
