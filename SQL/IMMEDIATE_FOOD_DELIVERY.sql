CREATE DATABASE IMMEDIATE_FOOD_DELIVERY;

USE IMMEDIATE_FOOD_DELIVERY;

-- Create the Delivery table
CREATE TABLE Delivery (
    delivery_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    customer_pref_delivery_date DATE
);

-- Insert data into the Delivery table
INSERT INTO Delivery (delivery_id, customer_id, order_date, customer_pref_delivery_date)
VALUES
(1, 1, '2019-08-01', '2019-08-02'),
(2, 2, '2019-08-02', '2019-08-02'),
(3, 1, '2019-08-11', '2019-08-12'),
(4, 3, '2019-08-24', '2019-08-24'),
(5, 3, '2019-08-21', '2019-08-22'),
(6, 2, '2019-08-11', '2019-08-13'),
(7, 4, '2019-08-09', '2019-08-09');


SELECT * FROM Delivery;

WITH CTE_RANK AS (
SELECT CUSTOMER_ID, ORDER_DATE, customer_pref_delivery_date, RANK()  
	OVER (PARTITION BY CUSTOMER_ID ORDER BY CUSTOMER_ID ASC, order_date ASC) AS RANK_NUM
FROM DELIVERY
)

SELECT ROUND(SUM(CASE WHEN ORDER_DATE = customer_pref_delivery_date THEN 1 ELSE 0 END)/
CAST(COUNT(CUSTOMER_ID) AS FLOAT)*100,2) AS IMMEDIATE_PERCENTAGE
FROM CTE_RANK WHERE RANK_NUM=1


