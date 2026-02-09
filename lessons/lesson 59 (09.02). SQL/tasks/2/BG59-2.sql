DROP TABLE students;
CREATE TABLE students (
    ID INTEGER PRIMARY KEY,
    username TEXT,
    age INTEGER
);
INSERT INTO students(id,username,age) VALUES (1, "Иван", 20);
INSERT INTO students(id,username,age) VALUES (2, "Мария", 22);
INSERT INTO students(id,username,age) VALUES (3, "Петр", 19);
SELECT * FROM students;

DROP TABLE employees;
CREATE TABLE employees (
    ID INTEGER PRIMARY KEY,
    name TEXT,
    position TEXT,
	salary INTEGER
);
INSERT INTO employees(ID,name,position,salary) VALUES (1, "Анна", "Разработчик", 50000);
INSERT INTO employees(ID,name,position,salary) VALUES (2, "Олег", "Менеджер", 60000);
INSERT INTO employees(ID,name,position,salary) VALUES (3, "Елена", "Дизайнер", 45000);
UPDATE employees SET salary = 65000 WHERE id = 2;
SELECT * FROM employees;

DROP TABLE goods;
CREATE TABLE goods (
    ID INTEGER PRIMARY KEY,
    name TEXT,
    price INTEGER,
	quantity INTEGER
);
INSERT INTO goods(ID,name,price,quantity) VALUES (1, "Ноутбук", 45000, 10);
INSERT INTO goods(ID,name,price,quantity) VALUES (2, "Мышь", 1500, 50);
INSERT INTO goods(ID,name,price,quantity) VALUES (3, "Клавиатура", 3000, 25);
INSERT INTO goods(ID,name,price,quantity) VALUES (4, "Монитор", 12000, 15);
DELETE FROM goods WHERE id = 3;
SELECT * FROM goods;

