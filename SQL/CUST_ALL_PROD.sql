CREATE DATABASE CUST_ALL_PROD;

USE CUST_ALL_PROD;

CREATE TABLE Product (
    product_key INT PRIMARY KEY
);

CREATE TABLE Customer (
    customer_id INT NOT NULL,
    product_key INT,
    FOREIGN KEY (product_key) REFERENCES Product(product_key)
);

-- Inserting data into the Product table
INSERT INTO Product (product_key) VALUES
(5),
(6);

-- Inserting data into the Customer table
INSERT INTO Customer (customer_id, product_key) VALUES
(1, 5),
(2, 6),
(3, 5),
(3, 6),
(1, 6);

SELECT * FROM Customer;

SELECT DISTINCT PRODUCT_KEY FROM PRODUCT;

WITH ProductCount AS (
    SELECT COUNT(DISTINCT PRODUCT_KEY) AS total_products FROM Product
),
CustomerProductCount AS (
    SELECT customer_id, COUNT(DISTINCT product_key) AS product_count
    FROM Customer
    GROUP BY customer_id
)
SELECT DISTINCT c.customer_id
FROM CustomerProductCount c
JOIN ProductCount p ON c.product_count = p.total_products;

-- OR
select customer_id from customer
group by customer_id
having count( distinct product_key) >= 
            (select count(product_key) from product);