from abc import ABC, abstractclassmethod
class Usuario: 
    def __init__(self, nombre, email, contraseña, rango):
        self.nombre = nombre
        self._email = email
        self.__contraseña = contraseña
        self.rango = rango
        
    @property
    def contraseña(self):
        return self.__contraseña
    # aplicar clase extracta
    @abstractclassmethod
    def iniciarSesion(self):       
        pass

    def seleccionar_curso(self, curso):
        print(f"{self.nombre} ha seleccionado el curso: {curso}")

    def seleccionar_elemento(self, elemento):
        print(f"{self.nombre} ha seleccionado el elemento: {elemento}")

    def consultar_inventario(self):
        print(f"{self.nombre} esta consultando el inventario.")

    def visualizar_historial(self):
        print(f"{self.nombre} esta visualizando su historial.")

    def dejar_comentario(self, comentario):
        print(f"{self.nombre} ha dejado el comentario: {comentario}")
        

class Supervisor(Usuario):
    def __init__(self, nombre, email, contraseña,rango, departamento):
        super().__init__(nombre, email, contraseña,rango)
        self.departamento = departamento
        
    def iniciar_sesion(self):
        print(f"Supervisor {self.nombre} ha iniciado sesión en el departamento {self.departamento}.")
    def ver_historial_dereporte():
        pass
    
    def ver_comentarios():
        pass

    def editar_estado_de_elemento():
        pass

    def crear_reporte():
        pass 

    def eliminar_comentario():
        pass

    def modificar_elemento():
        pass

class Administrador(Usuario):

    def iniciar_sesion(self):
        print(f"Administrador {self.nombre} ha iniciado sesión con privilegios completos.")
    def ver_reporte():
        pass
    def eliminar_reporte():
        pass
    def agregar_elemento():
        pass
    def eliminar_elemento():
        pass
    def crear_nueva_sala():
        pass

    def eliminar_usuario():
        pass

    def modificar_rol():
        pass
    def modificar_capacidad_aula():
        pass
    def modificar_Id_elemento():
        pass


# print(Supervisor.__base__)
# print(Usuario.__subclasses__())

juan= Supervisor("juan", "j@j.com", "1234", "Supervisor", "Sistemas")
admin = Administrador("admin", "a@a.com", "1234", "Administrador")

juan.iniciar_sesion()
admin.iniciar_sesion()
