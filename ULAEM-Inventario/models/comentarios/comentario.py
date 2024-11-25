from ..baseAbstractClass import BaseAbstractClass


class Comentario(BaseAbstractClass):
    def __init__(self, idComentario, contenido, fechaCreacion, idAula, cedula):
        self.idComentario = idComentario
        self.contenido = contenido
        self.fechaCreacion = fechaCreacion
        self.idAula = idAula
        self.cedula = cedula

    def get_datos(self):
        return (
            self.idComentario,
            self.contenido,
            self.fechaCreacion,
            self.idAula,
            self.cedula,
        )

    def update_datos(self):
        pass
