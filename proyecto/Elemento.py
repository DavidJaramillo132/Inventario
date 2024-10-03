class Elemento: 
    def __init__(self, nombre, tipo, estado, fechaAdquisicion, cantidad, idAula, idElemento):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado
        self.fechaAdquisicion = fechaAdquisicion
        self.cantidad = cantidad
        self.idAula = idAula
        self.idElemento = idElemento
        
    def __add__(self, otro):
        if self.tipo == otro.tipo:
            return Elemento(
                self.nombre,
                self.tipo,
                self.estado,
                self.fechaAdquisicion,
                self.cantidad + otro.cantidad,
                self.idAula,
                self.idElemento
            )
        else:
            print("No se pueden sumar elementos de diferente tipo.")

    def __repr__(self):
        return f"Elemento(nombre={self.nombre}, tipo={self.tipo}, cantidad={self.cantidad})"
  