CREATE DATABASE CONSECUTIVE_NUMBERS;

USE CONSECUTIVE_NUMBERS;

CREATE TABLE Logs (
    id INT IDENTITY(1,1) PRIMARY KEY,
    num VARCHAR(255)
);

INSERT INTO Logs (num) VALUES
('1'),
('1'),
('1'),
('2'),
('1'),
('2'),
('2');

SELECT * FROM LOGS;

SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1
JOIN Logs l3 ON l2.id = l3.id - 1
WHERE l1.num = l2.num AND l2.num = l3.num;
