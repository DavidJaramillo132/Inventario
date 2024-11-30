from utils.utilidades_interfaz import UtilidadesParaInterfaz
from components import ContenedorPrincipal


class InterfazVentanaPrincipal:

    @classmethod
    def mostrar_interfaz_ventana_principal(cls, root):
        UtilidadesParaInterfaz.limpiar_frame_principal(root)

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=0)
        root.grid_columnconfigure(1, weight=1)

        cls.__crear_ventana_principal(root)

    @staticmethod
    def __crear_ventana_principal(root):
        from UI.views.ventana_principal import BarraLateral

        contenedor_principal = ContenedorPrincipal(root)
        contenedor_principal.grid(row=0, column=1, sticky="nsew")
        barraLateral = BarraLateral(root, contenedor_principal)
        barraLateral.grid(row=0, column=0, sticky="ns")
