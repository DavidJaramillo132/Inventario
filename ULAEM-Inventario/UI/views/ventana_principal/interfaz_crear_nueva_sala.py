from enums import AulaNombreDatos as AND
from UI.gestores import GestorErrores
from utils.utilidades_interfaz import UtilidadesParaInterfaz

from components import LabelTituloSubtitulo, ContenedorBotones, ContenedorPrincipal,FormularioCrearAulas


class InterfazCrearNuevaSala(FormularioCrearAulas):
    @classmethod
    @GestorErrores.decorador("Error al mostrar el registro")
    def mostrar_interfaz_crear_sala(cls, frame_principal):
        UtilidadesParaInterfaz.limpiar_frame_principal(frame_principal)

        # Configurar frame_principal para distribuir espacio
        frame_principal.grid_columnconfigure(0, weight=1)
        frame_principal.grid_rowconfigure(0, weight=1)

        # Crear un contenedor interno centrado
        contenedor = ContenedorPrincipal(frame_principal)
        contenedor.grid(row=0, column=0, sticky="n")
        cls.__crear_interfaz_nueva_sala(contenedor)

    @classmethod
    def __crear_interfaz_nueva_sala(cls, contenedor):
        # Título
        LabelTituloSubtitulo(
            contenedor,
            "Crear nueva sala",
        ).grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")


        # Campos a mostrar
        campos = [campo.value for campo in list(AND)][1:]
        componentes = cls._crear_campos(contenedor, campos)

        # Crear botones
        cls._crear_botones(contenedor, componentes)

    @classmethod
    def _crear_botones(cls, contenedor, componentes):
        from UI.controllers import ControladorCrearSala

        frame_botones = ContenedorBotones(contenedor)
        frame_botones.grid(
            row=len(componentes) + 1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew"
        )

        frame_botones.agregar_boton(
            "Crear nueva sala",
            lambda: ControladorCrearSala.manejar_crear_nueva_sala(
                componentes[AND.DIMENSIONES.value].get(),
                componentes[AND.TIPO.value].get(),
            ),
            columna=0,
            columnspan=2,
        )
