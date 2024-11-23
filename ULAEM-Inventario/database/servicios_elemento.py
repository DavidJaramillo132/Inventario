from .conexion_DB import ConexionBD


class ServiciosElemento:
    db = ConexionBD()

    @classmethod
    def obtener_elementos_por_idaula(cls, id_aula):
        try:
            cls.db.execute(
                """
                    SELECT idElemento, nombre,tipo, estado,fechaAdquisicion,cantidad
                    FROM Elemento 
                    WHERE idAula = ?
                """,
                (id_aula,),
            )
            resultadoElementos = cls.db.fetchall()
            if not resultadoElementos:
                raise Exception("No hay elementos registrados")
            return resultadoElementos
        except Exception as e:
            raise Exception(f"Error al obtener elementos del aula: {str(e)}")

    @classmethod
    def agregar_elemento_a_aula(
        cls, nombre, tipo_elemto, estado, fecha, cantidad, id_aula
    ):
        try:
            cls.db.execute(
                """
                        INSERT INTO Elemento (nombre, tipo, estado, fechaAdquisicion, cantidad, idAula)
                        VALUES (?, ?, ?, ?, ?, ?)
                        """,
                (nombre, tipo_elemto, estado, fecha, cantidad, id_aula),
            )
            cls.db.commit()
            return True
        except Exception as e:
            cls.db.rollback()
            raise Exception(f"Error al agregar elemento al aula: {str(e)}")

    @classmethod
    def eliminar_elemento_de_aula(cls, id_elemento):
        try:
            cls.db.execute("DELETE FROM Elemento WHERE IdElemento = ?", (id_elemento,))
            cls.db.commit()
            return True
        except Exception as e:
            cls.db.rollback()
            raise Exception(f"Error al eliminar elemento del aula: {str(e)}")
