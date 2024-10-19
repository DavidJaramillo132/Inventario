import json
from abc import ABC, abstractclassmethod
import lista
import Elemento as claseElemento
import Aula as ClaseAula
import Inventario as ClaseInventario
import validaciones
FILE_PATH = 'aulas_diccionario.json'

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
    
    
    def agregar_elemento_a_aula(self, aula):
        # Permitir al administrador agregar un nuevo elemento a un aula específica
        nombre = validaciones.validar_entrada("Nombre del elemento: ", "str")
        tipo = validaciones.validar_entrada("Tipo de elemento: ", "str")
        estado = validaciones.validar_entrada("Estado del elemento: ", "str")
        fecha_adquisicion = validaciones.validar_entrada("Fecha de adquisición: ", "str")
        cantidad = validaciones.validar_entrada("Cantidad: ", "num")
        id_elemento = validaciones.validar_entrada("ID del elemento: ", "num")
        
        nuevo_elemento = claseElemento.Elemento(nombre,tipo,estado,fecha_adquisicion,cantidad,id_elemento)
        elemento_dict = nuevo_elemento.to_dict()
        


        

        

    def eliminar_elemento():
        pass
    
    def crear_nueva_sala(self):
        # Pedir al administrador que ingrese los detalles de la nueva aula
        size = validaciones.validar_entrada("Tamaño del aula (número de elementos que puede contener): ", "num")
        numero_aula = validaciones.validar_entrada("Número del aula: ", "num")
        id_aula = validaciones.validar_entrada("ID del aula: ", "num")
        tipo = validaciones.validar_entrada("Tipo de aula (clase, laboratorio, etc.): ", "str")

        # Crear una nueva instancia de Aula con los detalles proporcionados
        nueva_aula = ClaseAula.Aula(size, numero_aula, id_aula, tipo)
        # Convertir la instancia de Aula a un diccionario
        aula_dict = nueva_aula.to_dict()

        try:
            with open(FILE_PATH, 'r') as file:
                aulas = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            aulas = []  # Si el archivo no existe o está vacío, iniciamos con una lista vacía
            
        # Añadir el aula actual a la lista de aulas
        aulas.append(aula_dict)
            
        # Guardar la lista actualizada de aulas en el archivo
        with open(FILE_PATH, 'w') as file:
            json.dump(aulas, file, indent=4)
    
        print(f"Aula {numero_aula} de tipo {tipo} creada exitosamente con ID {id_aula} y capacidad de {size}.")


    def eliminar_usuario():
        pass

    def modificar_rol():
        pass
    
    def modificar_capacidad_aula(self, aula):
        # Lógica para modificar la capacidad de un aula específica
        nueva_capacidad = validaciones.validar_entrada("Nueva capacidad del aula: ", "num")
        aula.modificar_capacidad(nueva_capacidad)
        print(f"Capacidad del aula {aula.numero_aula} actualizada a {nueva_capacidad}.")
    
    def modificar_Id_elemento(self, aula, elemento):
        # Lógica para modificar el ID de un elemento en un aula específica
        nuevo_id = validaciones.validar_entrada("Nuevo ID del elemento: ", "num")
        elemento.modificar_id(nuevo_id)
        print(f"ID del elemento {elemento.nombre} en el aula {aula.numero_aula} actualizado a {nuevo_id}.")



