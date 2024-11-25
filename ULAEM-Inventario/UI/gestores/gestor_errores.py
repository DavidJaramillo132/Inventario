import traceback
from .gestor_notificaciones_gui import GestorNotificaciones


class GestorErrores:

    @staticmethod
    def manejar_error(nombre_funcion, mensaje, exception):
        """
        nombre_funcion: El nombre de la función donde ocurrió el error.
        mensaje: Un mensaje descriptivo del error.
        exception: La excepción que se produjo.
        FUNCION:
        Crear mensaje detallado
        """
        
        error_traceback = traceback.format_exc()
        error_message = f"{mensaje} en {nombre_funcion}:\n{str(exception)}\nDetalles:\n{error_traceback}"
        print(f"Error: {error_message}")


        GestorNotificaciones.mostrar_error(mensaje, str(exception))

    @staticmethod
    def decorador(mensaje=None):
        """
        mensaje (opcional): Un mensaje personalizado para describir el contexto del error.
        """
        def wrapper_decorator(func):
            """
            func: Es la función que será decorada. la función a la que se aplicará el decorador.
            """
            def wrapper(*args, **kwargs):
                """
                *args, **kwargs: Recibe cualquier número de argumentos para que funcione con cualquier función.
                
                FUNCION: 
                Llama a la funcion, si funciona todo va normalmente, pero si hay un error llama al metodo anterio(manejar_error)
                """
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    nombre_funcion = func.__name__ #__name__: El nombre de la función donde ocurrió el error 
                    GestorErrores.manejar_error(
                        nombre_funcion, mensaje or "Error inesperado", e
                    )

                    return {
                        "error": True,
                        "message": f"{mensaje}: {str(e)}" if mensaje else str(e),
                    }

            return wrapper

        return wrapper_decorator
