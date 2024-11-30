from components import (
    TopLevelPersonalizado,
    FormularioCrearElementos,
    LabelTituloSubtitulo,
    ContenedorBotones,
)
from UI.gestores import GestorErrores

from enums import EquipoNombreDatos as END


class InterfazAgregarElemento(FormularioCrearElementos):

    @classmethod
    @GestorErrores.decorador("Error al mostrar la interfaz de agregar elemento aula")
    def mostrar_interfaz_agregar_elemento_aula(cls, root, idAula):

        frame = TopLevelPersonalizado(root)
        frame.geometry("700x500")

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        cls._crear_interfaz_agregar_elemento(frame, idAula)

    @classmethod
    def _crear_interfaz_agregar_elemento(cls, frame, idAula):
        LabelTituloSubtitulo(
            frame,
            "Agregar nuevo elemento aula",
        ).grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="nsew")

        # Obtener los campos a rellenar y crear los widgets
        campos = [campo.value for campo in list(END)][1:]
        componentes = cls._crear_campos(frame, campos)

        # Poblar el último campo con idAula
        entry_id_aula = componentes.get(END.ID_AULA.value)
        if entry_id_aula:
            entry_id_aula.set(
                str(idAula)
            )  # Usar el método set para establecer el valor
            entry_id_aula.configure(state="disabled")  # Deshabilitar el campo
        else:
            raise KeyError(
                f"No se encontró el campo '{END.ID_AULA.value}' en los componentes."
            )

        # Crear botones
        cls._crear_botones(frame, componentes, idAula)

    @classmethod
    def _crear_botones(cls, frame, componentes, idAula):
        from UI.controllers import ControladorAgregarElemento

        frame_botones = ContenedorBotones(frame)
        frame_botones.grid(
            row=len(componentes) + 1,
            column=0,
            columnspan=2,
            padx=10,
            pady=5,
            sticky="nsew",
        )

        frame_botones.agregar_boton(
            "Agregar elemento",
            lambda: ControladorAgregarElemento.manejar_agregar_elemento_aula(
                frame,
                componentes[END.NOMBRE.value].get(),
                componentes[END.TIPO.value].get(),
                componentes[END.ESTADO.value].get(),
                componentes[END.FECHA_ADQUISICION.value].get(),
                componentes[END.CANTIDAD.value].get(),
                idAula,
            ),
            columna=0,
            columnspan=2,
        )
