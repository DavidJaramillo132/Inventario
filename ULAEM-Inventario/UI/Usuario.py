import customtkinter as ctk
from fpdf import FPDF
from tkcalendar import Calendar
import tkinter as tk
from abc import ABC, abstractclassmethod
from  utilidades.validaciones import validaciones
from utilidades.ConfiguraconApp import ConfigurarColores, ConfigararFuentesTexto, UtilidadesParaInterfaz
from UI.notificaciones import Notificaciones_aviso
# from UI.navegacion import Navegacion
from Database.querySQL import operacionSQL
from UI.subtablas import Subtabla
from UI.Elemento import ElementoFactory
from utilidades.widget import WidgetCtk


class InterfazUsuario(ABC): 
    def __init__(self, cedula, nombre, email, contraseña, rango):
        self.cedula = cedula
        self.nombre = nombre
        self._email = email
        self.__contraseña = contraseña
        self.rango = rango
        self.frame_principal = None  # Referencia a frame principal para que no haga error al limpiar una ventana 
        self.colores = ConfigurarColores()
        self.fuentes = ConfigararFuentesTexto()
        self.utilidades_interfaz = UtilidadesParaInterfaz()
        self.validar = validaciones()
        self.notificacion = Notificaciones_aviso()
        self.operacionesSQL = operacionSQL()
        self.factory = ElementoFactory()
        self.widget = WidgetCtk()

    @property
    def contraseña(self):
        return self.__contraseña
    

    @abstractclassmethod
    def ver_comentarios(self):
        pass


