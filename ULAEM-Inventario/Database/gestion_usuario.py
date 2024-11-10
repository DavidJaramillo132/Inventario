from UI.notificaciones import Notificaciones_aviso
from Database.conexionDB import ConexionBD
from UI.notificaciones import Notificaciones_aviso
# Servicio para gestión de usuarios
class ServiciosUsuario:
    def __init__(self):
        self.db = ConexionBD()
        self.notificacion = Notificaciones_aviso

    def obtener_usuario(self, cedula):
        self.db.execute("SELECT * FROM Usuario WHERE cedula = ?", (cedula,))
        return self.db.fetchone()


    def registrar_usuario(self, cedula, nombre, email, password, rango):
        if not all([cedula, nombre, email, password, rango]):
            self.notificacion.show_error("ERROR", "Todos los campos son obligatorios")
            return False

        self.db.execute("SELECT * FROM Usuario WHERE cedula=?", (cedula,))
        if self.db.fetchone():
            self.notificacion.show_error("Error", "El usuario ya existe")
            return False

        self.db.execute(
            "INSERT INTO Usuario (cedula, nombre, email, contraseña, rango) VALUES (?, ?, ?, ?, ?)",
            (cedula, nombre, email, password, rango)
        )
        self.db.commit()
        self.notificacion.show_info("Registro", "Usuario registrado exitosamente")
        return True
    
    