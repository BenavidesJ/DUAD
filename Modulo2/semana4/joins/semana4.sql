-- Creacion de Tablas
CREATE TABLE Books (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Author INTEGER
);

CREATE TABLE Authors (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL
);

CREATE TABLE Customers (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL
);

CREATE TABLE Rents (
    ID INTEGER PRIMARY KEY,
    BookID INTEGER,
    CustomerID INTEGER,
    State TEXT NOT NULL,
    FOREIGN KEY (BookID) REFERENCES Books(ID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(ID)
);

-- Insercion de Datos
INSERT INTO Books (ID, Name, Author) VALUES
(1, 'Don Quijote', 1),
(2, 'La Divina Comedia', 2),
(3, 'Vagabond 1-3', 3),
(4, 'Dragon Ball 1', 4),
(5, 'The Book of the 5 Rings', NULL);

INSERT INTO Authors (ID, Name) VALUES
(1, 'Miguel de Cervantes'),
(2, 'Dante Alighieri'),
(3, 'Takehiko Inoue'),
(4, 'Akira Toriyama'),
(5, 'Walt Disney');

INSERT INTO Customers (ID, Name, Email) VALUES
(1, 'John Doe', 'j.doe@email.com'),
(2, 'Jane Doe', 'jane@doe.com'),
(3, 'Luke Skywalker', 'darth.son@email.com');

INSERT INTO Rents (ID, BookID, CustomerID, State) VALUES
(1, 1, 2, 'Returned'),
(2, 2, 2, 'Returned'),
(3, 1, 1, 'On time'),
(4, 3, 1, 'On time'),
(5, 2, 2, 'Overdue');

-- Consultas
-- 1. Obtenga todos los libros y sus autores
SELECT Books.Name AS BookName, Authors.Name AS AuthorName
FROM Books
LEFT JOIN Authors ON Books.Author = Authors.ID;

-- 2. Obtenga todos los libros que no tienen autor
SELECT Books.Name AS BookName
FROM Books
WHERE Author IS NULL;

-- 3. Obtenga todos los autores que no tienen libros
SELECT Authors.Name AS AuthorName
FROM Authors
LEFT JOIN Books ON Authors.ID = Books.Author
WHERE Books.ID IS NULL;

-- 4. Obtenga todos los libros que han sido rentados en algún momento
SELECT DISTINCT Books.Name AS BookName
FROM Books
INNER JOIN Rents ON Books.ID = Rents.BookID;

-- 5. Obtenga todos los libros que nunca han sido rentados
SELECT Books.Name AS BookName
FROM Books
LEFT JOIN Rents ON Books.ID = Rents.BookID
WHERE Rents.ID IS NULL;

-- 6. Obtenga todos los clientes que nunca han rentado un libro
SELECT Customers.Name AS CustomerName
FROM Customers
LEFT JOIN Rents ON Customers.ID = Rents.CustomerID
WHERE Rents.ID IS NULL;

-- 7. Obtenga todos los libros que han sido rentados y están en estado “Overdue”
SELECT Books.Name AS BookName
FROM Books
INNER JOIN Rents ON Books.ID = Rents.BookID
WHERE Rents.State = 'Overdue';