class Supervisor(InterfazUsuario):
    def __init__(self, cedula, nombre, email, contraseña, rango):
        super().__init__(cedula, nombre, email, contraseña, rango)
        
            
    def elementos_de_aula(self, contenido_principal, idAula):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        # Frame para la tabla de datos
        table_frame = self.widget.crear_scrollable_frame(contenido_principal)
        table_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10, anchor="center")
        table_frame.pack_configure(anchor="center")
        
        resultados = self.operacionesSQL.obtener_elementos_por_idaula(idAula)
        
        # Encabezados de columna
        columnas_nombre = ["nombre", "tipo", "estado", "fechAdquisicion", "cantidad"]
        tabla = Subtabla(table_frame, columnas_nombre)
                    
        for (nombre, tipo, estado, fechAdquisicion, cantidad, idAula, IdElemento) in resultados:
            # Crear instancia del elemento usando la fábrica
            elemento = self.factory.crear_elemento(tipo, nombre, estado, fechAdquisicion, cantidad, IdElemento)

            # Crear una lista con los datos de la fila
            fila_datos = [nombre, tipo, estado, fechAdquisicion, cantidad]
            tabla.agregar_fila(fila_datos)

            # boton para mostrar la descripción del elemento
            btn_descripcion = self.widget.crear_boton(table_frame, "Descripcion",
                hover_color=self.colores.obtener_color_botones(),
                command=lambda elemento=elemento: mostrar_descripcion(elemento)
            )
            # Posicionar el botón de "Descripcion" en la columna de acciones
            btn_descripcion.grid(row=tabla.frame_padre.grid_size()[1] - 1, column=6, padx=2)

        def mostrar_descripcion(elemento):
            # Mostrar la información del elemento (puedes usar un diálogo o etiqueta)
            descripcion = elemento.descripcion()
            self.notificacion.show_info("Descripcion", descripcion)  # Aquí podrías mostrarlo en la interfaz, en vez de imprimirlo
        # Aquí podrías mostrarlo en la interfaz, en vez de imprimirlo


    def ver_comentarios(self, contenido_principal, idAula):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        # freme_princial = self.widget.crear_frame(contenido_principal)
        # freme_princial.pack(pady = 5,expand=True, anchor="center")
        # Frame para la tabla de datos
        table_frame = self.widget.crear_scrollable_frame(contenido_principal)
        table_frame.pack(side="top", fill="both", expand=True, padx=10, pady=10, anchor="center")
        table_frame.pack_configure(anchor="center")

        # Encabezados de columna
        columnas_nombre = ["Comentario", "fecha de creacion"]
        tabla = Subtabla(table_frame, columnas_nombre)

        resultados = self.operacionesSQL.comentario(idAula)
        
        for i, columnas_nombre in enumerate(resultados, start=1):
            tabla.agregar_fila(columnas_nombre)

        # Botón para agregar comentarios
        btn_comentario = self.widget.crear_boton(table_frame, "Agregar Comentarios",
                                    lambda: self.agregar_comentario(idAula, contenido_principal))
        btn_comentario.grid(row=len(resultados) + 1, column=0, columnspan=3, padx=2, pady=5) 


    def agregar_comentario(self, idAula, contenido_principal):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        comentario_frame = self.widget.crear_scrollable_frame(contenido_principal)
        comentario_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        label_comentario = self.widget.crear_label_titulo_subtitulos(comentario_frame, "Comentario")
        label_comentario.pack(pady=10)

        entry_comentario = self.widget.crear_entry(comentario_frame, False)
        entry_comentario.pack(padx=10, pady=10)

        def agregar(contenido_principal, idAula):
            comentario = entry_comentario.get()
            # Insertar comentario en la base de datos
            self.operacionesSQL.insertar_comentaraio(comentario, idAula, self.cedula)
            # Limpiar campo despues de insertar
            entry_comentario.delete(0, ctk.END)
            self.ver_comentarios(contenido_principal, idAula)

        # Boton para agregar un comentario a la base de datos
        button_crear_comentario = self.widget.crear_boton(comentario_frame, "Agregar comentario", 
                                            lambda: agregar(contenido_principal, idAula))
        button_crear_comentario.pack(pady=20)  

    
    def ver_perfil(self, contenido_principal):
        # Limpia la ventana principal de contenido previo
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        self.widget.crear_label_titulo_subtitulos(contenido_principal, "Perfil de Usuario").pack(pady=10)

            # Entrada para nombre
        self.widget.crear_label_texto_normal(contenido_principal, "Nombre del usuario").pack()
        entry_nombre = self.widget.crear_entry(contenido_principal, False)
        entry_nombre.insert(0, self.nombre)
        entry_nombre.configure(state="readonly")
        entry_nombre.pack(pady=5)

            # Entrada para email
        self.widget.crear_label_texto_normal(contenido_principal, "Email").pack()
        entry_email = self.widget.crear_entry(contenido_principal, False)
        entry_email.insert(0, self._email)
        entry_email.configure(state="readonly")
        entry_email.pack(pady=5)

            # Entrada para contraseña
        self.widget.crear_label_texto_normal(contenido_principal, "Contraseña").pack()
        entry_contraseña = self.widget.crear_entry(contenido_principal, False)
        entry_contraseña.insert(0, self.contraseña)
        entry_contraseña.configure(state="readonly")
        entry_contraseña.pack(pady=5)

            # Entrada para rango
        self.widget.crear_label_texto_normal(contenido_principal, "Rango").pack()
        entry_rango = self.widget.crear_entry(contenido_principal, False)
        entry_rango.insert(0, self.rango)
        entry_rango.configure(state="readonly")
        entry_rango.pack(pady=5)
        # boton para habilitar la edicion de perfil
        btn_editar = self.widget.crear_boton(contenido_principal, "Editar Perfil", 
                                            lambda: self.utilidades_interfaz.habilitar_edicion(entry_nombre, entry_email, entry_contraseña, entry_rango))
        btn_editar.pack(pady=10)

            # Botón de guardar solo se muestra si se habilita la edición
        btn_guardar = self.widget.crear_boton(contenido_principal, "Guardar Cambios", 
                                            lambda: self.utilidades_interfaz.guardar_cambios(entry_nombre, entry_email, entry_contraseña, entry_rango, self.cedula))
        btn_guardar.pack(pady=20)

    def crear_reporte(self, idAula):
        # Consulta SQL para obtener los elementos del aula específica

        resultados = self.operacionesSQL.obtener_elemento_de_aula(idAula)

        # Crear el PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Reporte De Aula", 0, 1, "C")
        pdf.ln(10)

        # Agregar encabezados de columna
        columns = ["Nombre", "Tipo", "Estado", "Fecha Adquisición", "Cantidad", "IdAula"]
        pdf.set_font("Times", "B", 14)
        for col in columns:
            pdf.cell(30, 10, col, 1, 0, "C")
        pdf.ln()

        # Agregar filas con los datos
        pdf.set_font("Times", "", 12)
        for row in resultados:
            for item in row:
                pdf.cell(30, 10, str(item), 1, 0, "C")
            pdf.ln()
        
        nombre_archivo = f"Reporte_Aula_{idAula}.pdf"

        # Guardar el archivo PDF
        nombre_archivo = f"Reporte_Aula_{idAula}.pdf"
        pdf.output(nombre_archivo)
        

        
    
