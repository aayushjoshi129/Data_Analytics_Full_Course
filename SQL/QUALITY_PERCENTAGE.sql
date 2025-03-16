CREATE DATABASE QUALITY_PERCENTAGE;

USE QUALITY_PERCENTAGE;

CREATE TABLE Queries (
    query_name VARCHAR(50),
    result VARCHAR(100),
    position INT,
    rating INT
);


INSERT INTO Queries (query_name, result, position, rating)
VALUES
('Dog', 'Golden Retriever', 1, 5),
('Dog', 'German Shepherd', 2, 5),
('Dog', 'Mule', 200, 1),
('Cat', 'Shirazi', 5, 2),
('Cat', 'Siamese', 3, 3),
('Cat', 'Sphynx', 7, 4);

SELECT * FROM QUERIES;

SELECT QUERY_NAME, ROUND(SUM(CAST(RATING AS FLOAT)/POSITION)/COUNT(QUERY_NAME),2) AS QUALITY, 
ROUND(CAST(SUM(CASE WHEN RATING<3 THEN 1 ELSE 0 END) AS FLOAT)/COUNT(*) * 100,2) AS POOR_QUERY_PERCENTAGE
FROM QUERIES GROUP BY QUERY_NAME;

