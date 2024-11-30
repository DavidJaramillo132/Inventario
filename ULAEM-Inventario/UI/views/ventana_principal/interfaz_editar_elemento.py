from components import (
    TopLevelPersonalizado,
    FormularioCrearElementos,
    LabelTituloSubtitulo,
    ContenedorBotones,
)
from UI.gestores import GestorErrores
from enums import EquipoNombreDatos as END
from UI.controllers import ControladorEditarElemento


class InterfazEditarElemento(FormularioCrearElementos):

    @classmethod
    @GestorErrores.decorador("Error al mostrar la interfaz de agregar elemento aula")
    def mostrar_interfaz_editar_elemento(cls, root,frame_tabla_elemento, elemento):

        frame_editar_elemento = TopLevelPersonalizado(frame_tabla_elemento)
        frame_editar_elemento.geometry("600x500")

        frame_editar_elemento.grid_columnconfigure(0, weight=1)
        frame_editar_elemento.grid_rowconfigure(0, weight=1)

        cls._crear_interfaz_agregar_elemento(root,frame_tabla_elemento,frame_editar_elemento, elemento)

    @classmethod
    def _crear_interfaz_agregar_elemento(cls,root,frame_tabla_elemento,frame_editar_elemento, elemento):
        LabelTituloSubtitulo(frame_editar_elemento,"Editar elemento",).grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")

        campos = [campo.value for campo in list(END)][1:]
        componentes = cls._crear_campos(frame_editar_elemento, campos)

        ControladorEditarElemento.poblar_campos(campos, componentes, elemento)
        componentes.get(END.ID_AULA.value).configure(state="disabled")
        # Crear botones
        cls._crear_botones(root,frame_tabla_elemento,frame_editar_elemento, componentes, elemento)

    @classmethod
    def _crear_botones(cls, root,frame_tabla_elemento,frame_editar_elemento, componentes, elemento):

        frame_botones = ContenedorBotones(frame_editar_elemento)
        frame_botones.grid(
            row=len(componentes) + 1,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="nsew",
        )

        frame_botones.agregar_boton(
            "Editar elemento",
            lambda: ControladorEditarElemento.manejar_editar_elemento(
                frame_editar_elemento,
                frame_tabla_elemento,
                root,
                componentes[END.NOMBRE.value].get(),
                componentes[END.TIPO.value].get(),
                componentes[END.ESTADO.value].get(),
                componentes[END.FECHA_ADQUISICION.value].get(),
                componentes[END.CANTIDAD.value].get(),
                elemento,
            ),
            columna=0,
            columnspan=2,
        )
