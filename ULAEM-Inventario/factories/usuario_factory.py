from models.usuarios import UsuarioAdministrador, UsuarioNormal
from enums import PrivilegiosUsuario, UsuarioNombreDatos as UND

class UsuarioFactory:
    @staticmethod
    def crear_usuario(datos:dict):
        print(datos)
        if datos[UND.PRIVILEGIOS.value] == PrivilegiosUsuario.ADMINISTRADOR.value:
            return UsuarioAdministrador.diccionario_a_instancia(datos)
        elif datos[UND.PRIVILEGIOS.value] == PrivilegiosUsuario.SIN_PRIVILEGIOS.value:
            return UsuarioNormal.diccionario_a_instancia(datos)
        else:
            
            raise ValueError("Tipo de privilegios no válidos")  