from datetime import datetime
import customtkinter as ctk
from tkinter import messagebox

class validaciones:
    def validar_texto(self, entrada):

        if not entrada.isalpha():
            messagebox.showerror("Error", "Solo se acepta palabras validas")
            return None
        return entrada

        
    def validar_email(self, email):
        if "@" not in email or "." not in email: #valida que el email tenga "@" y "."
            messagebox.showerror("Error", "El email debe de tener '@' y '.'")
            return None
        # raise ValueError("El email debe de tmener '@' y '.'") #Si no lo tiene manda este mensaje de error
        return email
                
    def validar_cedula(self, cedula):
        if not cedula.isdigit() or len(cedula) != 10: # Valida que cedula tenga digitos y que no pasen de 10 digitos
            messagebox.showerror("Error","La cédula debe ser un número de 10 dígitos.")
            return None
            # raise ValueError("La cédula debe ser un número de 10 dígitos.")
        return int(cedula)
        
    def validar_numero(self, numero):
        if not numero.isdigit(): # verifica si es un numero
            messagebox.showerror("Error","Solo se debe de colocar numeros")
            return None
            # raise ValueError("Solo se debe de colocar numeros") # si no es un numero manda un mensaje de error 
        return int(numero)

    def validar_fecha(self, fecha):
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error","La fecha debe tener el formato YYYY-MM-DD.")
            return None
            # raise ValueError("La fecha debe tener el formato YYYY-MM-DD.")
        return fecha

    def validar_contrasena(self, contrasena):
        if not any(char.isdigit() for char in contrasena):
            messagebox.showerror("Error", "La contraseña debe contener al menos un número.")
            return None

        if not any(char.isalpha() for char in contrasena):
            messagebox.showerror("Error", "La contraseña debe contener al menos una letra.")
            return None

        return contrasena       
            
            

# def validar_entrada(mensaje, tipo):
#     while True:
#         entrada = input(mensaje) 
#         if tipo == "num" and entrada.isdigit():
#             return int(entrada)
#         else:
#             notificacion = f"Solo se aceptan {('números enteros' if tipo == 'num' else 'texto')}"
#             print(notificacion)



#funciones que noo voy a utilizar
# def obtener_entrada(texto, funcion_validacion):

#     while True:
#         entrada = input(texto) # Solicita el texto que se va a mostrar, el cual va a ser el argumento
#         try:
#             return funcion_validacion(entrada) # Solicita el tipo de validacion que se va a realizar
#         except ValueError as e:
#             print(f"Error: {str(e)}")
#             print("Por favor, intente de nuevo.")
            
    

# def validar_telefono(telefono):
#     if not telefono.isdigit() or len(telefono) != 10: # valida que el numero telefonico contenga numeros y que sea sea igual a 10 digitos
#         raise ValueError("El teléfono debe ser un número de 10 dígitos.") #Si no lo 
#     return telefono
