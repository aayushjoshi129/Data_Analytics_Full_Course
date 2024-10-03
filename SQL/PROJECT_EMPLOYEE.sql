CREATE DATABASE PROJECT_EMPLOYEE;

USE PROJECT_EMPLOYEE;

CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    experience_years INT
);

INSERT INTO Employee (employee_id, name, experience_years)
VALUES
(1, 'Khaled', 3),
(2, 'Ali', 2),
(3, 'John', 1),
(4, 'Doe', 2);



CREATE TABLE Project (
    project_id INT,
    employee_id INT,
    FOREIGN KEY (employee_id) REFERENCES Employee(employee_id)
);


INSERT INTO Project (project_id, employee_id)
VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 4);


SELECT PROJECT_ID, ROUND(AVG(CAST(EXPERIENCE_YEARS AS FLOAT)),2) AS AVERAGE_YEARS 
FROM PROJECT P LEFT JOIN EMPLOYEE E ON P.EMPLOYEE_ID = E.EMPLOYEE_ID GROUP BY PROJECT_ID ORDER BY PROJECT_ID ASC;