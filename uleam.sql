create database uleam;

create table Historial(
idHistorial int identity primary key,
cedula varchar(10), --clave foranea hacia usuario
fecha date not null,
foreign key (cedula) references Usuario(cedula)
);

create table Usuario(
cedula varchar(10) check (len(cedula) = 10) primary key, --identificar a cada usuario
nombre varchar(100) not null,
email varchar(100) not null unique,
contrase�a varchar(100) not null,
rango varchar(50) not null
);



create table Aula(
idAula int primary key,
tama�o int not null,
tipo varchar(100) not null
);

create table Comentario (
idComentario int identity primary key,
contenido varchar(max) not null,
fechaCreacion date default getdate(), --La fecha de creaci�n del comentario
idAula int not null,
cedula varchar(10) not null,
foreign key (idAula) references Aula(idAula), -- relaci�n con Aula
foreign key (cedula) references Usuario(cedula) -- relaci�n con Usuario
);

create table Comentario (
    idComentario int identity primary key,
    contenido varchar(MAX) not null,
    fechaCreacion date default getdate(), -- La fecha de creaci�n del comentario
    idAula int not null,
    cedula varchar(10) not null,
    foreign key (idAula) references Aula(idAula), -- relaci�n con Aula
    foreign key (cedula) references Usuario(cedula) on delete cascade -- relaci�n con Usuario, permite eliminaci�n en cascada
);

create table Elemento (
IdElemento int identity primary key,
nombre varchar(100) not null,
tipo varchar(100) not null,
estado varchar(100) not null,
fechAdquisicion date not null,
cantidad int not null,
idAula  INT not null, -- Relaci�n con Inventario
foreign key (idAula) REFERENCES Aula(idAula)
);


CREATE TABLE Usuario_Aula (
    cedula VARCHAR(10),
    idAula INT,
    PRIMARY KEY (cedula, idAula),
    FOREIGN KEY (cedula) REFERENCES Usuario(cedula),
    FOREIGN KEY (idAula) REFERENCES Aula(idAula)
);







--
ALTER TABLE Comentario
DROP CONSTRAINT FK__Comentari__idAul__1EA48E88;

ALTER TABLE Elemento
DROP CONSTRAINT FK__Elemento__idAula__160F4887;

-- Ahora agrega las claves for�neas con ON DELETE CASCADE
ALTER TABLE Comentario
ADD CONSTRAINT FK__Comentari__idAul__1EA48E88
FOREIGN KEY (idAula) REFERENCES Aula(idAula) ON DELETE CASCADE;

ALTER TABLE Elemento
ADD CONSTRAINT FK__Elemento__idAula__160F4887
FOREIGN KEY (idAula) REFERENCES Aula(idAula) ON DELETE CASCADE;


------
ALTER TABLE Comentario
DROP CONSTRAINT FK_Comentario__cedul__1F98B2C1;

ALTER TABLE Comentario
ADD CONSTRAINT FK_Comentario__cedul__1F98B2C1
FOREIGN KEY (cedula) REFERENCES Usuarios(cedula)
ON DELETE CASCADE;