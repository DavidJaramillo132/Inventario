from .factory import Factory
from enums.tipo_equipos_enum import TipoEquipo as TP


class EquipoFactory(Factory):

    # Diccionario que mapea tipos de equipo a sus respectivas clases
    _equipos_map = {
        TP.ELECTRONICO.value: "EquipoElectronico",
        TP.ESCRITORIO.value: "EquipoEscritorio",
        TP.SILLA.value: "EquipoSilla",
        TP.DECORATIVO.value: "EquipoDecorativo",
        TP.HERRAMIENTA.value: "EquipoHerramienta",
        TP.SEGURIDAD.value: "EquipoSeguridad",
        TP.LIMPIEZA.value: "EquipoLimpieza",
        TP.ILUMINACION.value: "EquipoIluminacion",
        TP.OTRO.value: "EquipoOtro",
    }
    
    @staticmethod
    def crear_objeto(*datos):
        tipo_equipo = datos[2]  # Se asume que el tipo de equipo está en la posición 3
        print(tipo_equipo)
        print(datos)
        # Validar si el tipo de equipo existe en el mapeo
        if tipo_equipo not in EquipoFactory._equipos_map:
            print(EquipoFactory._equipos_map)
            raise ValueError(f"Tipo de equipo no válido: {tipo_equipo}")

        # Importar la clase dinámicamente
        module_path = "models.equipos"
        class_name = EquipoFactory._equipos_map[tipo_equipo]
        equipo_class = getattr(__import__(module_path, fromlist=[class_name]), class_name)

        print(f"Creando objeto de tipo {equipo_class.__name__}")
        # Crear y devolver la instancia del equipo
        return equipo_class(*datos)
