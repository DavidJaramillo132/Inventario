import pyodbc

DRIVER = "{ODBC Driver 17 for SQL Server}"
SERVER = "localhost"
DATABASE = "uleamU"
RUTA_ARCHIVO_SQL = r"ULAEM-Inventario\database\sql_creacion_tablas.sql"
with open(RUTA_ARCHIVO_SQL, "r") as file:
    SCRIPT_CREATE_TABLES = file.read()

class ConexionBD:
    def __init__(self):
        try:
            self.conexion = pyodbc.connect(
                f"DRIVER={DRIVER};"
                f"SERVER={SERVER};"
                f"DATABASE={DATABASE};"
                "Trusted_Connection=yes;"
            )
            self.cursor = self.conexion.cursor()
            self.cursor.execute(SCRIPT_CREATE_TABLES)
            self.commit()
        except pyodbc.Error as e:
            raise pyodbc.Error(f"Error al conectar a la base de datos: {e}")

    # Ejecuta una consulta SQL
    def execute(self, query, params=()):
        try:
            self.cursor.execute(query, params)
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            # raise

    # Guarda los cambios
    def commit(self):
        self.conexion.commit()

    # Revertir cambios en caso de error
    def rollback(self):
        self.conexion.rollback()

    # Obtiene una fila del resultado
    def fetchone(self):
        return self.cursor.fetchone()

    # Obtiene todas las filas del resultado
    def fetchall(self):
        return self.cursor.fetchall()

    # Cierra la conexión y el cursor
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
