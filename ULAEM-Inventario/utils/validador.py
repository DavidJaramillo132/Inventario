from datetime import datetime


class Validador:
    class ValidacionError(Exception):
        pass

    @staticmethod
    def validar_texto(entrada):
        palabras = entrada.split()
        if not palabras:
            raise Validador.ValidacionError("El texto no puede estar vacío.")
        if not all(palabra.isalpha() for palabra in palabras):
            raise Validador.ValidacionError(
                "El texto solo puede contener palabras alfabéticas."
            )

    @staticmethod
    def validar_email(email):
        if "@" not in email or "." not in email:
            raise Validador.ValidacionError("El email debe de tener '@' y '.'")

    @staticmethod
    def validar_cedula(cedula):
        if not cedula.isdigit() or len(cedula) != 10:
            raise Validador.ValidacionError(
                "La cédula debe ser un número de 10 dígitos."
            )

    @staticmethod
    def validar_numero(numero):
        try:
            int(numero)


        except ValueError:
            raise Validador.ValidacionError("El número debe ser un entero positivo.")

    @staticmethod
    def validar_fecha(fecha):
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise Validador.ValidacionError(
                "La fecha debe tener el formato YYYY-MM-DD."
            )

    @staticmethod
    def validar_contrasena(contrasena):
        if not any(char.isdigit() for char in contrasena):
            raise Validador.ValidacionError(
                "La contraseña debe contener al menos un número."
            )
        if not any(char.isalpha() for char in contrasena):
            raise Validador.ValidacionError(
                "La contraseña debe contener al menos una letra."
            )

    @staticmethod
    def validar_campos_completos(*args):
        for campo in args:
            if not campo:
                raise Validador.ValidacionError("Campos incompletos")

    @staticmethod
    def validar_todos_campos_cuenta(
        cedula, nombre, email, contrasena, ocupacion, privilegios
    ):
        Validador.validar_campos_completos(
            cedula, nombre, email, contrasena, ocupacion, privilegios
        )

        Validador.validar_cedula(cedula)
        Validador.validar_texto(nombre)
        Validador.validar_email(email)
        Validador.validar_contrasena(contrasena)

    def validar_todos_campos_sala(dimensiones, tipo):
        Validador.validar_campos_completos(dimensiones, tipo)
        Validador.validar_texto(tipo)
        Validador.validar_numero(dimensiones)

    def validar_todos_campos_elementos(
        nombre, tipo, estado, fecha_adquisicion, cantidad, idAula
    ):
        Validador.validar_campos_completos(
            nombre, tipo, estado, fecha_adquisicion, cantidad, idAula
        )
        Validador.validar_texto(nombre)
        Validador.validar_texto(tipo)
        Validador.validar_texto(estado)
        Validador.validar_numero(cantidad)
        Validador.validar_fecha(fecha_adquisicion)

    def validar_todos_campos_comentarios(contenido, idAula):
        Validador.validar_campos_completos(contenido, idAula)
        Validador.validar_texto(contenido)
        Validador.validar_numero(idAula)
