USE EMPLOYEE;

CREATE TABLE EMPLOYEE_SAL (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(10, 2),
    department VARCHAR(50)
);

INSERT INTO EMPLOYEE_SAL (employee_id, first_name, last_name, salary, department) VALUES
(1, 'John', 'Doe', 50000.00, 'HR'),
(2, 'Jane', 'Smith', 60000.00, 'IT'),
(3, 'Sam', 'Brown', 70000.00, 'Finance'),
(4, 'Lisa', 'White', 80000.00, 'Marketing'),
(5, 'Tom', 'Green', 90000.00, 'IT'),
(6, 'Anna', 'Black', 75000.00, 'Finance'),
(7, 'Steve', 'Blue', 85000.00, 'HR'),
(8, 'Emma', 'Gray', 95000.00, 'Marketing'),
(9, 'Chris', 'Red', 65000.00, 'IT'),
(10, 'Kelly', 'Purple', 55000.00, 'HR');


SELECT * FROM EMPLOYEE_SAL ORDER BY SALARY DESC;

-- NTH HIGHEST
-- SELECT * FROM EMPLOYEE_SAL E1 WHERE N-1 = (SELECT COUNT(DISTINCT SALARY) FROM EMPLOYEE_SAL E2 WHERE E2.SALARY>E1.SALARY)

-- 4TH HIGHEST
SELECT * FROM EMPLOYEE_SAL E1 WHERE 4-1 = (SELECT COUNT(DISTINCT SALARY) FROM EMPLOYEE_SAL E2 WHERE E2.SALARY>E1.SALARY);
