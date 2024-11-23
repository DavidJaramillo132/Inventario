from database import GestorServicioSQL
from models.usuarios import UsuarioSingleton
from enums import UsuarioNombreDatos as UND


class GestorAutentificacion:

    @staticmethod
    def registrar_usuario(cedula, nombre, email, contrasena, ocupacion, privilegio):
        GestorServicioSQL.registrar_usuario(
            cedula, nombre, email, contrasena, ocupacion, privilegio
        )
        return True

    @staticmethod
    def actualizar_usuario(cedula, nombre, email, contrasena, ocupacion, privilegio):
        GestorServicioSQL.actualizar_usuario(
            cedula, nombre, email, contrasena, ocupacion, privilegio
        )
        return True

    @staticmethod
    def autenticar_usuario(cedula, contrasena):
        datosUsuarios = GestorServicioSQL.obtener_cedula_contrasena()
        for cedulaDB, contrasenaDB in datosUsuarios:
            if cedula == cedulaDB and contrasena == contrasenaDB:
                return True
        return False

    @staticmethod
    def login_usuario(cedula, contrasena):
        # Aquí llamas a la validación antes de registrar al usuario
        if GestorAutentificacion.autenticar_usuario(cedula, contrasena):
            datos_usuario = GestorServicioSQL.obtener_usuario_por_cedula(cedula)

            datos_usuario_dict = GestorAutentificacion.tupla_a_dict(datos_usuario)

            UsuarioSingleton.initialize(datos_usuario_dict)
            return True
        return False

    @staticmethod
    def tupla_a_dict(tupla):
        return dict(
            zip(
                [
                    UND.CEDULA.value,
                    UND.NOMBRE.value,
                    UND.EMAIL.value,
                    UND.CONTRASENA.value,
                    UND.OCUPACION.value,
                    UND.PRIVILEGIOS.value,
                ],
                tupla,
            )
        )
