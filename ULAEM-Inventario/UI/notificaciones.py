from tkinter import messagebox
# Clase abstraccion para las notificaciones
class Notificaciones_aviso:
    @staticmethod
    def show_info(title, message):
        messagebox.showinfo(title, message)

    @staticmethod
    def show_error(title, message):
        messagebox.showerror(title, message)