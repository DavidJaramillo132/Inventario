import customtkinter as ctk



class Subtabla:
    def __init__(self, frame_padre, columnas):
        self.columnas = columnas
        self.frame_padre = frame_padre
        self.cabezera()

    def cabezera(self):
        for col_index, col_name in enumerate(self.columnas):
            label = ctk.CTkLabel(self.frame_padre, text=col_name, width=80)
            label.grid(row=0, column=col_index, padx=5, pady=5)

    def agregar_fila(self, fila_nombres):
        # Para cada elemento en la fila, crea una etiqueta en la columna correspondiente
        filas = self.frame_padre.grid_size()[1]  # Empieza en la siguiente fila disponible
        for columnas, item in enumerate(fila_nombres):
            label = ctk.CTkLabel(self.frame_padre, text=str(item), width=80)
            label.grid(row=filas, column=columnas, padx=5, pady=5)
