import customtkinter as ctk
from utilidades.ConfiguraconApp import ConfigurarColores, ConfigararFuentesTexto


class WidgetCtk:
    def __init__(self):
        self.fuente_texto = ConfigararFuentesTexto()
        self.colores = ConfigurarColores()

        
    def crear_frame(self, freme):
        contenedor_frame = ctk.CTkFrame(freme, fg_color=self.colores.obtener_color_principal())
        # contenedor_frame.pack(anchor="center", fill="both", expand=True)
        return contenedor_frame
    
    
    def crear_label_titulo_subtitulos(self, frame, Contenido):
        label = ctk.CTkLabel(frame, text= Contenido, 
                             font=self.fuente_texto.obtener_fuente_titulos_subtitulos())
        return label
    
    def crear_label_texto_normal(self, frame, Contenido):
        label = ctk.CTkLabel(frame, text=Contenido, 
                             font=self.fuente_texto.obtener_fuente_textos())
        return label
    
    def crear_entry(self, frame, password):
        if password == True:
            entry = ctk.CTkEntry(frame, placeholder_text="", 
                                 show="*", height=50, width=200, 
                                 font=self.fuente_texto.obtener_fuente_textos(), 
                                 fg_color=self.colores.obtener_color_principal(), 
                                 border_width=10, 
                                 border_color=self.colores.obtener_color_bordes())
            return entry
        elif password == False:
            entry = ctk.CTkEntry(frame, placeholder_text="", 
                                 height=50, width=200, 
                                 font=self.fuente_texto.obtener_fuente_textos(), 
                                 fg_color=self.colores.obtener_color_principal(), 
                                 border_width=10, 
                                 border_color=self.colores.obtener_color_bordes())
            return entry
        else:
            print("Error en el entry")
            
    def crear_boton(self, freme,  contenido, commando):
        boton = ctk.CTkButton(freme, text=contenido, 
                              command=commando, 
                              font=self.fuente_texto.obtener_fuente_textos(), 
                              fg_color=self.colores.obtener_color_principal(), 
                              hover_color=self.colores.obtener_color_botones())
        return boton
    
    def crear_checkbox(self, freme, rango):
        checkbox = ctk.CTkComboBox(freme, values=rango, 
                                   height=50, width=200, 
                                   fg_color=self.colores.obtener_color_principal(), 
                                   border_width=10, border_color=self.colores.obtener_color_bordes())
        return checkbox
    
    def crear_scrollable_frame(self, frame_padre):
        # Método para crear un CTkScrollableFrame
        scrollable_frame = ctk.CTkScrollableFrame(
            frame_padre, 
            fg_color=self.colores.obtener_color_principal(), 
            width=580
        )
        return scrollable_frame
    
    def crear_combobox(self, frame, valores):
        combobox = ctk.CTkComboBox(
            frame,
            values=valores,
            height=50,
            width=200,
            fg_color=self.colores.obtener_color_principal(),
            border_width=10,
            border_color=self.colores.obtener_color_bordes()
        )
        return combobox