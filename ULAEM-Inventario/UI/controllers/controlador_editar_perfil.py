from UI.gestores import GestorErrores, GestorAutentificacion, GestorNotificaciones
from utils.validador import Validador
from models.usuarios import UsuarioSingleton


class ControladorEditarPerfil:

    @staticmethod
    @GestorErrores.decorador("Error al mostrar la interfaz de editar perfil")
    def mostrar_interfaz_editar_perfil(frame_editar_perfil):
        from UI.views.ventana_principal import InterfazEditarPerfil

        InterfazEditarPerfil.mostrar_editar_perfil(frame_editar_perfil)


    @staticmethod
    def poblar_campos(campos, componentes):
        """
        Pobla los campos con los datos de un usuario existente usando un diccionario.
        """
        usuario = UsuarioSingleton.get_instance()
        datos_usuario = usuario.get_datos(formato="dict")  # Ahora es un dict
        print(datos_usuario)
        print(usuario.get_datos())

        for campo in campos:
            # Verifica si el campo existe en el dict de datos_usuario
            valor = datos_usuario.get(campo)
            if valor is not None:
                componente = componentes.get(campo)
                if componente and hasattr(componente, "set"):
                    componente.set(valor)  # Pobla el componente con el valor
                else:
                    print(
                        f"El componente para {campo} no tiene un método 'set' o no existe"
                    )
            else:
                print(f"No hay valor en 'datos_usuario' para el campo: {campo}")

    @staticmethod
    @GestorErrores.decorador("Error al actualizar el perfil")
    def manejar_actualizar_perfil(
        frame_editar_perfil, cedula, nombre, email, contrasena, ocupacion, privilegios
    ):
        Validador.validar_todos_campos_cuenta(
            cedula, nombre, email, contrasena, ocupacion, privilegios
        )

        if GestorAutentificacion.actualizar_usuario(
            cedula, nombre, email, contrasena, ocupacion, privilegios
        ):
            usuario = UsuarioSingleton.get_instance()
            usuario.update_datos(
                nombre=nombre,
                email=email,
                contrasena=contrasena,
                ocupacion=ocupacion,
                privilegios=privilegios,
            )
            GestorNotificaciones.mostrar_info(
                "Perfil actualizado", "Perfil actualizado con éxito"
            )
            ControladorEditarPerfil.mostrar_interfaz_editar_perfil(frame_editar_perfil)
