CREATE DATABASE CLASS_GT_5_STUD;

USE CLASS_GT_5_STUD;

CREATE TABLE Courses (
    student VARCHAR(255),
    class VARCHAR(255),
    PRIMARY KEY (student, class)
);


INSERT INTO Courses (student, class) VALUES
('A', 'Math'),
('B', 'English'),
('C', 'Math'),
('D', 'Biology'),
('E', 'Math'),
('F', 'Computer'),
('G', 'Math'),
('H', 'Math'),
('I', 'Math');

SELECT * FROM COURSES;

SELECT CLASS FROM COURSES GROUP BY CLASS HAVING COUNT(CLASS)>=5;