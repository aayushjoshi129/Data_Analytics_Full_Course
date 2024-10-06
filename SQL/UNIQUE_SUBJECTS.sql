CREATE DATABASE UNIQUE_SUBJECTS;

USE UNIQUE_SUBJECTS;

CREATE TABLE Teacher (
    teacher_id INT,
    subject_id INT,
    dept_id INT,
    PRIMARY KEY (subject_id, dept_id)
);

INSERT INTO Teacher (teacher_id, subject_id, dept_id)
VALUES
(1, 2, 3),
(1, 2, 4),
(1, 3, 3),
(2, 1, 1),
(2, 2, 1),
(2, 3, 1),
(2, 4, 1);

SELECT * FROM Teacher;

SELECT TEACHER_ID, COUNT(DISTINCT SUBJECT_ID) AS CNT FROM TEACHER GROUP BY TEACHER_ID;


