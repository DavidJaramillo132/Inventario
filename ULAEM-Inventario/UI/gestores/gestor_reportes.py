import datetime
import os
from fpdf import FPDF

from UI.gestores import GestorErrores, GestorNotificaciones
from database import GestorServicioSQL
from enums import EquipoNombreDatos as END


class GestorReportes:
    @staticmethod

    @GestorErrores.decorador("Error al generar el reporte")
    def generar_reporte_aula(idAula):
        try:
            resultados = GestorServicioSQL.obtener_elementos_por_idaula(idAula)
            print(resultados)
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, f"Reporte de Aula {idAula}", 0, 1, "C")
            pdf.ln(10)

            # Encabezados de columna y anchos
            columns = [
                (END.NOMBRE.value, 50),
                (END.TIPO.value, 30),
                (END.ESTADO.value, 25),
                (END.FECHA_ADQUISICION.value, 40),
                (END.CANTIDAD.value, 20),
            ]

            GestorReportes._agregar_encabezados(pdf, columns)
            GestorReportes._agregar_filas(pdf, resultados, columns)

            # Guardar el archivo
            GestorReportes._guardar_pdf(pdf, idAula)

            # Muestra el mensaje de éxito solo si todo el proceso fue exitoso
            GestorNotificaciones.mostrar_info(
                "Reporte generado", "Reporte generado con éxito"
            )
            return True
        except Exception as e:
            raise Exception(f"Error al generar el reporte: {e}")


    @staticmethod
    def _agregar_encabezados(pdf, columns):
        pdf.set_font("Times", "B", 12)
        for col_name, col_width in columns:
            pdf.cell(col_width, 10, col_name, 1, 0, "C")
        pdf.ln()

    @staticmethod
    def _agregar_filas(pdf, resultados, columns):
        pdf.set_font("Times", "", 12)
        for row in resultados:
            for value, (_, col_width) in zip(row[1:], columns):
                pdf.cell(col_width, 10, str(value), 1, 0, "C")
            pdf.ln()

    @staticmethod
    def _guardar_pdf(pdf, idAula):
        # Asegurarse de que exista la carpeta de salida
        carpeta_reportes = "reportes"
        os.makedirs(carpeta_reportes, exist_ok=True)

        # Generar el nombre del archivo
        tiempo_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = os.path.join(
            carpeta_reportes, f"reporte_aula_{idAula}_{tiempo_actual}.pdf"
        )

        # Guardar el archivo
        pdf.output(nombre_archivo)
        print(f"Reporte guardado en: {nombre_archivo}")
