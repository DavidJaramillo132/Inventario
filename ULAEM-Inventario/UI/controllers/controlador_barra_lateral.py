from UI.gestores import GestorNotificaciones
from models.usuarios import UsuarioSingleton



class ControladorBarraLateral:
    
    @staticmethod
    def mostrar_interfaz_editar_perfil(frame_principal):
        from UI.controllers import ControladorEditarPerfil

        ControladorEditarPerfil.mostrar_interfaz_editar_perfil(frame_principal)
    
    @staticmethod
    def mostrar_interfaz_tabla_aulas(root,frame_principal):
        from UI.controllers import ControladorTablaAula
        
        ControladorTablaAula.mostrar_interfaz_tabla_aulas(root,frame_principal)

    @staticmethod
    def mostrar_interfaz_tabla_usuarios(root,frame_principal):
        from UI.controllers import ControladorTablaUsuario
        
        ControladorTablaUsuario.mostrar_interfaz_tabla_usuarios(root,frame_principal)
    
    @staticmethod
    def mostrar_interfaz_crear_nuevas_salas(frame_principal):
        from UI.controllers import ControladorCrearSala
        
        ControladorCrearSala.mostrar_interfaz_crear_sala(frame_principal)
    
    
    @staticmethod
    def mostrar_interfaz_register(frame_principal):
        from UI.controllers import ControladorRegister
        
        ControladorRegister.mostrar_interfaz_register(frame_principal)
    
    @staticmethod
    def confirmar_cerrar_sesion(root):
        from UI.views.inicio_sesion import InterfazLogin

        if GestorNotificaciones.mostrar_confirmacion(
            "Cerrar sesión", "¿Está seguro que desea cerrar sesión?"
        ):
            UsuarioSingleton().get_instance().destroy()
            InterfazLogin.mostrar_interfaz_login(root)
