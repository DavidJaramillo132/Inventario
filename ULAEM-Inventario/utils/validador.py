from datetime import datetime


class Validador:
    """
    Clase que agrupa métodos de validación para diferentes tipos de datos,
    asegurando que cumplan con ciertos criterios antes de ser procesados.
    """

    class ValidacionError(Exception):
        """
        Clase interna que representa errores específicos de validación.
        """

        pass

    @staticmethod
    def validar_texto(entrada):
        """
        Valida que la entrada sea un texto no vacío y compuesto solo por palabras alfabéticas.

        Args:
            entrada (str): Cadena de texto a validar.

        Raises:
            ValidacionError: Si la entrada está vacía o contiene caracteres no alfabéticos.
        """
        palabras = entrada.split()
        if not palabras:
            raise Validador.ValidacionError("El texto no puede estar vacío.")
        if not all(palabra.isalpha() for palabra in palabras):
            print(f"Error en: {palabras}")
            raise Validador.ValidacionError(
                "El texto solo puede contener palabras alfabéticas."
            )
    @staticmethod        
    def  validar_comentario(entrada):     
        if entrada.isalpha():
            return "Texto válido."

    @staticmethod
    def validar_email(email):
        """
        Valida que el email contenga '@' y '.'.

        Args:
            email (str): Dirección de email a validar.

        Raises:
            ValidacionError: Si el email no tiene '@' o '.'.
        """
        if "@" not in email or "." not in email:
            raise Validador.ValidacionError("El email debe de tener '@' Y '.'")
        if "ñ" in email or "Ñ" in email:
            raise Validador.ValidacionError("El email no debe de tener la palabra 'ñ'")
            

    @staticmethod
    def validar_cedula(cedula):
        """
        Valida que la cédula sea un número de exactamente 10 dígitos.

        Args:
            cedula (str): Cédula a validar.

        Raises:
            ValidacionError: Si la cédula no es numérica o no tiene 10 dígitos.
        """
        if not cedula.isdigit() or len(cedula) != 10:
            raise Validador.ValidacionError(
                "La cédula debe ser un número de 10 dígitos."
            )

    @staticmethod
    def validar_numero(numero):
        """
        Valida que el número sea un entero positivo.

        Args:
            numero: Valor numérico a validar.

        Raises:
            ValidacionError: Si el número no es un entero positivo.
        """
        try:
            int(numero)
        except ValueError:
            raise Validador.ValidacionError("El número debe ser un entero positivo.")

    @staticmethod
    def validar_fecha(fecha):
        """
        Valida que la fecha siga el formato 'YYYY-MM-DD'.

        Args:
            fecha (str): Fecha a validar.

        Raises:
            ValidacionError: Si la fecha no cumple con el formato esperado.
        """
        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            raise Validador.ValidacionError(
                "La fecha debe tener el formato YYYY-MM-DD."
            )

    @staticmethod
    def validar_contrasena(contrasena):
        """
        Valida que la contraseña contenga al menos un número y una letra.

        Args:
            contrasena (str): Contraseña a validar.

        Raises:
            ValidacionError: Si la contraseña no cumple con los criterios mínimos.
        """
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
        """
        Valida que ningún campo esté vacío.

        Args:
            *args: Campos a validar.

        Raises:
            ValidacionError: Si algún campo está vacío.
        """
        for campo in args:
            if not campo:
                raise Validador.ValidacionError("Campos incompletos")

    @staticmethod
    def validar_todos_campos_cuenta(
        cedula, nombre, email, contrasena, ocupacion, privilegios
    ):
        """
        Valida que todos los campos necesarios para crear una cuenta sean válidos.

        Args:
            cedula: Cédula del usuario.
            nombre: Nombre del usuario.
            email: Email del usuario.
            contrasena: Contraseña del usuario.
            ocupacion: Ocupación del usuario.
            privilegios: Privilegios asignados al usuario.

        Raises:
            ValidacionError: Si algún campo no cumple con los criterios de validación.
        """
        Validador.validar_campos_completos(
            cedula, nombre, email, contrasena, ocupacion, privilegios
        )
        Validador.validar_cedula(cedula)
        Validador.validar_texto(nombre)
        Validador.validar_email(email)
        Validador.validar_contrasena(contrasena)
        

    def validar_todos_campos_sala(idAula, dimensiones, tipo):
        """
        Valida los campos necesarios para la configuración de una sala.

        Args:
            dimensiones: Dimensiones de la sala.
            tipo: Tipo de sala.

        Raises:
            ValidacionError: Si los campos no cumplen con los criterios de validación.
        """
        Validador.validar_campos_completos(idAula, dimensiones, tipo)
        Validador.validar(idAula, dimensiones, tipo)

    def validar_todos_campos_elementos(
        nombre, tipo, estado, fecha_adquisicion, cantidad, idAula
    ):
        """
        Valida los campos necesarios para registrar elementos en una sala.

        Args:
            nombre: Nombre del elemento.
            tipo: Tipo de elemento.
            estado: Estado del elemento.
            fecha_adquisicion: Fecha de adquisición del elemento.
            cantidad: Cantidad de elementos.
            idAula: Identificador del aula asociada.

        Raises:
            ValidacionError: Si los campos no cumplen con los criterios de validación.
        """
        Validador.validar_campos_completos(
            nombre, tipo, estado, fecha_adquisicion, cantidad, idAula
        )
        Validador.validar(nombre, tipo, estado, fecha_adquisicion, cantidad, idAula)

    def validar_todos_campos_comentarios(contenido, idAula):
        """
        Valida los campos necesarios para registrar comentarios.

        Args:
            contenido: Contenido del comentario.
            idAula: Identificador del aula asociada.

        Raises:
            ValidacionError: Si los campos no cumplen con los criterios de validación.
        """
        Validador.validar_campos_completos(contenido, idAula)
        Validador.validar(contenido, idAula)

    @staticmethod
    def validar(*args):
        """
        Método que valida múltiples tipos de datos con un solo método, utilizando
        argumentos variables para adaptarse a los diferentes casos.

        Args:
            *args: Campos a validar que pueden ser de diferentes tipos (str, int, etc.).

        Raises:
            ValidacionError: Si algún campo no cumple con los criterios de validación.
        """
        for campo in args:
            print(campo)
            if isinstance(campo, str):
                if "-" in campo:
                    Validador.validar_fecha(campo)
                elif campo.isdigit():
                    Validador.validar_numero(campo)
                elif campo.isalpha():
                    Validador.validar_texto(campo)
                else:
                    # Si el campo es un texto, valida como texto
                    Validador.validar_comentario(campo)
            elif isinstance(campo, int):
                # Si el campo es un número, valida como número
                Validador.validar_numero(campo)

            else:
                raise Validador.ValidacionError(
                    f"Validación no soportada para el tipo: {type(campo)}"
                )
