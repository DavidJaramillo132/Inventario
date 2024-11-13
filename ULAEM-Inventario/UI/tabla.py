import pyodbc
import customtkinter as ctk
# from conexion_db import cursor, conexion
from utilidades.ConfiguraconApp import ConfigurarColores, ConfigararFuentesTexto, UtilidadesParaInterfaz
from UI.notificaciones import Notificaciones_aviso
from Database.querySQL import operacionSQL
from utilidades.singleton import UserSingleton
from utilidades.widget import WidgetCtk


class Tabla:
    def __init__(self):
        self.notificacion = Notificaciones_aviso()
        self.colores = ConfigurarColores()
        self.fuentes = ConfigararFuentesTexto()
        self.utilidades_interfaz = UtilidadesParaInterfaz()
        self.operacionesSQL =  operacionSQL()
        self.usuario = UserSingleton.get_instance()
        self.widget = WidgetCtk()


    def admin_crear_tabla_aula(self, contenido_principal):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        # Crear label de título usando WidgetCtk
        label_register = self.widget.crear_label_titulo_subtitulos(contenido_principal, "Aulas")
        label_register.pack(pady=10)

        # Frame para la tabla de datos usando WidgetCtk
        table_frame = ctk.CTkScrollableFrame(contenido_principal, fg_color=self.colores.obtener_color_principal(), width=580)
        table_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10, anchor="center")

        # Centrar correctamente
        contenido_principal.pack_propagate(False)
        table_frame.pack_configure(anchor="center")

        # Encabezados de columna
        columns = ["ID de Aula", "Tipo", "Funciones"]
        for col in columns:
            label = self.widget.crear_label_texto_normal(table_frame, col)
            label.grid(row=0, column=columns.index(col), padx=5, pady=5)

        resultados = self.operacionesSQL.obtener_aulas()

        # Mostrar datos en la tabla
        for i, (idAula, tipo) in enumerate(resultados, start=1):
            # Mostrar ID de Aula y Tipo
            self.widget.crear_label_texto_normal(table_frame, f"{idAula}").grid(row=i, column=0, padx=5, pady=5)
            self.widget.crear_label_texto_normal(table_frame, f"{tipo}").grid(row=i, column=1, padx=5, pady=5)

            # Botón de "Agregar elemento a aula"
            btn_agregar_elemento = self.widget.crear_boton(
                table_frame,
                "Agregar elemento a aula",
                lambda idAula=idAula: self.usuario.agregar_elemento_a_aula(contenido_principal, idAula)
            )
            btn_agregar_elemento.grid(row=i, column=2, padx=2)

            # Botón de "Ver Elementos"
            btn_eliminar_elemento = self.widget.crear_boton(
                table_frame,
                "Ver Elementos",
                lambda idAula=idAula: self.usuario.eliminar_elemento(contenido_principal, idAula)
            )
            btn_eliminar_elemento.grid(row=i, column=3, padx=2)

            # Botón de "Comentarios"
            btn_ver_comentarios = self.widget.crear_boton(
                table_frame,
                "Comentarios",
                lambda idAula=idAula: self.usuario.ver_comentarios(contenido_principal, idAula)
            )
            btn_ver_comentarios.grid(row=i, column=4, padx=2)

            # Botón de "Eliminar Sala"
            btn_eliminar_sala = self.widget.crear_boton(
                table_frame,
                "Eliminar Sala",
                lambda idAula=idAula: eliminar_sala(contenido_principal, idAula)
            )
            btn_eliminar_sala.grid(row=i, column=5, padx=2)

        def eliminar_sala(contenido_principal, idAula):
            try:
                self.operacionesSQL.eliminar_aula(idAula)
                self.notificacion.show_info("Eliminar", f"El Aula {idAula} fue eliminado correctamente")
                self.admin_crear_tabla_aula(contenido_principal)
            except Exception as e:
                self.notificacion.show_error("Error", f"No se pudo eliminar el aula {idAula}: {e}")

            
    def supervisor_crear_tabla_aula(self, contenido_principal):
        # Limpiar el frame
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        # Crear label de título usando WidgetCtk
        label_register = self.widget.crear_label_titulo_subtitulos(contenido_principal, "Aulas")
        label_register.pack(pady=10)

        # Frame para la tabla de datos usando CTkScrollableFrame (mantiene su creación directa)
        table_frame = ctk.CTkScrollableFrame(contenido_principal, fg_color=self.colores.obtener_color_principal(), width=580)
        table_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10, anchor="center")

        # Centrar correctamente
        contenido_principal.pack_propagate(False)
        table_frame.pack_configure(anchor="center")

        # Encabezados de columna
        columns = ["ID de Aula", "Tamaño", "Tipo", "Funciones"]
        for col in columns:
            label = self.widget.crear_label_texto_normal(table_frame, col)
            label.grid(row=0, column=columns.index(col), padx=5, pady=5)

        # Consulta SQL para obtener datos de aulas
        resultados = self.operacionesSQL.obtener_aulas()

        # Mostrar datos en la tabla
        for i, (idAula, tipo) in enumerate(resultados, start=1):
            # ID de Aula y Tipo
            self.widget.crear_label_texto_normal(table_frame, f"{idAula}").grid(row=i, column=0, padx=5, pady=5)
            self.widget.crear_label_texto_normal(table_frame, f"{tipo}").grid(row=i, column=1, padx=5, pady=5)

            # Botón "Ver elementos"
            btn_ver_elemento = self.widget.crear_boton(
                table_frame,
                "Ver elementos",
                lambda idAula=idAula: self.usuario.elementos_de_aula(contenido_principal, idAula)
            )
            btn_ver_elemento.grid(row=i, column=2, padx=2)

            # Botón "Comentarios"
            btn_agregar_comentario = self.widget.crear_boton(
                table_frame,
                "Comentarios",
                lambda idAula=idAula: self.usuario.ver_comentarios(contenido_principal, idAula)
            )
            btn_agregar_comentario.grid(row=i, column=3, padx=2)

            # Botón "Crear Reporte"
            btn_crear_reporte = self.widget.crear_boton(
                table_frame,
                "Crear Reporte",
                lambda idAula=idAula: self.usuario.crear_reporte(idAula)
            )
            btn_crear_reporte.grid(row=i, column=4, padx=2)
