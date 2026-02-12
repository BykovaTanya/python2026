DROP TABLE Orders;
DROP TABLE Customers;



CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT,
    LastName TEXT,
	Email TEXT
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER, 
	OrderDate TEXT CHECK (OrderDate is date(OrderDate)),
	TotalAmount REAL,
	FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
INSERT INTO Customers (CustomerID, FirstName, LastName,Email )
VALUES (1, "John", "Doe", "johndoe@example.com"),
       (2, "Jane", "Smith", "janesmith@example.com");

INSERT INTO Orders (OrderID, CustomerID,OrderDate,TotalAmount)
VALUES (101, 1, "2025-02-01", 100.50),
       (102, 2, "2025-02-02", 200.75);
 
SELECT Customers.FirstName, Customers.LastName, Orders.OrderID, Orders.TotalAmount
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID;	
--[запрос A]
SELECT Customers.FirstName, Customers.LastName, Orders.OrderID, Orders.TotalAmount
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID; 
--[запрос B]
SELECT FirstName, LastName, NULL AS OrderID, NULL AS TotalAmount
FROM Customers
UNION
SELECT NULL, NULL, OrderID, TotalAmount FROM Orders;

SELECT OrderID, CustomerID, OrderDate, TotalAmount FROM Orders
EXCEPT
SELECT CustomerID, FirstName, LastName, Email FROM Customers;

