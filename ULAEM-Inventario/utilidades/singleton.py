from UI.Usuario import Administrador, Supervisor


class UserSingleton:
    _instance = None  # almacena la instancia única de UserSingleton

        # metodo para crear una nueva instancia de la clase.
    def __new__(cls):
        # Si _instance es None, significa que aún no existe ninguna instancia.
        if cls._instance is None:
            # Llama al metodo __new__ para crear una instancia.
            cls._instance = super(UserSingleton, cls).__new__(cls)
        # Retorna la instancia única existente.
        return cls._instance
    
    # no dependa de ninguna instancia

    @classmethod
    def initialize(cls, tipo_usuario, cedula, nombre, email, contraseña, rango):
        #  inicializa la instancia con datos especificos del usuario.
        # Verifica si _instance es None, lo que indica que no hay instancia creada.
        if cls._instance is None:
            # Si no hay instancia, lanza una excepción indicando que debe crearse primero con get_instance
            raise Exception("La instancia aún no ha sido creada. Use el método get_instance para obtener la instancia.")
        
        # Inicializa la instancia según el tipo de usuario.
        if tipo_usuario == "Administrador":
            cls._instance = Administrador(cedula, nombre, email, contraseña, rango)
        elif tipo_usuario == "Supervisor":
            cls._instance = Supervisor(cedula, nombre, email, contraseña, rango)
        else:
            raise ValueError("Tipo de usuario no válido: Debe ser 'Administrador' o 'Supervisor'.")

    # no dependa de ninguna instancia
    @classmethod
    def get_instance(cls):
        # Método de clase para obtener la instancia única de UserSingleton.
        # Si _instance es None, significa que la instancia aún no ha sido creada.
        if cls._instance is None:
            # Crea la instancia llamando al constructor de UserSingleton.
            cls._instance = cls()
        # Retorna la instancia única de UserSingleton.
        return cls._instance

    #Retorna los datos del usuario inicializado
    # def obtener_datos_usuario(self):
    #     if hasattr(self, 'usuario'):
    #         return {
    #             'cedula': self.usuario.cedula,
    #             'nombre': self.usuario.nombre,
    #             'email': self.usuario.email,
    #             'rango': self.usuario.rango
    #         }
    #     else:
    #         raise Exception("Usuario no inicializado en UserSingleton.")
        
    # Administrador    
        
    def crear_nueva_sala(self, Contenido_principal):
        self._instance.crear_nueva_sala(Contenido_principal)
        
    def ingresar_usuario(self, contenido_principal):
        self._instance.ingresar_usuario(contenido_principal)
    
    def modificar_usuario(self, contenido_principal, cedula, nombre, email, contraseña, rango):
        self._instance.modificar_usuario(contenido_principal, cedula, nombre, email, contraseña, rango)
        
    def ver_usuario(self, contenido_principal): 
        self._instance.ver_usuario(contenido_principal)
    
    def agregar_elemento_a_aula(self, contenido_principal, id_aula):
        self._instance.agregar_elemento_a_aula(contenido_principal, id_aula)

    def eliminar_elemento(self,contenido_principal, idAula):
        self._instance.eliminar_elemento(contenido_principal, idAula)
        
    def ver_comentarios(self, contenido_principal,idAula):
        self._instance.ver_comentarios(contenido_principal,idAula)


    # Supervisor
    def ver_perfil(self, contenido_principal):
        self._instance.ver_perfil(contenido_principal)
        
    def elementos_de_aula(self, contenido_principal, idAula):
        self._instance.elementos_de_aula(contenido_principal, idAula)
    
    def ver_comentarios(self, contenido_principal, idAula):
        self._instance.ver_comentarios(contenido_principal, idAula)
        
    def agregar_comentario(self, idAula, cedula):
        self._instance.agregar_comentario(idAula, cedula)
        
    def crear_reporte(self, idAula):
        self._instance.crear_reporte(idAula)
        
    

# def singleton(cls):
#     isinstances = dict()
    
#     def wrap():
#         if cls not in isinstances:
#             isinstances[cls] = cls(*args, **kwargs)
        
#         return isinstances[cls]
#     return wrap

# @singleton
# class UserSingleton(object):
#     def __init__(self,nombre):
#         self.nombre = nombre


# user1 = UserSingleton("David")
# user2 = UserSingleton("Javier")
    
# print(user1 is user2)