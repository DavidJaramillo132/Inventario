from .usuario import Usuario

class UsuarioAdministrador(Usuario):
    def __init__(self, cedula, nombre, email, contrasena, ocupacion, privilegios):
        super().__init__(cedula, nombre, email, contrasena, ocupacion, privilegios)
        
    
    def es_administrador(self):
        return True