import customtkinter as ctk
from .custom_entry import EntryPersonalizado
from .label_titulo_subtitulo import LabelTituloSubtitulo

class EntryLabel(ctk.CTkFrame):
    def __init__(self, parent, texto,grid=False,row=0, *args, **kwargs):

        super().__init__(parent, fg_color="transparent", *args, **kwargs)

        self.label = LabelTituloSubtitulo(self, texto)

        self.entry = EntryPersonalizado(self)
        if grid:
            self.entry.grid(row=row, column=1)
        else:
            
            self.label.pack(pady=10)
            self.entry.pack(pady=10)
        
        

    def get(self):
        return self.entry.get()
    
    def set(self, valor):
        self.entry.insert(0, valor)
    
    def clear(self):
        self.entry.delete(0, "end")

