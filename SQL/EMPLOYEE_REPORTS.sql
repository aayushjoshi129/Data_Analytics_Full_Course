CREATE DATABASE EMPLOYEE_REPORTS;

USE EMPLOYEE_REPORTS;

CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    reports_to INT NULL,
    age INT,
    FOREIGN KEY (reports_to) REFERENCES Employees(employee_id)
);


INSERT INTO Employees (employee_id, name, reports_to, age) VALUES
(9, 'Hercy', NULL, 43),
(6, 'Alice', 9, 41),
(4, 'Bob', 9, 36),
(2, 'Winston', NULL, 37);


SELECT * FROM Employees;

WITH CTE_DETAILS AS (
SELECT REPORTS_TO AS EMPLOYEE_ID, COUNT(DISTINCT EMPLOYEE_ID) AS REPORTS_COUNT, 
ROUND(AVG(CAST(AGE AS FLOAT)), 0) AS AVERAGE_AGE FROM EMPLOYEES WHERE REPORTS_TO IS NOT NULL
GROUP BY REPORTS_TO)

SELECT C.EMPLOYEE_ID, E.NAME, C.REPORTS_COUNT, C.AVERAGE_AGE 
FROM CTE_DETAILS C JOIN EMPLOYEES E ON C.EMPLOYEE_ID = E.EMPLOYEE_ID ORDER BY C.EMPLOYEE_ID;

-- TYPE 2
SELECT e.employee_id, 
       e.name, 
       COUNT(r.employee_id) AS reports_count, 
       ROUND(AVG(r.age), 0) AS average_age
FROM Employees e
JOIN Employees r ON e.employee_id = r.reports_to
GROUP BY e.employee_id, e.name
ORDER BY e.employee_id;

