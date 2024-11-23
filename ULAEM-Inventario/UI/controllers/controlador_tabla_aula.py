from UI.gestores import GestorErrores, GestorNotificaciones

class ControladorTablaAula:
    @staticmethod
    def mostrar_interfaz_tabla_aulas(root,frame_principal):
        from UI.views.ventana_principal.tablas import TablaAula
        
        TablaAula.mostrar_interfaz_tabla_aulas(root,frame_principal)
    
    
    @staticmethod
    def mostrar_interfaz_agregar_elemento_aula(root, idaula):
        from UI.controllers import ControladorAgregarElemento
        
        ControladorAgregarElemento.mostrar_interfaz_agregar_elemento(root,idaula)

    @staticmethod 
    def mostrar_interfaz_ver_elementos(root, idaula):
        from UI.controllers import ControladorTablaElemento
        
        ControladorTablaElemento.mostrar_interfaz_tabla_usuarios(root,idaula)
    
    @staticmethod
    def mostrar_interfaz_ver_comentarios(root,frame_principal, idaula):
        from UI.controllers import ControladorTablaComentario
        
        ControladorTablaComentario.mostrar_interfaz_tabla_comentarios(root,idaula)

    @staticmethod
    def mostrar_interfaz_agregar_comentario(root, idaula):
        from UI.controllers import ControladorAgregarComentario
        
        ControladorAgregarComentario.mostrar_interfaz_agregar_comentario(root,idaula)

    

    @staticmethod
    @GestorErrores.decorador("Error al generar el reporte")
    def generar_reporte(idAula):
        from UI.gestores import GestorReportes

        if GestorReportes.generar_reporte_aula(idAula):
            GestorNotificaciones.mostrar_info("Reporte generado","Reporte generado con éxito")
