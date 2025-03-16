CREATE DATABASE PRODUCT_SALES_ANALYSIS;

USE PRODUCT_SALES_ANALYSIS;

-- Create the Product table
CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255)
);

-- Create the Sales table
CREATE TABLE Sales (
    sale_id INT,
    product_id INT,
    year INT,
    quantity INT,
    price INT,
    PRIMARY KEY (sale_id, year),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- Insert sample data into the Product table
INSERT INTO Product (product_id, product_name) VALUES
(100, 'Nokia'),
(200, 'Apple'),
(300, 'Samsung');

-- Insert sample data into the Sales table
INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2008, 10, 5000),
(2, 100, 2009, 12, 5000),
(3, 200, 2011, 15, 9000);

SELECT * FROM PRODUCT;

SELECT * FROM SALES;

WITH FirstSale AS (
    SELECT 
        product_id, 
        MIN(year) AS first_year
    FROM 
        Sales
    GROUP BY 
        product_id
)
SELECT 
    s.product_id, 
    fs.first_year, 
    s.quantity, 
    s.price
FROM 
    FirstSale fs
JOIN 
    Sales s ON fs.product_id = s.product_id AND fs.first_year = s.year;




