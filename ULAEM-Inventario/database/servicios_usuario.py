from database.conexion_DB import ConexionBD


class ServiciosUsuario:
    db = ConexionBD()

    @classmethod
    def obtener_usuarios(cls):
        try:
            cls.db.execute("SELECT * FROM Usuario")
            resultadoUsuarios = cls.db.fetchall()
            if not resultadoUsuarios:
                raise Exception("No hay usuarios registrados")
            return resultadoUsuarios
        except Exception as e:
            raise Exception(f"Error al obtener usuarios: {str(e)}")

    @classmethod
    def obtener_cedula_contrasena(cls):
        try:
            cls.db.execute("SELECT cedula,contrasena FROM Usuario")
            resultadoUsuarios = cls.db.fetchall()
            if not resultadoUsuarios:
                raise Exception("No hay usuarios registrados")
            return resultadoUsuarios
        except Exception as e:
            raise Exception(f"Error al obtener usuarios: {str(e)}")

    @classmethod
    def obtener_usuario_por_cedula(cls, cedula):
        try:
            cls.db.execute("SELECT * FROM Usuario WHERE cedula = ?", (cedula,))
            resultadoUsuario = cls.db.fetchone()
            if not resultadoUsuario:
                raise Exception("Usuario no encontrado")
            return resultadoUsuario
        except Exception as e:
            raise Exception(
                f"Error al obtener el usuario con cédula {cedula}: {str(e)}"
            )

    @classmethod
    def actualizar_usuario(
        cls,
        cedula,
        nuevo_nombre,
        nuevo_email,
        nueva_contraseña,
        nueva_ocupacion,
        nuevos_privilegios,
    ):
        try:
            cls.db.execute(
                """UPDATE Usuario 
                   SET nombre = ?, email = ?, contrasena = ?, ocupacion = ?, privilegios = ?
                   WHERE cedula = ?""",
                (
                    nuevo_nombre,
                    nuevo_email,
                    nueva_contraseña,
                    nueva_ocupacion,
                    nuevos_privilegios,
                    cedula,
                ),
            )
            print(cls.obtener_usuario_por_cedula(cedula))
            cls.db.commit()
            return True
        except Exception as e:
            raise Exception(f"Error al actualizar usuario: {str(e)}")

    @classmethod
    def registrar_usuario(cls, cedula, nombre, email, password, ocupacion, privilegios):
        try:
            cls.db.execute(
                "SELECT * FROM Usuario WHERE cedula=? or email=?", (cedula, email)
            )
            if cls.db.fetchone():
                raise Exception("El usuario ya existe")

            cls.db.execute(
                "INSERT INTO Usuario (cedula, nombre, email, contrasena, ocupacion,privilegios) VALUES (?, ?, ?, ?, ?,?)",
                (cedula, nombre, email, password, ocupacion, privilegios),
            )
            cls.db.commit()
            return True
        except Exception as e:

            raise Exception(f"Error al registrar usuario: {str(e)}")

    @classmethod
    def eliminar_usuario(cls, cedula):
        try:
            cls.db.execute("DELETE FROM Usuario WHERE cedula = ?", (cedula,))
            cls.db.commit()
            return True
        except Exception as e:
            raise Exception(f"Error al eliminar usuario con cédula {cedula}: {str(e)}")
