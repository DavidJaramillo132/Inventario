from UI.gestores import GestorErrores, GestorAutentificacion, GestorNotificaciones
from utils.validador import Validador
from database import GestorServicioSQL


class ControladorEditarElemento:

    @staticmethod
    @GestorErrores.decorador("Error al mostrar la interfaz de editar elemento ")
    def mostrar_interfaz_editar_elemento(root,frame_tabla_elemento, elemento):
        from UI.views.ventana_principal import InterfazEditarElemento

        InterfazEditarElemento.mostrar_interfaz_editar_elemento(root,frame_tabla_elemento, elemento)

    @staticmethod
    def poblar_campos(campos, componentes, elemento):
        """
        Pobla los campos con los datos de un usuario existente.
        """
        datos_elemento = elemento.get_datos()[1:]

        for campo, valor in zip(campos, datos_elemento):
            componente = componentes.get(campo)
            if componente and hasattr(componente, "set"):
                componente.set(valor)
            else:
                print(
                    f"El componente para {campo} no tiene un método 'set' o no existe"
                )

    
    @staticmethod
    @GestorErrores.decorador("Error al actualizar el perfil")
    def manejar_editar_elemento(
        frame_editar_elemento,
        frame_tabla_elemento,
        root,
        nuevo_nombre,
        nuevo_tipo,
        nuevo_estado,
        nuevo_fecha_adquisicion,
        nuevo_cantidad,
        elemento,
    ):
        id_elemento = elemento.get_idElemento()
        id_aula = elemento.get_idAula()
        Validador.validar_todos_campos_elementos(
            nuevo_nombre,
            nuevo_tipo,
            nuevo_estado,
            nuevo_fecha_adquisicion,
            nuevo_cantidad,
            id_elemento,
        )
        GestorServicioSQL.actualizar_elemento(
            id_elemento,
            nuevo_nombre,
            nuevo_tipo,
            nuevo_estado,
            nuevo_fecha_adquisicion,
            nuevo_cantidad,
        )

        GestorNotificaciones.mostrar_info(
            "Elemento editado", "Se ha editado el elemento exitosamente"
        )
        from UI.controllers import ControladorTablaElemento

        frame_tabla_elemento.destroy()
        frame_editar_elemento.destroy()
        ControladorTablaElemento.mostrar_interfaz_tabla_elementos(root, id_aula)
