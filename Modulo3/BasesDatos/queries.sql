-- Asegura que las FKs funcionen
PRAGMA foreign_keys = ON;

CREATE TABLE Cliente (
    ID_Cliente INTEGER PRIMARY KEY,
    Correo_Electronico TEXT NOT NULL
);

CREATE TABLE Productos (
    Codigo_Producto INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Precio REAL NOT NULL,
    Fecha_Ingreso TEXT,
    Marca TEXT
);

CREATE TABLE Carrito_Compras (
    ID_Carrito INTEGER PRIMARY KEY,
    ID_Cliente INTEGER NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
);

CREATE TABLE Carrito_Productos (
    ID_CarritoProductos INTEGER PRIMARY KEY,
    ID_Carrito INTEGER NOT NULL,
    Codigo_Producto INTEGER NOT NULL,
    Cantidad INTEGER NOT NULL,
    FOREIGN KEY (ID_Carrito) REFERENCES Carrito_Compras(ID_Carrito),
    FOREIGN KEY (Codigo_Producto) REFERENCES Productos(Codigo_Producto)
);

CREATE TABLE Factura (
    Numero_Factura INTEGER PRIMARY KEY,
    Fecha_Compra TEXT NOT NULL,
    ID_Cliente INTEGER NOT NULL,
    Monto_Total REAL NOT NULL,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
);

CREATE TABLE Productos_Factura (
    ID_ProductosFactura INTEGER PRIMARY KEY,
    Numero_Factura INTEGER NOT NULL,
    Codigo_Producto INTEGER NOT NULL,
    Cantidad INTEGER NOT NULL,
    FOREIGN KEY (Numero_Factura) REFERENCES Factura(Numero_Factura),
    FOREIGN KEY (Codigo_Producto) REFERENCES Productos(Codigo_Producto)
);


-- Modificar tabla facturas

ALTER TABLE Factura
ADD COLUMN Telefono_Comprador TEXT;

ALTER TABLE Factura
ADD COLUMN Codigo_Empleado TEXT;

-- Agregar datos a las tablas

INSERT INTO Cliente (ID_Cliente, Correo_Electronico) VALUES
(1, 'juan@example.com'),
(2, 'maria@example.com');

INSERT INTO Productos (Codigo_Producto, Nombre, Precio, Fecha_Ingreso, Marca) VALUES
(100, 'Silla Gamer',       150000, '2023-10-01', 'Razer'),
(101, 'Teclado Mecánico',  60000,  '2023-11-05', 'Logitech'),
(102, 'Monitor 24"',       250000, '2023-09-15', 'LG');

INSERT INTO Productos (Codigo_Producto, Nombre, Precio, Fecha_Ingreso, Marca) VALUES
(103, 'Silla Gamer',       45000, '2023-10-02', 'Razer'),
(104, 'Teclado Mecánico',  38000,  '2023-12-05', 'Logitech'),
(105, 'Monitor 24"',       270000, '2023-09-19', 'LG');

INSERT INTO Carrito_Compras (ID_Carrito, ID_Cliente) VALUES
(1, 1),
(2, 2);

INSERT INTO Carrito_Productos (ID_CarritoProductos, ID_Carrito, Codigo_Producto, Cantidad) VALUES
(1, 1, 100, 2),  
(2, 1, 101, 1),  
(3, 2, 102, 3);  

INSERT INTO Factura (
  Numero_Factura,
  Fecha_Compra,
  ID_Cliente,
  Monto_Total,
  Telefono_Comprador,
  Codigo_Empleado
) 
VALUES
(500, '2023-12-01', 1, 360000, '3001234567', 'EMP001'),
(501, '2023-12-02', 2, 250000, '3012345678', 'EMP002');

INSERT INTO Factura (
  Numero_Factura,
  Fecha_Compra,
  ID_Cliente,
  Monto_Total,
  Telefono_Comprador,
  Codigo_Empleado
) 
VALUES
(502, '2023-12-01', 1, 360000, '3001234567', 'EMP001'),
(503, '2023-12-02', 1, 250000, '3012345678', 'EMP001');

INSERT INTO Productos_Factura (ID_ProductosFactura, Numero_Factura, Codigo_Producto, Cantidad) VALUES
(1, 500, 100, 2), 
(2, 500, 101, 1), 
(3, 501, 102, 1);

INSERT INTO Productos_Factura (ID_ProductosFactura, Numero_Factura, Codigo_Producto, Cantidad) VALUES
(4, 502, 100, 2), 
(5, 502, 100, 1), 
(6, 501, 101, 1); 

-- Consultas
-- 1 Obtener todos los productos almacenados
SELECT * 
FROM Productos;
-- 2 Obtener todos los productos que tengan un precio mayor a 50000
SELECT * 
FROM Productos
WHERE Precio > 50000;
-- 3 Obtener todas las compras de un mismo producto por id
SELECT *
FROM Productos_Factura
WHERE Codigo_Producto = 101;

-- 4 Obtener todas las compras de un mismo producto mostrando el total comprado
SELECT 
    Codigo_Producto,
    SUM(Cantidad) AS Total_Comprado
FROM Productos_Factura
GROUP BY Codigo_Producto;

--5 Obtener todas las facturas realizadas por el mismo comprador
SELECT *
FROM Factura
WHERE ID_Cliente = 1;

SELECT *
FROM Factura
WHERE Telefono_Comprador = '3001234567';

-- 7 Obtener una factura por su codigo o numero de factura
SELECT *
FROM Factura
WHERE Numero_Factura = 500;
