CREATE DATABASE PRODUCT_PRICE_GIVEN_DATE;

USE PRODUCT_PRICE_GIVEN_DATE;

CREATE TABLE Products (
    product_id INT,
    new_price INT,
    change_date DATE,
    PRIMARY KEY (product_id, change_date)
);


INSERT INTO Products (product_id, new_price, change_date)
VALUES 
(1, 20, '2019-08-14'),
(2, 50, '2019-08-14'),
(1, 30, '2019-08-15'),
(1, 35, '2019-08-16'),
(2, 65, '2019-08-17'),
(3, 20, '2019-08-18');


SELECT * FROM Products;

WITH LatestPrice AS (
    SELECT 
        product_id,
        new_price,
        change_date,
        ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT 
    p.product_id,
    COALESCE(lp.new_price, 10) AS price
FROM 
    (SELECT DISTINCT product_id FROM Products) p
LEFT JOIN 
    LatestPrice lp ON p.product_id = lp.product_id AND lp.rn = 1;




-- OR


SELECT 
    p.product_id, 
    COALESCE((
        SELECT TOP 1 new_price 
        FROM Products p2 
        WHERE p2.product_id = p.product_id AND p2.change_date <= '2019-08-16'
        ORDER BY p2.change_date DESC
    ), 10) AS price
FROM 
    (SELECT DISTINCT product_id FROM Products) p
ORDER BY 
    p.product_id;

