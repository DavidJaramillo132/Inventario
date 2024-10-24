import Aula
import Elemento
import Inventario as claseInventario
import Usuario as claseUsuario
import Historial
import lista 
import validaciones

#Estoy desde la raiz David
# esti es un pull request


# Funciones de practica
def ingresar_usuario():
    cantidad_usuario = validaciones.validar_entrada("Cuantos estudiantes desea ingresar? ", "num")
    for i in range(cantidad_usuario):
        nombre_usuario = validaciones.validar_entrada("Ingrese el nombre: ", "str")
        email_usuario = validaciones.validar_entrada("Ingrese el email: ", "str")
        contraseña_usuario = validaciones.validar_entrada("Ingrese la contrasea ", "str")
        rango_usuario = validaciones.validar_entrada("Ingrese el rango: ", "str")
        lista.usuarios_diccionario.append({"nombre": nombre_usuario,"email":email_usuario,"contraseña": contraseña_usuario,"rango":rango_usuario })
        
   
def ver_usuarios():
    for claseUsuario.Usuario in lista.usuarios_diccionario:
        i = 1
        print(f"{i} {claseUsuario.Usuario["nombre"]}")
        i += 1




def opciones_admin():
    while True:
        print("\n0. Salir",
            "1. Crear nueva sala",
            "2. agregar_elemento_a_aula",
            "3. ingresar usuarios",
            "4. ver_usuarios",
            sep="\n")
        
        opcion = validaciones.validar_entrada("Seleccionar opcion","num")
        if opcion == 0:
            print("Gracias por usar el Sistema de Atención Médica. ¡Hasta luego!")
            break
        
        try:
            
            if opcion == 1:
                claseUsuario.Administrador.crear_nueva_sala(claseUsuario.Administrador)
            elif opcion == 2:
                print("por definir")
            elif opcion == 3:
                claseUsuario.Administrador.agregar_elemento_a_aula(claseUsuario.Administrador, )
            elif opcion == 4:
                print("por definir")
            elif opcion == 5:
                ingresar_usuario()
            elif opcion == 6:
                print("Por definir")
            elif opcion == 7:
                return
            elif opcion == 8:
                ver_usuarios()
            else:
                print("Pueda nada")
        except Exception as e: 
            print(f"Error: {str(e)}")
    
    
    
    
    
    
def opciones_supervisor():
    while True:
        opcion = validaciones.validar_entrada(""" 
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

def main():
    validaciones.imprimir_encabezado("Sistema de gestion de Inventario")
    print("\n0. Salir",
            "1. administrador",
            "2. supervisor",
            sep="\n")

    while True:
        opcion = validaciones.validar_entrada("\nEliga una opcion: ", "num")
        try:
            if opcion == 1:
                opciones_admin()
            elif opcion == 2:
                opciones_supervisor()
        except Exception as e:
            print("INGRESE UN VALOR CORRECTO")
            
    
    
main()


