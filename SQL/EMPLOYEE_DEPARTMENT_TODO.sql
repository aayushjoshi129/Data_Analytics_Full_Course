CREATE DATABASE EMPLOYEE_DEPARTMENT;

USE EMPLOYEE_DEPARTMENT;

CREATE TABLE Employee (
    employee_id INT,
    department_id INT,
    primary_flag VARCHAR(1),
    PRIMARY KEY (employee_id, department_id)
);

INSERT INTO Employee (employee_id, department_id, primary_flag) VALUES
(1, 1, 'N'),
(2, 1, 'Y'),
(2, 2, 'N'),
(3, 3, 'N'),
(4, 2, 'N'),
(4, 3, 'Y'),
(4, 4, 'N');

SELECT employee_id,department_id FROM Employee WHERE (primary_flag = 'Y' 
OR employee_id NOT IN(SELECT employee_id FROM Employee WHERE primary_flag = 'Y'))



