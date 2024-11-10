from Database.conexionDB import ConexionBD
from UI.notificaciones import Notificaciones_aviso
from datetime import datetime

class operacionSQL:
    def __init__(self):
        self.db = ConexionBD()
        self.notificacion = Notificaciones_aviso()


    def obtener_aulas(self):
        # query = "SELECT idAula, tamaño, tipo FROM Aula"
        self.db.execute("SELECT idAula, tipo FROM Aula")
        return self.db.fetchall()  # Usa el método fetchall de ConexionBD
    
    def obtener_elementos_por_idaula(self, id_aula):
        self.db.execute("""
            SELECT nombre, tipo, estado, fechAdquisicion, cantidad, idAula, IdElemento
            FROM Elemento 
            WHERE idAula = ?
        """, (id_aula,))
        return self.db.fetchall()
    
    def comentario(self, idAula):
                # Consulta SQL para obtener datos actualizados con filtro
        self.db.execute("""
                SELECT  contenido, fechaCreacion
                FROM Comentario 
                WHERE idAula = ?
        """, (idAula,))

        return self.db.fetchall()
    #iinsertar comentarios
    def insertar_comentaraio(self, comentario, idAula, cedula):
        try:
            self.db.execute("INSERT INTO Comentario (contenido, idAula, cedula) VALUES (?, ?, ?)", (comentario, idAula, cedula))
            self.db.commit()
            self.notificacion.show_info("Comentario", "Comentario agregado")
            self.db.commit()
        
        except Exception as e:
            self.notificacion.show_error("Database Error", f"Error: {e}")
            self.db.rollback()
    
        # Recupera datos del usuario desde la base de datos
    def recuperar_usuario_por_cedula(self, cedula):
        self.db.execute("SELECT nombre, email, contraseña, rango FROM Usuario WHERE cedula = ?", (cedula,))
        return self.db.fetchone()
    
        # Actualiza los valores en la base de datos
    def actualizar_valores(self,nuevo_nombre, nuevo_email, nueva_contraseña, nuevo_rango, cedula):
        self.db.execute(""" UPDATE Usuario 
                        SET nombre = ?, email = ?, contraseña = ?, rango = ? 
                        WHERE cedula = ?""",(nuevo_nombre, nuevo_email, nueva_contraseña, nuevo_rango, cedula))
        self.db.commit()
    
    # Consulta SQL para obtener los elementos del aula específica
    def obtener_elemento_de_aula(self, idAula):
        self.db.execute("""
            SELECT nombre, tipo, estado, fechAdquisicion, cantidad, idAula 
            FROM Elemento 
            WHERE idAula = ?
        """, (idAula,))
        return self.db.fetchall()
    #Crear aula
    def crear_aula(self,id_aula, tipo):
        self.db.execute("insert into Aula(idAula, tipo) values (?,?)", (id_aula, tipo))
        self.db.commit()
    #agregar_elemento_a_aula
    def agregar_elemento_a_aula_sql(self,nombre, tipo_elemto, estado, fecha, cantidad, id_aula):
        self.db.execute("""
                    INSERT INTO Elemento (nombre, tipo, estado, fechAdquisicion, cantidad, idAula)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """, (nombre, tipo_elemto, estado, datetime.strptime(fecha, "%Y-%m-%d"), cantidad, id_aula))
        self.db.commit()
    # Consulta SQL para obtener datos actualizados con filtro
    def obtener_elementos(self, idAula):
        self.db.execute("""
                SELECT IdElemento, nombre, tipo, estado, fechAdquisicion, cantidad 
                FROM Elemento 
                WHERE idAula = ?
            """, (idAula))
        return self.db.fetchall()
    
    # Función para eliminar un elemento
    def eliminar_elemento(self,IdElemento):
        self.db.execute("DELETE FROM Elemento WHERE IdElemento = ?", (IdElemento))
        self.db.commit()
        
    # Eliminar sala
    def eliminar_aula(self, idAula):
        try:
            # Inicia una transacción y elimina directamente el aula
            self.db.execute("DELETE FROM Aula WHERE idAula = ?", (idAula,))
            self.db.commit()
        except Exception as e:
            # Si ocurre un error, revertir cambios
            self.db.rollback()
            print(f"Error al eliminar el aula {idAula}: {e}")

        
    #Agrega usuario
    def agregar_usuario_a_db(self,cedula, nombre, email, password, rango):
        self.db.execute("""
                    INSERT INTO Usuario (cedula, nombre, email, contraseña, rango)
                    VALUES (?, ?, ?, ?, ?)
                """, (cedula, nombre, email, password, rango))
        self.db.commit()
        
    # Consulta SQL para obtener datos de usuario
    def obtener_datos_usuarios(self):
        self.db.execute("""
                SELECT cedula, nombre, email, contraseña, rango 
                FROM Usuario 
            """)
        return self.db.fetchall()
        
    # Función para eliminar un usuario
    def eliminar_usuario(self, cedula):
        self.db.execute("delete from Usuario where cedula = ?",(cedula))
        self.db.commit()
        
    # Actualiza los valores de usuario
    def actualizar_usuario(self, nuevo_nombre, nuevo_email, nueva_contraseña, nuevo_rango, cedula):
        self.db.execute("""
                    UPDATE Usuario 
                    SET nombre = ?, email = ?, contraseña = ?, rango = ? 
                    WHERE cedula = ?
                """, (nuevo_nombre, nuevo_email, nueva_contraseña, nuevo_rango, cedula))
        self.db.commit()