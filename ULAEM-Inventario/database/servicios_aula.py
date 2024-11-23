from database.conexion_DB import ConexionBD


class ServiciosAula:
    db = ConexionBD()

    @classmethod
    def obtener_aulas(cls):
        try:
            cls.db.execute("SELECT * FROM Aula")
            resultadosAulas = cls.db.fetchall()
            if not resultadosAulas:
                raise Exception("No hay aulas registradas")
            return resultadosAulas
        except Exception as e:
            raise Exception(f"Error al obtener aulas: {str(e)}")

    @classmethod
    def obtener_aula_por_id(cls, id_aula):
        try:
            cls.db.execute(
                "SELECT * FROM Aula WHERE idAula = ?", (id_aula,)
            )
            resultadoAula = cls.db.fetchone()
            if not resultadoAula:
                raise Exception("Aula no encontrada")
            return resultadoAula
        except Exception as e:
            raise Exception(f"Error al obtener aula: {str(e)}")

    @classmethod
    def actualizar_aula(cls, id_aula, tipo, dimensiones):
        try:
            cls.db.execute(
                "UPDATE Aula SET tipo = ? WHERE idAula = ?", (tipo, dimensiones,id_aula)
            )
            cls.db.commit()
            return True
        except Exception as e:
            cls.db.rollback()
            raise Exception(f"Error al actualizar aula: {str(e)}")

    @classmethod
    def crear_aula(cls, dimensiones,tipo):
        try:
            if not all([tipo, dimensiones]):
                raise Exception("Campos incompletos")

            cls.db.execute(
                "INSERT INTO Aula(dimensiones, tipo) VALUES (?,?)", (dimensiones,tipo)
            )
            cls.db.commit()
            return True
        except Exception as e:
            cls.db.rollback()
            raise Exception(f"Error al crear aula: {str(e)}")

    @classmethod
    def eliminar_aula(cls, id_aula):
        try:
            cls.db.execute("DELETE FROM Aula WHERE idAula = ?", (id_aula,))
            cls.db.commit()
            return True
        except Exception as e:
            cls.db.rollback()
            raise Exception(f"Error al eliminar aula: {str(e)}")

