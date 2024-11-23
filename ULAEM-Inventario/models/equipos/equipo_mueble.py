from .elemento import Elemento
# Subclase para elementos de tipo mobiliario
class EquipoMueble(Elemento):
    def get_descripcion(self):
        return f"Mobiliario: {self.nombre}, Estado: {self.estado}, Adquirido en: {self.fecha_adquisicion}, Cantidad: {self.cantidad}"

    def get_categoria(self):
        return "Mueble"  # Implementación específica para el tipo