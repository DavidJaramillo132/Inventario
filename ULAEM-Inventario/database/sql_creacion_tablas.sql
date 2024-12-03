-- Verificar si la base de datos 'uleam' existe, y crearla si no existe
IF NOT EXISTS (
    SELECT 1
    FROM sys.databases
    WHERE name = 'uleam'
)
BEGIN
    CREATE DATABASE uleam;
END;

-- Usar la base de datos 'uleam'
USE uleam;

-- Crear tabla Usuario si no existe
IF NOT EXISTS (
    SELECT
        1
    FROM
        sys.tables
    WHERE
        name = 'Usuario'
) BEGIN CREATE TABLE Usuario (
    cedula VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    contrasena VARCHAR(100) NOT NULL,
    ocupacion VARCHAR(50) NOT NULL,
    privilegios VARCHAR(255) NOT NULL
);
-- Insertar usuario admin
END;

--select * from Usuario;

-- Crear tabla Aula si no existe
IF NOT EXISTS (
    SELECT
        1
    FROM
        sys.tables
    WHERE
        name = 'Aula'
) BEGIN CREATE TABLE Aula (
    idAula INT PRIMARY KEY,
    dimensiones INT NOT NULL,
    tipo VARCHAR(100) NOT NULL
);

END;

-- Crear tabla Comentario si no existe
IF NOT EXISTS (
    SELECT
        1
    FROM
        sys.tables
    WHERE
        name = 'Comentario'
) BEGIN CREATE TABLE Comentario (
    idComentario INT IDENTITY PRIMARY KEY,
    contenido VARCHAR(MAX) NOT NULL,
    fechaCreacion DATE DEFAULT GETDATE(),
    idAula INT NOT NULL,
    cedula varchar(10),
    FOREIGN KEY (idAula) REFERENCES Aula(idAula) ON DELETE CASCADE,
    FOREIGN KEY (cedula) REFERENCES Usuario(cedula) ON DELETE CASCADE
);

END;

-- Crear tabla Elemento si no existe
IF NOT EXISTS (
    SELECT
        1
    FROM
        sys.tables
    WHERE
        name = 'Elemento'
) BEGIN CREATE TABLE Elemento (
    idElemento INT IDENTITY PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(100) NOT NULL,
    estado VARCHAR(100) NOT NULL,
    fechaAdquisicion DATE NOT NULL,
    cantidad INT NOT NULL,
    idAula INT NOT NULL,
    FOREIGN KEY (idAula) REFERENCES Aula(idAula) ON DELETE CASCADE
);

END;