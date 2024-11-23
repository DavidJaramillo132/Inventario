

class UsuarioSingleton:
    _instance = None
    usuario = None
    is_initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UsuarioSingleton, cls).__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls, datos: dict):
        from factories.usuario_factory import UsuarioFactory

        if cls.is_initialized:
            raise Exception("La instancia ya ha sido inicializada.")
        
        
        cls.usuario = UsuarioFactory.crear_usuario(datos)
        cls.is_initialized = True

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def destroy(cls):
        cls._instance.usuario = None
        cls._instance = None
        cls.is_initialized = False
        
    
    def es_administrador(self):
        if self._instance.usuario:
            return self._instance.usuario.es_administrador()
        return False

    def get_datos_usuario(self):
        return self._instance.usuario.get_datos_usuario()
    
    def update_usuario(self, cedula, nombre, email, contrasena, ocupacion, privilegios):
        self._instance.usuario.update_datos(cedula, nombre, email, contrasena, ocupacion, privilegios)
    
    def get_cedula(self):
        return self._instance.usuario.cedula

    # def crear_nueva_sala(self, Contenido_principal):
    #     self._instance.crear_nueva_sala(Contenido_principal)

    # def ingresar_usuario(self, contenido_principal):
    #     self._instance.ingresar_usuario(contenido_principal)

    # def modificar_usuario(
    #     self, contenido_principal, cedula, nombre, email, contraseña, rango
    # ):
    #     self._instance.modificar_usuario(
    #         contenido_principal, cedula, nombre, email, contraseña, rango
    #     )

    # def ver_usuario(self, contenido_principal):
    #     self._instance.ver_usuario(contenido_principal)

    # def agregar_elemento_a_aula(self, contenido_principal, id_aula):
    #     self._instance.agregar_elemento_a_aula(contenido_principal, id_aula)

    # def eliminar_elemento(self, contenido_principal, idAula):
    #     self._instance.eliminar_elemento(contenido_principal, idAula)

    # def ver_comentarios(self, contenido_principal, idAula):
    #     self._instance.ver_comentarios(contenido_principal, idAula)

    # # Supervisor
    # def ver_perfil(self, contenido_principal):
    #     self._instance.ver_perfil(contenido_principal)

    # def elementos_de_aula(self, contenido_principal, idAula):
    #     self._instance.elementos_de_aula(contenido_principal, idAula)

    # def ver_comentarios(self, contenido_principal, idAula):
    #     self._instance.ver_comentarios(contenido_principal, idAula)

    # def agregar_comentario(self, idAula, cedula):
    #     self._instance.agregar_comentario(idAula, cedula)

    # def crear_reporte(self, idAula):
    #     self._instance.crear_reporte(idAula)
