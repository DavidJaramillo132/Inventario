from abc import abstractmethod
from ..baseAbstractClass import BaseAbstractClass
from enums import UsuarioNombreDatos as UND

class Usuario(BaseAbstractClass):
    def __init__(self, cedula, nombre, email, contrasena, ocupacion, privilegios):
        self.__cedula = cedula
        self._nombre = nombre
        self._email = email
        self.__contrasena = contrasena
        self.__ocupacion = ocupacion
        self.__privilegios = privilegios

    # Como contrato, debe implementar los metodos abstractos de la clase BaseAbstractClass

    def update_datos(
        self, nombre=None, email=None, contrasena=None, ocupacion=None, privilegios=None
    ):
        if nombre is not None:
            self.nombre = nombre
        if email is not None:
            self.email = email
        if contrasena is not None:
            self.contrasena = contrasena
        if ocupacion is not None:
            self.ocupacion = ocupacion
        if privilegios is not None:
            self.privilegios = privilegios

    # Como contrato, debe implementar los metodos abstractos de la clase BaseAbstractClass
    def get_datos(self, tipo="tuple"):
        if tipo == "dict":
            return {
                UND.CEDULA.value: self.cedula,
                UND.NOMBRE.value: self.nombre,
                UND.EMAIL.value: self.email,
                UND.CONTRASENA.value: self.contrasena,
                UND.OCUPACION.value: self.ocupacion,
                UND.PRIVILEGIOS.value: self.privilegios,
                
            }

        return (
            self.cedula,
            self.nombre,
            self.email,
            self.contrasena,
            self.ocupacion,
            self.privilegios,
        )

    @abstractmethod
    def es_administrador(self):
        pass

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def contrasena(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, contrasena):
        self.__contrasena = contrasena

    @property
    def ocupacion(self):
        return self.__ocupacion

    @ocupacion.setter
    def ocupacion(self, ocupacion):
        self.__ocupacion = ocupacion

    @property
    def privilegios(self):
        return self.__privilegios

    @privilegios.setter
    def privilegios(self, privilegios):
        self.__privilegios = privilegios

    def __str__(self):
        return f"Usuario: {self.nombre}, Ocupacion: {self.ocupacion}, Privilegios: {self.privilegios}"
