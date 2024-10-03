class Aula: 
    def __init__(self, tamaño, numeroAula, idAula, tipo):
        self.tamaño = tamaño
        self.numero_Aula = numeroAula
        self.id_Aula = idAula
        self.tipo = tipo
        
    def agregar_elemenmto(self, elemento):
        if elemento.tipo == "mueble":
            print(f"Se ha agregado una mesa y su nombre es: {elemento.nombre}")
        else:
            print(f"El elemento de tipo {elemento.tipo} no se puede agregar en esta aula.")
        pass

    def eliminar_elemento():
        pass
           
        