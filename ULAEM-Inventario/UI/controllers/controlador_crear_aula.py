from utils.validador import Validador
from database import GestorServicioSQL
from UI.gestores import GestorErrores, GestorNotificaciones
class ControladorCrearSala:
    @staticmethod
    @GestorErrores.decorador("Error al mostrar la creación de una sala")
    def mostrar_interfaz_crear_sala(frame_principal):
        from UI.views.ventana_principal import InterfazCrearNuevaSala
        InterfazCrearNuevaSala.mostrar_interfaz_crear_sala(frame_principal)
    
    @staticmethod
    @GestorErrores.decorador("Error al crear la sala")
    def manejar_crear_nueva_sala(dimensiones,tipo):
        Validador.validar_todos_campos_sala(dimensiones, tipo)
        
        GestorServicioSQL.crear_aula(dimensiones, tipo)
        GestorNotificaciones.mostrar_info("Sala creada", "La sala ha sido creada correctamente")
        
        