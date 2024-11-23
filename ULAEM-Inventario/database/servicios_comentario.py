from database.conexion_DB import ConexionBD


class ServiciosComentario:
    db = ConexionBD()

    @classmethod
    def obtener_comentarios(cls):
        try:
            cls.db.execute("SELECT * FROM Comentario")
            resultadoUsuarios = cls.db.fetchall()
            if not resultadoUsuarios:
                raise Exception("No hay comentarios ingresados")
            return resultadoUsuarios
        except Exception as e:
            raise Exception(f"Error al obtener comentarios: {str(e)}")
        
    @classmethod
    def obtener_comentarios_por_aula(cls, idAula):
        try:
            cls.db.execute("SELECT * FROM Comentario WHERE idAula = ?", (idAula,))
            resultadoUsuarios = cls.db.fetchall()
            if not resultadoUsuarios:
                raise Exception("No hay comentarios ingresados")
            return resultadoUsuarios
        except Exception as e:
            raise Exception(f"Error al obtener comentarios: {str(e)}")

    @classmethod
    def crear_comentario(cls, contenido,idAula, cedula):
        try:
            cls.db.execute(
                "INSERT INTO Comentario (contenido,idAula,cedula) VALUES (?, ?,?)",
                (contenido,idAula, cedula),
            )
            cls.db.commit()
            return True
        except Exception as e:

            raise Exception(f"Error al registrar usuario: {str(e)}")
        
    @classmethod
    def eliminar_comentario(cls, idComentario):
        try:
            cls.db.execute("DELETE FROM Comentario WHERE idComentario = ?", (idComentario,))
            cls.db.commit()
            return True
        except Exception as e:
            raise Exception(f"Error al eliminar comentario: {str(e)}")
