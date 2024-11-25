class UsuarioSingleton:
    """""
    Clase Singleton para gestionar una única instancia de usuario. 
    Esta clase se asegura de que solo exista una instancia de UsuarioSingleton en toda la aplicación.
    """""
    _instance = None  # Variable de clase para almacenar la única instancia del Singleton
    _usuario = None  # Almacena los datos del usuario
    is_initialized = False  # Indica si la instancia ha sido inicializada

    def _new_(cls):
        """""
        Método especial para implementar el patrón Singleton. 
        Sobrescribe la creación de una nueva instancia para devolver siempre la misma.
        """""
        if cls._instance is None:
            cls.instance = super(UsuarioSingleton, cls).new_(cls)  # Llama al método original de creación de instancia
        return cls._instance  # Devuelve la instancia única

    @classmethod
    def initialize(cls, datos):
        """""
        Inicializa la instancia única con datos de usuario. 
        Llama al UsuarioFactory para crear el usuario.
        Si ya está inicializado, lanza una excepción.
        
        Args:
            datos (dict): Información necesaria para crear un usuario.
        """""
        from factories.usuario_factory import UsuarioFactory  # Importación diferida para evitar dependencias cíclicas

        if cls.is_initialized:
            raise Exception("La instancia ya ha sido inicializada.")  # Previene la inicialización múltiple

        cls._usuario = UsuarioFactory.crear_usuario(datos)  # Crea un usuario utilizando la fábrica
        cls.is_initialized = True  # Marca la instancia como inicializada

    @classmethod
    def get_instance(cls):
        """""
        Devuelve la única instancia del Singleton. 
        Si no existe, la crea.
        
        Returns:
            UsuarioSingleton: Instancia única de la clase.
        """""
        if cls._instance is None:
            cls._instance = cls()  # Crea la instancia si aún no existe
        return cls._instance  # Devuelve la instancia única

    @classmethod
    def destroy(cls):
        """""
        Destruye la instancia del Singleton, reiniciando sus atributos estáticos.
        """""
        cls._usuario = None  # Borra los datos del usuario
        cls._instance = None  # Borra la instancia del Singleton
        cls.is_initialized = False  # Restablece el estado de inicialización

    def es_administrador(self):
        """""
        Comprueba si el usuario almacenado es un administrador.
        
        Returns:
            bool: True si el usuario es administrador, False en caso contrario o si no hay usuario.
        """""
        if self._usuario:
            return self._usuario.es_administrador()  # Llama al método es_administrador del usuario
        return False  # Devuelve False si no hay usuario

    def get_datos(self):
        """""
        Devuelve los datos del usuario actual.
        
        Returns:
            dict: Información del usuario.
        """""
        return self._usuario.get_datos()  # Llama al método get_datos del usuario

    def update_datos(self, cedula, nombre, email, contrasena, ocupacion, privilegios):
        """""
        Actualiza los datos del usuario almacenado.
        
        Args:
            cedula (str): Nueva cédula del usuario.
            nombre (str): Nuevo nombre del usuario.
            email (str): Nuevo correo electrónico del usuario.
            contrasena (str): Nueva contraseña del usuario.
            ocupacion (str): Nueva ocupación del usuario.
            privilegios (list): Nuevos privilegios del usuario.
        """""
        # Actualiza los datos del usuario usando su método
        self._usuario.update_datos(cedula, nombre, email, contrasena, ocupacion, privilegios)  

    def get_cedula(self):
        """""
        Obtiene la cédula del usuario actual.
        
        Returns:
            str: Cédula del usuario.
        """""
        return self._usuario.cedula  # Devuelve la cédula del usuario
