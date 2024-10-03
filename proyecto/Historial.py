class Historial: 
    def __init__(self, usuario, fecha, cambios):
        self.usuario = usuario
        self.fecha = fecha
        self.cambios = cambios
        
    def registrar_cambios(self):
        pass
    
    def __eq__(self, otro):
        return self.usuario == otro.usuario and self.fecha == otro.fecha

    def __repr__(self):
        return f"Historial(usuario={self.usuario}, fecha={self.fecha}, cambios={self.cambios})"
