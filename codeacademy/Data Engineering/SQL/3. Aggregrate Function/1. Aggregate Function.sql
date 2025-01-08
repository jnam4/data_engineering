-- ------------
-- Chapter 3: Aggregate Functions
-- Date: 2025.01.05
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------

-- -------------
-- 0. Drop & Create Tables
-- -------------
DROP TABLE IF EXISTS "fake_apps";
CREATE TABLE IF NOT EXISTS "fake_apps"(
    id INT,
    name TEXT,
    category TEXT,
    downloads INT,
    Price FLOAT
);

-- -------------
-- Check column name
-- -------------
SELECT * FROM fake_apps
-- id, name, category, downloads, price


-- -------------
-- 1. Count 
-- SELECT COUNT()
-- takes the name of column as argument, and return counts of the non-empty records
-- -------------
SELECT COUNT(*)
FROM fake_apps 
WHERE price = 0;
-- count how many free apps 


-- -------------
-- 2. Sum
-- SUM()
-- return the sum of all the values in the column 
-- -------------
SELECT SUM(downloads)
FROM fake_apps;
-- sum all the values in the downloads 


-- -------------
-- 3. Max / Min 
-- Max() Min()
-- takes argument and print out maximum/minimum value 
-- -------------
SELECT MAX(price)
FROM fake_apps;
-- return the price of most expensive app 



-- -------------
-- 4. Average
-- AVG() 
-- return average number of arguments 
-- -------------
SELECT AVG(price)
FROM fake_apps;
-- return average price of app



-- -------------
-- 5. Round 
-- ROUND(column name, integer)
-- return values in the column to 0 decimal places
-- FLOAT- need to use cast :: operator (:: is Postgres specific)
--        round((value::Decimal/Numeric),2)
-- -------------
-- Problem 
SELECT name, ROUND(price, 0) AS price
FROM fake_apps;
-- show error, because price is FLOAT data type 
-- Therefore, need to use (cast :: operator)

-- :: Solution 
SELECT name, ROUND(price::decimal, 0) AS price 
FROM fake_apps;
-- return name and price that rounded by 0 decimal places and rename it to the price 

SELECT ROUND(price::decimal,2)
FROM fake_apps;
-- return avegrage price rounded by second decimal places 
-- normally in sql standards:
SELECT ROUND(price, 2)
FROM fake_apps;



-- -------------
-- 6. Group By-1
-- GROUP BY ()
-- comes after any WHERE 
-- but before ORDER BY or LIMIT
-- -------------
SELECT price, COUNT(*) 
FROM fake_apps
WHERE downloads > 20000
GROUP BY price;
-- return the count of columns in the each price whichever has mnore than 20,000 times of downloads

SELECT category, SUM(downloads)
FROM fake_apps
GROUP BY category;
-- return the category and sum of downloads of each category



-- -------------
-- 7. Group By-2
-- Group By 1,2,3,...
-- each number represent nth of columns 
-- GROUP BY 1:first column 
-- GROUO BY 2:second column 
-- -------------
SELECT category, price, ROUND(AVG(downloads),2)
FROM fake_apps
GROUP BY 1,2;
-- return category, price, average of downloads rounded by two decimal places tha grouped by category, and price column 



-- -------------
-- 8. Having 
-- Similar to Where
-- WHERE: results based on the values of the individaul rows
-- HAVING: results based on the values on aggregate property 
-- Comes after GROUP BY
-- But before ORDER BY and LIMIT
-- -------------
SELECT price, 
   ROUND(AVG(downloads)),
   COUNT(*)
FROM fake_apps
GROUP BY price
HAVING COUNT(*) > 10;
-- Condition has an aggregate function, so we have to use having 




-- -------------



-- -------------



-- -------------



-- -------------