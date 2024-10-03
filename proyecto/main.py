import Aula
import Elemento
import Inventario
import Usuario
import Historial

usuarios = []

def validar_entrada(mensaje, tipo):
    while True:
        entrada = input(mensaje) 
        if tipo == "num" and entrada.isdigit():
            return int(entrada)
        elif tipo == "str" and not entrada.isdigit():
            return entrada.title().strip()
        else:
            notificacion = f"Solo se aceptan {('números enteros' if tipo == 'num' else 'texto')}"
            print(notificacion)

# usuarios del sistema    
usuario1 = Usuario.Usuario("David", "djdavidjaramillo@gmail.com", "12345", "Estudiante")
usuario2 = Usuario.Usuario("Diego", "diegocasanova@gmail.com", "6789", "Estudiante")
usuario3 = Usuario.Usuario("Justin", "justin@gmail.com", "123456", "Profesor")
# Aula
aula1 = Aula.Aula("4x4", "1", "#001", "Laboratorio")
# sobre carga de la clase elemento
elemento0 = Elemento.Elemento("mesa_estudiante", "mueble","buen estado", "ayer", 7, "#001","#001")
elemento1 = Elemento.Elemento("Mesa", "mueble", "buen estado", "2024-09-21", 5, "#001", "#001")
elemento2 = Elemento.Elemento("Mesa", "mueble", "buen estado", "2024-09-21", 3, "#001", "#002")
nuevo_elemento = elemento1 + elemento2  
print(nuevo_elemento)  


# sobre carga de la clase historial
historial1 = Historial.Historial(usuario1, "2024-09-21", "Actualizacion del inventario")
historial2 = Historial.Historial(usuario1, "2024-09-21", "Cambio en el sistema")
historial3 = Historial.Historial(usuario2, "2024-09-21", "Modificacion de elementos")


print(historial1 == historial2)  
print(historial1 == historial3) 
print(historial1)


# Funciones de practica
def ingresar_usuario():
    cantidad_usuario = validar_entrada("Cuantos estudiantes desea ingresar? ", "num")
    for i in range(cantidad_usuario):
        nombre_usuario = validar_entrada("Ingrese el nombre: ", "str")
        email_usuario = validar_entrada("Ingrese el email: ", "str")
        contraseña_usuario = validar_entrada("Ingrese la contrasea ", "str")
        rango_usuario = validar_entrada("Ingrese el rango: ", "str")
        usuarios.append({"nombre": nombre_usuario,"email":email_usuario,"contraseña": contraseña_usuario,"rango":rango_usuario })
        
   
def ver_usuarios():
    for Usuario.Usuario in usuarios:
        i = 1
        print(f"{i} {Usuario.Usuario["nombre"]}")
        i += 1

def main():
    while True:
        opcion = validar_entrada(""" 
            Que desea hacer en el sistema
            1. Agregar aula
            2. eliminar aula
            3. Agregar elemento
            4. Eliminar elemento
            5. Agregar Usuario.Usuario
            6. Eliminar Usuario.Usuario""","num")
        
        if opcion == 1:
            print("Por definir")
        elif opcion == 2:
            print("por definir")
        elif opcion == 3:
            print("por definir")
        elif opcion == 4:
            print("por definir")
        elif opcion == 5:
            ingresar_usuario()
        elif opcion == 6:
            print("Por definir")
        else:
            print("Pueda nada")
                
        

main()

"""No tomar en cuenta"""
# def visualizar_inventario():
#     while True:
#         print("\n1. Aula 201\n2. Aula 202\n3. Aula 203\n4. Aula 204\n5. Salir")
#         opcion_aula = int(input("Elija un aula: "))
        
#         if opcion_aula == 1:
#             print("\nElija el tipo de inventario: \n1. Muebles 201\n2. Electrónicos 201")
#             opcion_inventario = int(input("Seleccione una opción: "))
#             if opcion_inventario == 1:
#                 print("Has seleccionado Muebles 201.")
#             elif opcion_inventario == 2:
#                 print("Has seleccionado Electrónicos 201.")
#         elif opcion_aula == 2:
#             print("\nElija el tipo de inventario: \n1. Muebles 202\n2. Electrónicos 202")
#             opcion_inventario = int(input("Seleccione una opción: "))
#             if opcion_inventario == 1:
#                 print("Has seleccionado Muebles 202.")
#             elif opcion_inventario == 2:
#                 print("Has seleccionado Electrónicos 202.")
#         elif opcion_aula == 5:
#             print("Saliendo del programa.")
#             break
#         else:
#             print("Opción no válida, intente de nuevo.")


# visualizar_inventario()