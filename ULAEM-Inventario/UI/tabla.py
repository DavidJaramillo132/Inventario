import pyodbc
import customtkinter as ctk
# from conexion_db import cursor, conexion
from utilidades.ConfiguraconApp import ConfigurarColores, ConfigararFuentesTexto, UtilidadesParaInterfaz
from UI.notificaciones import Notificaciones_aviso
from Database.querySQL import operacionSQL
from utilidades.singleton import UserSingleton

class Tabla:
    def __init__(self):
        self.notificacion = Notificaciones_aviso()
        self.colores = ConfigurarColores()
        self.fuentes = ConfigararFuentesTexto()
        self.utilidades_interfaz = UtilidadesParaInterfaz()
        self.operacionesSQL =  operacionSQL()
        self.usuario = UserSingleton.get_instance()

    def admin_crear_tabla_aula(self, contenido_principal):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        
        label_register = ctk.CTkLabel(contenido_principal, text="Aulas", font=self.fuentes.obtener_fuente_titulos_subtitulos())
        label_register.pack(pady=10)

        # Frame para la tabla de datos
        table_frame = ctk.CTkScrollableFrame(contenido_principal, fg_color=self.colores.obtener_color_principal(), width=580)
        table_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10,anchor="center")

        #Centrar correctamente
        contenido_principal.pack_propagate(False)
        table_frame.pack_configure(anchor="center")
        # Encabezados de columna
        columns = ["ID de Aula", "Tipo", "Funciones"]
        for col in columns:
            label = ctk.CTkLabel(table_frame, text=col, width=80)
            label.grid(row=0, column=columns.index(col), padx=5, pady=5)


        resultados = self.operacionesSQL.obtener_aulas()

        # Mostrar datos en la tabla
        for i, (idAula, tipo) in enumerate(resultados, start=1):
            # admin = claseUsuario.Administrador("1315844983","admin", "admin@example.com", "contra", "admin")  # ADMIN YA INSTANCIADO

            ctk.CTkLabel(table_frame, text=f"{idAula}", width=80).grid(row=i, column=0, padx=5, pady=5)
            # ctk.CTkLabel(table_frame, text=f"{tamaño}", width=80).grid(row=i, column=1, padx=5, pady=5)
            ctk.CTkLabel(table_frame, text=f"{tipo}", width=80).grid(row=i, column=1, padx=5, pady=5)

            # Botones de acción
            btn_agregar_elemento = ctk.CTkButton(table_frame, text="Agregar elemento a aula", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                command=lambda idAula=idAula: self.usuario.agregar_elemento_a_aula(contenido_principal, idAula)
            )            
            btn_agregar_elemento.grid(row=i, column=2, padx=2)
            
            btn_eliminar_elemento = ctk.CTkButton(table_frame, text="Ver Elementos", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                command=lambda idAula=idAula: self.usuario.eliminar_elemento(contenido_principal, idAula)
            )
            btn_eliminar_elemento.grid(row=i, column=3, padx=2)
            
            btn_ver_comentarios = ctk.CTkButton(table_frame, text="Comentarios", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                command=lambda idAula=idAula: self.usuario.ver_comentarios(contenido_principal,idAula)
            )
            btn_ver_comentarios.grid(row=i, column=4, padx=2)
            btn_ver_comentarios = ctk.CTkButton(table_frame, text="Eliminar Sala", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                command=lambda idAula=idAula: eliminar_sala(contenido_principal, idAula)
            )
            btn_ver_comentarios.grid(row=i, column=5, padx=2)

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

        label_register = ctk.CTkLabel(contenido_principal, text="Aulas", font=self.fuentes.obtener_fuente_titulos_subtitulos())
        label_register.pack(pady=10)

        # Frame para la tabla de datos
        table_frame = ctk.CTkScrollableFrame(contenido_principal, fg_color=self.colores.obtener_color_principal(), width=580)
        table_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10,anchor="center")

        #Centrar correctamente
        contenido_principal.pack_propagate(False)
        table_frame.pack_configure(anchor="center")
        # Encabezados de columna
        columns = ["ID de Aula", "Tamaño", "Tipo", "Funciones"]
        for col in columns:
            label = ctk.CTkLabel(table_frame, text=col, width=80)
            label.grid(row=0, column=columns.index(col), padx=5, pady=5)

        # Consulta SQL
        resultados = self.operacionesSQL.obtener_aulas()

        # Mostrar datos en la tabla
        for i, (idAula, tipo) in enumerate(resultados, start=1):
            # supervi = claseUsuario.Supervisor("1315844983","admin", "admin@example.com", "contra", "admin")  # ADMIN YA INSTANCIADO

            ctk.CTkLabel(table_frame, text=f"{idAula}", width=80).grid(row=i, column=0, padx=5, pady=5)
            ctk.CTkLabel(table_frame, text=f"{tipo}", width=80).grid(row=i, column=1, padx=5, pady=5)

            # Botones de acción
            btn_ver_elemento = ctk.CTkButton(table_frame, text="Ver elementos", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                command=lambda idAula=idAula: self.usuario.elementos_de_aula(contenido_principal,idAula)
            )            
            btn_ver_elemento.grid(row=i, column=2, padx=2)
            
            btn_agregar_comentario = ctk.CTkButton(table_frame, text="Comentarios", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                command=lambda idAula=idAula: self.usuario.ver_comentarios(contenido_principal, idAula)
            )
            btn_agregar_comentario.grid(row=i, column=3, padx=2)
            
            btn_crear_reporte = ctk.CTkButton(table_frame, text="Crear Reporte", fg_color=self.colores.obtener_color_principal(), hover_color=self.colores.obtener_color_botones(),
                command=lambda idAula=idAula: self.usuario.crear_reporte(idAula)
            )
            btn_crear_reporte.grid(row=i, column=4, padx=2)
            