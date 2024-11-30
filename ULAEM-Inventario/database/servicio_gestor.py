from .servicios_usuario import ServiciosUsuario
from .servicios_aula import ServiciosAula
from .servicios_comentario import ServiciosComentario
from .servicios_elemento import ServiciosElemento


class GestorServicioSQL:
    """
    Clase que actúa como intermediario entre la capa de servicios y la lógica de la aplicación,
    gestionando operaciones relacionadas con aulas, elementos, usuarios y comentarios.
    """

    servicios_usuario = ServiciosUsuario()  # Instancia para gestionar operaciones de usuario.
    servicios_aula = ServiciosAula()  # Instancia para gestionar operaciones de aulas.
    servicios_comentario = ServiciosComentario()  # Instancia para gestionar operaciones de comentarios.
    servicios_elemento = ServiciosElemento()  # Instancia para gestionar operaciones de elementos.

    # Métodos relacionados con aulas
    @classmethod
    def obtener_aulas(cls):
        """
        Obtiene todas las aulas registradas.

        Returns:
            list: Lista de aulas.
        """
        return cls.servicios_aula.obtener_aulas()
    
    @classmethod
    def obtener_id_aula(cls,id_aula):
        """
        Obtiene todas las aulas registradas.

        Returns:
            list: Lista de aulas.
        """
        return cls.servicios_aula.obtener_id_aula(id_aula)

    @classmethod
    def obtener_aula_por_id(cls, id_aula):
        """
        Obtiene los detalles de una aula específica por su ID.

        Args:
            id_aula (int): ID del aula.

        Returns:
            dict: Detalles del aula.
        """
        return cls.servicios_aula.obtener_aula_por_id(id_aula)

    @classmethod
    def crear_aula(cls,idAula, dimensiones, tipo):
        """
        Crea un aula con las dimensiones y tipo especificados.

        Args:
            dimensiones (int): Dimensiones del aula.
            tipo (str): Tipo de aula.

        Returns:
            bool: True si la creación fue exitosa.
        """
        return cls.servicios_aula.crear_aula(idAula,dimensiones, tipo)

    @classmethod
    def eliminar_aula(cls, id_aula):
        """
        Elimina un aula por su ID.

        Args:
            id_aula (int): ID del aula.

        Returns:
            bool: True si la eliminación fue exitosa.
        """
        return cls.servicios_aula.eliminar_aula(id_aula)

    # Métodos relacionados con elementos
    @classmethod
    def obtener_elementos_por_idaula(cls, id_aula):
        """
        Obtiene todos los elementos asociados a un aula específica.

        Args:
            id_aula (int): ID del aula.

        Returns:
            list: Lista de elementos del aula.
        """
        return cls.servicios_elemento.obtener_elementos_por_idaula(id_aula)
    
    @classmethod
    def actualizar_elemento(cls,id_elemento,nombre, tipo, estado, fecha_adquisicion, cantidad):
        return cls.servicios_elemento.actualizar_elemento(id_elemento,nombre, tipo, estado, fecha_adquisicion, cantidad)

    @classmethod
    def agregar_elemento_a_aula(cls, nombre, tipo_elemento, estado, fecha_adquisicion, cantidad, id_aula):
        """
        Agrega un elemento a un aula específica.

        Args:
            nombre (str): Nombre del elemento.
            tipo_elemento (str): Tipo de elemento.
            estado (str): Estado del elemento.
            fecha_adquisicion (str): Fecha de adquisición del elemento (YYYY-MM-DD).
            cantidad (int): Cantidad de elementos.
            id_aula (int): ID del aula.

        Returns:
            bool: True si la operación fue exitosa.
        """
        return cls.servicios_elemento.agregar_elemento_a_aula(
            nombre, tipo_elemento, estado, fecha_adquisicion, cantidad, id_aula
        )

    @classmethod
    def eliminar_elemento_de_aula(cls, id_elemento):
        """
        Elimina un elemento específico de un aula.

        Args:
            id_elemento (int): ID del elemento.

        Returns:
            bool: True si la operación fue exitosa.
        """
        return cls.servicios_elemento.eliminar_elemento_de_aula(id_elemento)

    # Métodos relacionados con usuarios
    @classmethod
    def obtener_usuarios(cls):
        """
        Obtiene todos los usuarios registrados.

        Returns:
            list: Lista de usuarios.
        """
        return cls.servicios_usuario.obtener_usuarios()

    @classmethod
    def obtener_cedula_contrasena(cls):
        """
        Obtiene todas las cédulas y contraseñas registradas.

        Returns:
            list: Lista de tuplas (cédula, contraseña).
        """
        return cls.servicios_usuario.obtener_cedula_contrasena()

    @classmethod
    def obtener_usuario_por_cedula(cls, cedula):
        """
        Obtiene los datos de un usuario específico por su cédula.

        Args:
            cedula (str): Cédula del usuario.

        Returns:
            dict: Datos del usuario.
        """
        return cls.servicios_usuario.obtener_usuario_por_cedula(cedula)

    @classmethod
    def actualizar_usuario(cls, cedula, nuevo_nombre, nuevo_email, nueva_contraseña, nueva_ocupacion, nuevos_privilegios):
        """
        Actualiza los datos de un usuario existente.

        Args:
            cedula (str): Cédula del usuario.
            nuevo_nombre (str): Nuevo nombre del usuario.
            nuevo_email (str): Nuevo email del usuario.
            nueva_contraseña (str): Nueva contraseña del usuario.
            nueva_ocupacion (str): Nueva ocupación del usuario.
            nuevos_privilegios (str): Nuevos privilegios asignados al usuario.

        Returns:
            bool: True si la operación fue exitosa.
        """
        return cls.servicios_usuario.actualizar_usuario(
            cedula, nuevo_nombre, nuevo_email, nueva_contraseña, nueva_ocupacion, nuevos_privilegios
        )

    @classmethod
    def registrar_usuario(cls, cedula, nombre, email, contrasena, ocupacion, privilegio):
        """
        Registra un nuevo usuario en la base de datos.

        Args:
            cedula (str): Cédula del usuario.
            nombre (str): Nombre del usuario.
            email (str): Email del usuario.
            contrasena (str): Contraseña del usuario.
            ocupacion (str): Ocupación del usuario.
            privilegio (str): Nivel de privilegio del usuario.

        Returns:
            bool: True si la operación fue exitosa.
        """
        return cls.servicios_usuario.registrar_usuario(
            cedula, nombre, email, contrasena, ocupacion, privilegio
        )

    @classmethod
    def eliminar_usuario(cls, cedula):
        """
        Elimina un usuario específico por su cédula.

        Args:
            cedula (str): Cédula del usuario.

        Returns:
            bool: True si la operación fue exitosa.
        """
        return cls.servicios_usuario.eliminar_usuario(cedula)

    # Métodos relacionados con comentarios
    @classmethod
    def obtener_comentarios_por_aula(cls, id_aula):
        """
        Obtiene todos los comentarios asociados a un aula específica.

        Args:
            id_aula (int): ID del aula.

        Returns:
            list: Lista de comentarios del aula.
        """
        return cls.servicios_comentario.obtener_comentarios_por_aula(id_aula)

    @classmethod
    def crear_comentario(cls, contenido, idAula, cedula):
        """
        Crea un comentario asociado a un aula.

        Args:
            contenido (str): Contenido del comentario.
            idAula (int): ID del aula asociada.
            cedula (str): Cédula del usuario que realiza el comentario.

        Returns:
            bool: True si la operación fue exitosa.
        """
        return cls.servicios_comentario.crear_comentario(contenido, idAula, cedula)

    @classmethod
    def eliminar_comentario(cls, id_comentario):
        """
        Elimina un comentario específico por su ID.

        Args:
            id_comentario (int): ID del comentario.

        Returns:
            bool: True si la operación fue exitosa.
        """
        return cls.servicios_comentario.eliminar_comentario(id_comentario)
