from .servicios_usuario import ServiciosUsuario
from .servicios_aula import ServiciosAula
from .servicios_comentario import ServiciosComentario
from .servicios_elemento import ServiciosElemento


class GestorServicioSQL:

    servicios_usuario = ServiciosUsuario()
    servicios_aula = ServiciosAula()
    servicios_comentario = ServiciosComentario()
    servicios_elemento = ServiciosElemento()

    # Métodos relacionados con aulas

    @classmethod
    def obtener_aulas(cls):
        return cls.servicios_aula.obtener_aulas()

    @classmethod
    def obtener_aula_por_id(cls, id_aula):
        return cls.servicios_aula.obtener_aula_por_id(id_aula)

    @classmethod
    def crear_aula(
        cls,
        dimensiones,
        tipo,
    ):
        return cls.servicios_aula.crear_aula(dimensiones, tipo)

    @classmethod
    def eliminar_aula(cls, id_aula):
        return cls.servicios_aula.eliminar_aula(id_aula)

    # Métodos relacionados con elementos
    @classmethod
    def obtener_elementos_por_idaula(cls, id_aula):
        return cls.servicios_elemento.obtener_elementos_por_idaula(id_aula)

    @classmethod
    def agregar_elemento_a_aula(
        cls, nombre, tipo_elemento, estado, fecha_adquisicion, cantidad, id_aula
    ):
        return cls.servicios_elemento.agregar_elemento_a_aula(
            nombre, tipo_elemento, estado, fecha_adquisicion, cantidad, id_aula
        )

    @classmethod
    def eliminar_elemento_de_aula(cls, id_elemento):
        return cls.servicios_elemento.eliminar_elemento_de_aula(id_elemento)

    # Métodos relacionados con usuarios
    @classmethod
    def obtener_usuarios(cls):
        return cls.servicios_usuario.obtener_usuarios()

    @classmethod
    def obtener_cedula_contrasena(cls):
        return cls.servicios_usuario.obtener_cedula_contrasena()

    @classmethod
    def obtener_usuario_por_cedula(cls, cedula):
        return cls.servicios_usuario.obtener_usuario_por_cedula(cedula)

    @classmethod
    def actualizar_usuario(
        cls,
        cedula,
        nuevo_nombre,
        nuevo_email,
        nueva_contraseña,
        nueva_ocupacion,
        nuevos_privilegios,
    ):
        return cls.servicios_usuario.actualizar_usuario(
            cedula,
            nuevo_nombre,
            nuevo_email,
            nueva_contraseña,
            nueva_ocupacion,
            nuevos_privilegios,
        )

    @classmethod
    def registrar_usuario(
        cls, cedula, nombre, email, contrasena, ocupacion, privilegio
    ):
        return cls.servicios_usuario.registrar_usuario(
            cedula, nombre, email, contrasena, ocupacion, privilegio
        )

    @classmethod
    def eliminar_usuario(cls, cedula):
        return cls.servicios_usuario.eliminar_usuario(cedula)

    # Métodos relacionados con comentarios
    @classmethod
    def obtener_comentarios(cls):
        return cls.servicios_comentario.obtener_comentarios()

    @classmethod
    def obtener_comentarios_por_aula(cls, id_aula):
        return cls.servicios_comentario.obtener_comentarios_por_aula(id_aula)

    @classmethod
    def crear_comentario(cls, contenido, idAula, cedula):
        return cls.servicios_comentario.crear_comentario(
            contenido, idAula, cedula
        )
    @classmethod
    def eliminar_comentario(cls, id_comentario):
        return cls.servicios_comentario.eliminar_comentario(id_comentario)
