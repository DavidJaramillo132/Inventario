from tkinter import messagebox
# Clase abstraccion para las notificaciones
class GestorNotificaciones:
    @staticmethod
    def mostrar_info(title, message):
        messagebox.showinfo(title, message)

    @staticmethod
    def mostrar_error(title, message):
        messagebox.showerror(title, message)
        
    @staticmethod
    def mostrar_confirmacion(title, message):
        return messagebox.askokcancel(title, message)