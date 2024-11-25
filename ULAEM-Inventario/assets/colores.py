
# Clase para configuración de colores
class Colores:
    __color_principal = "#111317"
    __color_botones = "#0E4A6B"
    __border_color = "#0D1822"

    @classmethod
    def get_color_principal(cls):
        return cls.__color_principal
    @classmethod
    def get_color_botones(cls):
        return cls.__color_botones
    @classmethod
    def get_border_color(cls):
        return cls.__border_color


