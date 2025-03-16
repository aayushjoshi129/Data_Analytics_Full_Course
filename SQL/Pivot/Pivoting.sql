CREATE DATABASE PIVOT_DB;

USE PIVOT_DB;

CREATE TABLE Store_Information (
    Store_Name VARCHAR(50),
    Sales INT,
    Txn_Date DATE
);


INSERT INTO Store_Information (Store_Name, Sales, Txn_Date)
VALUES 
('Los Angeles', 1500, '1999-01-05'),
('San Diego', 250, '1999-01-07'),
('Los Angeles', 300, '1999-01-08'),
('Boston', 700, '1999-01-08');


select * from Store_Information;


CREATE TABLE Geography (
    Region_Name VARCHAR(50),
    Store_Name VARCHAR(50)
);



INSERT INTO Geography (Region_Name, Store_Name)
VALUES 
('East', 'Boston'),
('East', 'New York'),
('West', 'Los Angeles'),
('West', 'San Diego');


select * from Geography;

SELECT SUM(Sales) FROM Store_Information
WHERE EXISTS
(SELECT * FROM Geography
WHERE Region_Name = 'East');




SELECT Store_Name, CASE Store_Name
  WHEN 'Los Angeles' THEN Sales * 2
  WHEN 'San Diego' THEN Sales * 1.5
  ELSE Sales
  END
"New Sales",
Txn_Date
FROM Store_Information;


CREATE TABLE Total_Sales (
    Year INT,
    Store VARCHAR(50),
    Sales INT
);

INSERT INTO Total_Sales (Year, Store, Sales)
VALUES 
(2020, 'Chicago', 100),
(2020, 'Phoenix', 200),
(2020, 'London', 250),
(2021, 'Chicago', 200),
(2021, 'Phoenix', 400),
(2021, 'London', 550),
(2022, 'Chicago', 300),
(2022, 'Phoenix', 150),
(2022, 'London', 220);

select * from Total_Sales;

SELECT Store, Year, SUM(Sales) Sales_Sum
FROM Total_Sales
GROUP BY Store, Year;


SELECT * FROM
(
    SELECT Store, Year, SUM(Sales) AS Sales
    FROM Total_Sales
    GROUP BY Store, Year
) AS SourceTable
PIVOT
(
    SUM(Sales)
    FOR Year IN ([2020], [2021], [2022])
) AS PivotTable;



select * from (
select Store, Year, Sales from Total_Sales
) AS SourceTable
PIVOT
( 
SUM(Sales) FOR YEAR IN ([2020],[2021], [2022])
)
AS PIVOT_TABLE



CREATE TABLE olympic_medal_winners (
    Olympic_year INT,
    sport VARCHAR(50),
    gender CHAR(1),
    event VARCHAR(100),
    medal VARCHAR(10),
    Con CHAR(3),  -- Country 3 letters
    athlete VARCHAR(100)
);

-- Insert dummy data
INSERT INTO olympic_medal_winners (Olympic_year, sport, gender, event, medal, Con, athlete)
VALUES 
(2016, 'Archery', 'M', 'Men''s Individual', 'Gold', 'BRA', 'MARIANO Arthur'),
(2016, 'Archery', 'F', 'Women''s Individual', 'Silver', 'USA', 'JOHNSON Emily'),
(2020, 'Swimming', 'M', 'Men''s 100m Freestyle', 'Gold', 'AUS', 'SMITH Michael'),
(2020, 'Swimming', 'F', 'Women''s 100m Freestyle', 'Bronze', 'CAN', 'LEE Sarah'),
(2016, 'Athletics', 'M', 'Men''s 100m', 'Gold', 'JAM', 'BOLT Usain'),
(2020, 'Athletics', 'F', 'Women''s 200m', 'Silver', 'GBR', 'THOMPSON Elaine'),
(2012, 'Gymnastics', 'M', 'Men''s All-Around', 'Bronze', 'JPN', 'UCHIMURA Kohei'),
(2016, 'Gymnastics', 'F', 'Women''s Floor', 'Gold', 'USA', 'BILES Simone'),
(2020, 'Basketball', 'M', 'Men''s Team', 'Gold', 'USA', 'DURANT Kevin'),
(2020, 'Basketball', 'F', 'Women''s Team', 'Silver', 'FRA', 'DUPONT Sandrine');


SELECT * FROM olympic_medal_winners;

-- which country won which and how many medals 

SELECT * FROM (
SELECT CON, MEDAL FROM olympic_medal_winners
) AS INT_TABLE
PIVOT
(
COUNT(MEDAL) FOR MEDAL IN (
[Gold], [Silver], [Bronze]
)
) AS PIVOT_MEDAL

