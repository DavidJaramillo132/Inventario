import traceback
from .gestor_notificaciones_gui import GestorNotificaciones


class GestorErrores:

    @staticmethod
    def manejar_error(nombre_funcion, mensaje, exception):

        # Crear mensaje detallado
        error_traceback = traceback.format_exc()
        error_message = f"{mensaje} en {nombre_funcion}:\n{str(exception)}\nDetalles:\n{error_traceback}"
        print(f"Error: {error_message}")


        GestorNotificaciones.mostrar_error(mensaje, str(exception))

    @staticmethod
    def decorador(mensaje=None):
        def wrapper_decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    nombre_funcion = func.__name__
                    GestorErrores.manejar_error(
                        nombre_funcion, mensaje or "Error inesperado", e
                    )

                    return {
                        "error": True,
                        "message": f"{mensaje}: {str(e)}" if mensaje else str(e),
                    }

            return wrapper

        return wrapper_decorator
