CREATE DATABASE EMPLOYEE;

USE EMPLOYEE;

CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department CHAR(1),
    managerId INT,
    FOREIGN KEY (managerId) REFERENCES Employee(id)
);


INSERT INTO Employee (id, name, department, managerId) VALUES
(101, 'John', 'A', NULL),
(102, 'Dan', 'A', 101),
(103, 'James', 'A', 101),
(104, 'Amy', 'A', 101),
(105, 'Anne', 'A', 101),
(106, 'Ron', 'B', 101);


SELECT NAME FROM EMPLOYEE WHERE ID IN (SELECT MANAGERID FROM EMPLOYEE GROUP BY MANAGERID HAVING COUNT(*)>=5);