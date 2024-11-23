from utils.validador import Validador
from database import GestorServicioSQL
from UI.gestores import GestorErrores, GestorNotificaciones
from models.usuarios import UsuarioSingleton

class ControladorAgregarComentario:
    @staticmethod
    @GestorErrores.decorador("Error al mostrar la interfaz de agregar comentario")
    def mostrar_interfaz_agregar_comentario(frame_principal, idAula):
        from UI.views.ventana_principal import InterfazAgregarComentario

        InterfazAgregarComentario.mostrar_interfaz_agregar_comentario(
            frame_principal, idAula
        )

    @staticmethod
    @GestorErrores.decorador("Error al agregar el comentario")
    def manejar_agregar_comentario(frame, contenido, idAula):
        print(contenido)
        contenido = contenido.strip()
        print(contenido)
        Validador.validar_todos_campos_comentarios(contenido, idAula)
        usuario = UsuarioSingleton.get_instance()
        cedula = usuario.get_cedula()

        GestorServicioSQL.crear_comentario(contenido, idAula,cedula)
        GestorNotificaciones.mostrar_info(
            "Comentario agregado", "El comentario ha sido agregado correctamente"
        )

        frame.destroy()
