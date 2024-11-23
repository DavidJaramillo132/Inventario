from .elemento import Elemento
# Subclase para elementos de tipo equipo electrónico
class EquipoElectronico(Elemento):
    def getDescripcion(self):
        return f"Equipo electrónico: {self.nombre}, Estado: {self.estado}, Adquirido en: {self.fecha_adquisicion}, Cantidad: {self.cantidad}"

    def getCategoria(self):
        return "Electrodomestico" 