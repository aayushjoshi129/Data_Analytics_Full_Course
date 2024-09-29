CREATE DATABASE CONFIRMATION_RATE;

USE CONFIRMATION_RATE;

CREATE TABLE Signups (
    user_id INT PRIMARY KEY,
    time_stamp DATETIME
);

INSERT INTO Signups (user_id, time_stamp) VALUES
(3, '2020-03-21 10:16:13'),
(7, '2020-01-04 13:57:59'),
(2, '2020-07-29 23:09:44'),
(6, '2020-12-09 10:39:37');


CREATE TABLE Confirmations (
    user_id INT,
    time_stamp DATETIME,
    action VARCHAR(10),
    PRIMARY KEY (user_id, time_stamp),
    FOREIGN KEY (user_id) REFERENCES Signups(user_id),
    CHECK (action IN ('confirmed', 'timeout'))
);

INSERT INTO Confirmations (user_id, time_stamp, action) VALUES
(3, '2021-01-06 03:30:46', 'timeout'),
(3, '2021-07-14 14:00:00', 'timeout'),
(7, '2021-06-12 11:57:29', 'confirmed'),
(7, '2021-06-13 12:58:28', 'confirmed'),
(7, '2021-06-14 13:59:27', 'confirmed'),
(2, '2021-01-22 00:00:00', 'confirmed'),
(2, '2021-02-28 23:59:59', 'timeout');


SELECT * FROM Confirmations;

SELECT * FROM Signups;


SELECT S.user_id, (SUM(CASE WHEN UPPER(ACTION)='CONFIRMED' THEN 1.00 ELSE 0.00 END)*1 / COUNT(ISNULL(ACTION,1))) AS CONFIRMATION_RATE 
FROM SIGNUPS S LEFT JOIN Confirmations C ON S.user_id = C.user_id GROUP BY S.USER_ID

--OR

SELECT S.user_id, ROUND(AVG(CASE WHEN UPPER(ACTION)='CONFIRMED' THEN 1.00 ELSE 0.00 END),2) AS CONFIRMATION_RATE 
FROM SIGNUPS S LEFT JOIN Confirmations C ON S.user_id = C.user_id GROUP BY S.USER_ID
