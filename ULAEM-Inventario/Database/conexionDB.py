import pyodbc
# Abstracción para la conexión a la base de datos
class ConexionBD:
    def __init__(self):
        try:
            # Inicializa la conexión a la base de datos
            self.conexion = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=localhost;'
                'DATABASE=uleam;'
                'Trusted_Connection=yes;'  # Cambia a Trusted_Connection=no si pruebas con usuario y contraseña
                # 'UID=tu_usuario;PWD=tu_contraseña;'  # Descomenta y ajusta si usas autenticación SQL Server
            )
            self.cursor = self.conexion.cursor()
        except pyodbc.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
            raise

    # consultas
    def execute(self, query, params=()):
        try:
            # Ejecuta la consulta SQL
            self.cursor.execute(query, params)
        except pyodbc.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            self.rollback()
            raise

    # guardar cambios
    def commit(self):
        self.conexion.commit()

    # Obtiene una fila del resultado
    def fetchone(self):
        return self.cursor.fetchone()

    # Obtiene todas las filas del resultado
    def fetchall(self):
        return self.cursor.fetchall()
    
    # Revertir cambios en caso de error
    def rollback(self):
        self.conexion.rollback()

    # Cierra la conexión y el cursor
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
        print("Conexión cerrada.")
    # consultas
    def execute(self, query, params=()):
        # Ejecuta la consulta SQL
        self.cursor.execute(query, params)
    # guardar cambios
    def commit(self):
        self.conexion.commit()

        # Obtiene una fila del resultado
    def fetchone(self):
        return self.cursor.fetchone()

        # Obtiene todas las filas del resultado
    def fetchall(self):
        return self.cursor.fetchall()
    
    def rollback(self):
        self.cursor.rollback()
    