class Administrador(InterfazUsuario):
    def __init__(self, cedula, nombre, email, contraseña, rango):
        super().__init__(cedula, nombre, email, contraseña, rango)
    
    
    def crear_nueva_sala(self, contenido_principal):
        # Limpiar el contenido previo en el frame principal
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        # Frame contenedor central
        frame_contenedor = ctk.CTkFrame(contenido_principal)
        frame_contenedor.pack(fill="both", expand=True)  # Ocupar todo el espacio y centrar

        # Sección de registro
        frame_registro = self.widget.crear_frame(frame_contenedor)
        frame_registro.pack(anchor="center", fill=ctk.BOTH, expand=True, padx=10, pady=10)  # Centrar y agregar padding

        # Título de registro
        label_register = self.widget.crear_label_titulo_subtitulos(frame_registro, "Crear Aula")
        label_register.pack(anchor="center", pady=10)  # Centrar el título

        # Crear un frame interno para organizar en dos columnas
        frame_form = self.widget.crear_frame(frame_registro)
        frame_form.pack(anchor="center", pady=20, padx=10)  # Centrar el frame_form dentro de frame_registro

        # ID del aula
        label_id_aula = self.widget.crear_label_texto_normal(frame_form, "Ingrese el ID del aula: ")
        label_id_aula.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        entry_id_aula = self.widget.crear_entry(frame_form, False)
        entry_id_aula.grid(row=0, column=1, padx=10, pady=10)

        # Tipo de sala
        label_tipo = self.widget.crear_label_texto_normal(frame_form, "Ingrese el tipo de sala:")
        label_tipo.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        opciones = ["Laboratorio", "Docencia", "Clase"]
        entry_tipo = self.widget.crear_combobox(frame_form, opciones)
        entry_tipo.grid(row=1, column=1, padx=10, pady=10)
        
        # Botón para crear el aula
        button_crear_sala = self.widget.crear_boton(frame_form, "Crear Sala", lambda: agregar_nueva_aula())
        button_crear_sala.grid(row=5, column=1, pady=20, sticky="e")  # Alinear a la derecha

        
        def agregar_nueva_aula():
            id_aula = entry_id_aula.get()
            tipo = entry_tipo.get()
            
            self.validar.validar_numero(id_aula)
            
            self.operacionesSQL.crear_aula(id_aula, tipo)
            
            self.notificacion.show_info("Aula Agregada", f"Aula con id {id_aula} y de tipo {tipo} fue agregado correctamente")
                
            # Limpiar campos después de insertar
            entry_id_aula.delete(0, ctk.END)
            # entry_size.delete(0, ctk.END)
            entry_tipo.set("")  # Esto limpia el ComboBox

    def agregar_elemento_a_aula(self, contenido_principal, id_aula):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        # Seccion de registro
        frame_agregar = self.widget.crear_frame(contenido_principal)
        frame_agregar.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        label_register = self.widget.crear_label_titulo_subtitulos(frame_agregar, "Agregar Elemento")
        label_register.pack(pady=10)

        # crear un frame interno para organizar en dos columnas
        frame_form = self.widget.crear_frame(frame_agregar)
        frame_form.pack(pady=20, padx=10)
        
        # Nombre
        label_nombre = self.widget.crear_label_texto_normal(frame_form, "Nombre del elemento")
        label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        

        entry_nombre = self.widget.crear_entry(frame_form, False)
        entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        
        #tipo
        label_tipo = self.widget.crear_label_texto_normal(frame_form, "Tipo de elemento")
        label_tipo.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        tipo = ["Mueble", "Electrodomestico"]
        entry_tipo = self.widget.crear_combobox(frame_form, tipo)
        entry_tipo.grid(row=1, column=1, padx=10, pady=10)
        
        #estado del elemento
        label_estado = self.widget.crear_label_texto_normal(frame_form, "Nombre del elemento")
        label_estado.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        estado = ["Malo", "Regular", "Bueno", "Exelente"]
        entry_estado = self.widget.crear_combobox(frame_form, estado)
        entry_estado.grid(row=2, column=1, padx=10, pady=10)
        
        
        #fecha de adquisicion
        label_fecha = self.widget.crear_label_texto_normal(frame_form, "Fecha de adquisición")
        label_fecha.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        # Entrada de fecha con calendario emergente
        entry_fecha = self.widget.crear_entry(frame_form, False)
        entry_fecha.grid(row=3, column=1, padx=10, pady=10)

        # Función para abrir el calendario y seleccionar una fecha
        def abrir_calendario():
            # Crear ventana emergente de calendario
            top_calendario = tk.Toplevel(contenido_principal)
            top_calendario.grab_set()

            calendario = Calendar(top_calendario, selectmode='day', date_pattern='yyyy-mm-dd')
            calendario.pack(pady=20)

            def seleccionar_fecha():
                fecha_seleccionada = calendario.get_date()
                entry_fecha.delete(0, tk.END)
                entry_fecha.insert(0, fecha_seleccionada)
                top_calendario.destroy()

            boton_seleccionar = self.widget.crear_boton(top_calendario, "Seleccionar", lambda: seleccionar_fecha())
            boton_seleccionar.pack(pady=10)

        # Asociar el calendario al hacer clic en el campo de entrada de fecha
        entry_fecha.bind("<Button-1>", lambda e: abrir_calendario())
        
        #cantidad
        label_numero = self.widget.crear_label_texto_normal(frame_form, "Ingrese la cantidad")
        label_numero.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        
        # Entrada de fecha con calendario emergente
        entry_numero = self.widget.crear_entry(frame_form, False)        
        entry_numero.grid(row=4, column=1, padx=10, pady=10)
        
        # Llamar a la funcion para agregar el elemento
        button_crear_sala = self.widget.crear_boton(frame_form, "Agregar",
                                    lambda: agregar_elemento(id_aula))
        button_crear_sala.grid(row=5, column=1, pady=20)  
         
        def agregar_elemento(id_aula):
            nombre = entry_nombre.get()
            tipo_elemto = entry_tipo.get()
            estado = entry_estado.get()
            fecha = entry_fecha.get()
            cantidad = entry_numero.get()
            
            
            self.validar.validar_texto(nombre)
            self.validar.validar_texto(tipo_elemto)
            self.validar.validar_texto(estado)
            self.validar.validar_fecha(fecha)
            self.validar.validar_numero(cantidad)
        
            try:
                self.operacionesSQL.agregar_elemento_a_aula_sql(nombre, tipo_elemto, estado, fecha, cantidad, id_aula)
                self.notificacion.show_info("Elemento agregado", f"Se a agregado correctamente el elemento {nombre} al aula con id {id_aula}")
                
                # Limpiar campos despues de insertar
                entry_nombre.delete(0, ctk.END)# Esto limpia el entry
                entry_tipo.set("")  # Esto limpia el ComboBox
                entry_estado.set("")  # Esto limpia el ComboBox
                entry_fecha.delete(0, ctk.END) # Esto limpia el entry
                entry_numero.delete(0, ctk.END)# Esto limpia el entry
                
            except Exception as e:
                self.notificacion.show_error("Database Error", f"Error: {e}")
                # conexion.rollback()
                
        
    def eliminar_elemento(self,contenido_principal, idAula):
        
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        # Frame para la tabla de datos
# Correcto: solo pasar 'side' y otros parámetros en el pack
        table_frame = self.widget.crear_scrollable_frame(contenido_principal)
        table_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)


        # Encabezados de columna
        # columns = ["Nombre", "Tipo", "Estado", "Fecha De Adquisicion", "Cantidad"]
        
        # Funcion para actualizar la tabla después de cada eliminación
        def actualizar_tabla(idAula):
            # Limpiar el contenido previo (ignorando encabezados de columna)
            # for widget in table_frame.winfo_children()[len(columns):]:
            #     widget.destroy()

            # Obtener los elementos desde la base de datos
            resultados = self.operacionesSQL.obtener_elementos(idAula)
            columnas_nombre = ["Nombre", "Tipo", "Estado", "Fecha Adquisicion", "Cantidad", "Acciones"]
            tabla = Subtabla(table_frame, columnas_nombre)
            
            # Recorrer cada elemento y crear filas en la tabla
            for (IdElemento, nombre, tipo, estado, fechAdquisicion, cantidad) in resultados:                
                # Crear una lista con los datos de la fila
                fila_datos = [nombre, tipo, estado, fechAdquisicion, cantidad]
                tabla.agregar_fila(fila_datos)

                # Botón para eliminar el elemento
                btn_eliminar = self.widget.crear_boton(table_frame, "Eliminar",
                    lambda IdElemento=IdElemento: eliminar(IdElemento, idAula)
                )
                # Posicionar el botón de "Eliminar" en la columna de acciones
                btn_eliminar.grid(row=tabla.frame_padre.grid_size()[1] - 1, column=5, padx=2)
           
        # Función para eliminar un elemento
        def eliminar(IdElemento, idAula):
            try:
                self.operacionesSQL.eliminar_elemento(IdElemento)
                self.notificacion.show_info("Eliminar", f"El elemento con fue eliminado correctamente del aula con ID {idAula}")

                # Llamar a la función para actualizar la tabla con el filtro actual
                actualizar_tabla(idAula)
                
            except Exception as e:
                self.notificacion.show_error("Error", f"No se pudo eliminar el elemento con ID {IdElemento} del aula con ID {idAula}: {e}")

        # aparece la tabla
        actualizar_tabla(idAula)

    
    def ingresar_usuario(self, contenido_principal):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)        

        # Seccion de registro
        frame_agregar = self.widget.crear_frame(contenido_principal)
        frame_agregar.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        label_register = self.widget.crear_label_titulo_subtitulos(frame_agregar, "Crear nuevo usuario")
        label_register.pack(pady=10)

        # crear un frame interno para organizar en dos columnas
        frame_form = self.widget.crear_frame(frame_agregar)
        frame_form.pack(pady=20, padx=10)
        
        # Cedula
        label_cedula = self.widget.crear_label_texto_normal(frame_form, "Cedula del usuario")
        label_cedula.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        entry_cedula = self.widget.crear_entry(frame_form, False)
        entry_cedula.grid(row=0, column=1, padx=10, pady=10)
        
        #Nombre
        label_nombre = self.widget.crear_label_texto_normal(frame_form, "Nombre del usuario")
        label_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        entry_nombre = self.widget.crear_entry(frame_form, False)
        entry_nombre.grid(row=1, column=1, padx=10, pady=10) 
        
        #Email
        label_email = self.widget.crear_label_texto_normal(frame_form, "Email del usuario nuevo")
        label_email.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        entry_email = self.widget.crear_entry(frame_form, False)
        entry_email.grid(row=2, column=1, padx=10, pady=10) 
        
        #contraseña
        label_password = self.widget.crear_label_texto_normal(frame_form, "contraseña")
        label_password.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        entry_password = self.widget.crear_entry(frame_form, True)
        entry_password.grid(row=3, column=1, padx=10, pady=10) 
        
        #rango
        label_rango = self.widget.crear_label_texto_normal(frame_form, "Rango del usuario")
        label_rango.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        
        rangos = ["Software", "IT", "Profesor", "ADMIN"]
        entry_rango = self.widget.crear_combobox(frame_form, rangos)
        entry_rango.grid(row=4, column=1, padx=10, pady=10) 
        
        # Llamar a la funcion para agregar el elemento
        button_crear_sala = self.widget.crear_boton(frame_form, "Agregar",
                                    lambda: agregar_usuario())
        button_crear_sala.grid(row=5, column=1, pady=20)  
        
        def agregar_usuario():
            cedula = entry_cedula.get()
            nombre = entry_nombre.get()
            email = entry_email.get()
            password = entry_password.get()
            rango = entry_rango.get()

            self.validar.validar_cedula(cedula)
            self.validar.validar_texto(nombre)
            self.validar.validar_email(email)
            self.validar.validar_contrasena(password)
            self.validar.validar_texto(rango)
            
            try:
                self.operacionesSQL.agregar_usuario_a_db(cedula, nombre, email, password, rango)
                self.notificacion.show_info("Usuario agregado", f"usuario {nombre} ingresado correctamente")
                
            except Exception as e:
                self.notificacion.show_error("Error", f"No se logro agreagr el usuario {nombre}: {e}")

    def ver_usuario(self, contenido_principal):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        # Seccion de registro
        frame_agregar = self.widget.crear_frame(contenido_principal)
        frame_agregar.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

        label_register = self.widget.crear_label_titulo_subtitulos(frame_agregar, "Eliminar usuario")
        label_register.pack(pady=10)

        # crear un frame interno para organizar
        tabla_frame = self.widget.crear_frame(frame_agregar)
        tabla_frame.pack(pady=20, padx=10)
        

        columna_nombre = ["Cedula", "Nombre", "Email", "Contraseña", "Rango"]
        tabla = Subtabla(tabla_frame, columna_nombre)

        def actualizar_tabla():
            # Limpiar el contenido previo
            for widget in tabla_frame.winfo_children()[len(columna_nombre):]:  # Ignorar encabezados de columna
                widget.destroy()

            resultados = self.operacionesSQL.obtener_datos_usuarios()

            for i, (cedula, nombre, email, contraseña, rango) in enumerate(resultados, start=1):
                # Crear una lista con los datos de la fila
                fila_datos = [cedula, nombre, email, contraseña, rango]
                tabla.agregar_fila(fila_datos)

                # Botón para eliminar el usuario
                btn_eliminar = self.widget.crear_boton(tabla_frame,"Eliminar",
                    lambda cedula=cedula: eliminar(cedula)
                )
                btn_eliminar.grid(row=tabla.frame_padre.grid_size()[1] - 1, column=5, padx=2)

                # Botón para modificar el usuario
                btn_modificar = self.widget.crear_boton(tabla_frame,"Modificar Usuario",
                    lambda contenido_principal=contenido_principal, cedula=cedula, nombre=nombre, email=email, contraseña=contraseña, rango=rango: self.modificar_usuario(contenido_principal, cedula, nombre, email, contraseña, rango)
                )
                btn_modificar.grid(row=tabla.frame_padre.grid_size()[1] - 1, column=6, padx=2)

        # Función para eliminar un usuario
        def eliminar(cedula):
            try:
                self.operacionesSQL.eliminar_usuario(cedula)
                self.notificacion.show_info("Eliminar", f"Se a eliminado correctamemnte al usuario con cedula {cedula}")

                # Llamar a la función para actualizar la tabla con el filtro actual
                actualizar_tabla()
                
            except Exception as e:
                self.notificacion.show_error("Error", f"No se pudo eliminar al usuario {cedula} {e}")

        # aparece la tabla
        actualizar_tabla()
            
    def modificar_usuario(self, contenido_principal, cedula, nombre, email, contraseña, rango):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)            
            # Crea los campos de entrada para cada valor a modificar
        self.widget.crear_label_texto_normal(contenido_principal, "Modificar Usuario").pack(pady=10)

        # Entrada para nombre
        self.widget.crear_label_texto_normal(contenido_principal, "Nombre").pack()
        entry_nombre = self.widget.crear_entry(contenido_principal)
        entry_nombre.insert(0, nombre)  # Muestra el valor actual
        entry_nombre.pack(pady=5)

            # Entrada para email
        self.widget.crear_label_texto_normal(contenido_principal, "Email").pack()
        entry_email = self.widget.crear_entry(contenido_principal)
        entry_email.insert(0, email)
        entry_email.pack(pady=5)

            # Entrada para contraseña
        self.widget.crear_label_texto_normal(contenido_principal, "Contraseña").pack()
        entry_contraseña = self.widget.crear_entry(contenido_principal, show="*")
        entry_contraseña.insert(0, contraseña)
        entry_contraseña.pack(pady=5)

        # Entrada para rango
        self.widget.crear_label_texto_normal(contenido_principal, "Rango").pack()
        entry_rango = self.widget.crear_entry(contenido_principal)
        entry_rango.insert(0, rango)
        entry_rango.pack(pady=5)

        # Botón para guardar los cambios
        def guardar_cambios():
            nuevo_nombre = entry_nombre.get()
            nuevo_email = entry_email.get()
            nueva_contraseña = entry_contraseña.get()
            nuevo_rango = entry_rango.get()
            try:
                
                # Actualiza los valores de usuario en la base de datos
     
                self.operacionesSQL.actualizar_usuario(nuevo_nombre, nuevo_email, nueva_contraseña, nuevo_rango, cedula)
                self.notificacion.show_info("Éxito", "Usuario modificado correctamente")

            except Exception as e:
                self.notificacion.show_error("Error", f"No se pudo modificar el usuario: {e}")

        btn_guardar = self.widget.crear_boton(contenido_principal, "Guardar Cambios", lambda: guardar_cambios())
        btn_guardar.pack(pady=20)

        
    def ver_comentarios(self, contenido_principal,idAula):
        self.utilidades_interfaz.limpiar_frame_principal(contenido_principal)

        # Frame para la tabla de datos
        table_frame = ctk.CTkScrollableFrame(contenido_principal, width=580)
        table_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        # Encabezados de columna
        columnas_nombre = ["Comentario", "fecha de creacion"]
        tabla = Subtabla(table_frame, columnas_nombre)

        resultados = self.operacionesSQL.comentario(idAula)
        
        for i, (contenido, fechaCreacion) in enumerate(resultados, start=1):
            # Crear una lista con los datos de la fila
            fila_datos = [contenido, fechaCreacion]
            tabla.agregar_fila(fila_datos)
        