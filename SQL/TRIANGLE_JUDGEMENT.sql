CREATE DATABASE TRIANGLE_JUDGEMENT;

USE TRIANGLE_JUDGEMENT;

CREATE TABLE Triangle (
    x INT,
    y INT,
    z INT,
    PRIMARY KEY (x, y, z)
);

INSERT INTO Triangle (x, y, z) VALUES
(13, 15, 30),
(10, 20, 15);

SELECT * FROM TRIANGLE;

SELECT x, y, z,
    CASE 
        WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;

-- SOLUTION 2

select x,y,z, case when x+y<= z or x+z<=y or y+z<=x then 'No'
else 'Yes' end triangle 
from triangle;

