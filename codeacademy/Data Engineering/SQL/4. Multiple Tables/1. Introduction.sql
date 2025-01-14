-- ------------
-- Chapter 4: Multiple Tables
-- Date: 2025.01.05
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------

-- -------------
-- 0. Create Schema & Drop Tables
-- -------------
CREATE SCHEMA practice;
DROP TABLE IF EXISTS practice.orders;
DROP TABLE IF EXISTS practice.subscriptions;
DROP TABLE IF EXISTS practice.customers;



DROP TABLE IF EXISTS newspaper;
DROP TABLE IF EXISTS online;
DROP TABLE IF EXISTS months;


DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS students;
D
-- -------------
-- 1. Create Tables
-- -------------
CREATE TABLE IF NOT EXISTS practice.orders(
    order_id INT,
    customer_id INT,
    subscription_id INT,
    purchase_date DATE
);
CREATE TABLE IF NOT EXISTS practice.subscriptions(
    subscription_id INT,
    description TEXT,
    price_per_month INT,
    subscription_length TEXT
);
CREATE TABLE IF NOT EXISTS practice.customers(
    customer_id INT,
    customer_name TEXT,
    address TEXT
);



CREATE TABLE IF NOT EXISTS newspaper(
    id INT, 
    first_name TEXT, 
    last_name TEXT, 
    email TEXT, 
    start_month INT, 
    end_month INT
);
CREATE TABLE IF NOT EXISTS online(
    id INT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    start_month INT,
    end_month INT
);
CREATE TABLE IF NOT EXISTS month(
    month INT
);



CREATE TABLE IF NOT EXISTS classes(
    id INT,
    description TEXT,
    weeks INT,
    enrollment_cap INT
);

CREATE TABLE IF NOT EXISTS students(
    id INT,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    class_id INT
);

-- -------------
-- 2. Combining Tables with SQL
--
-- SELECT (columns that want to show)
-- FROM (table want to show)
-- JOIN (table that want to combine)
--  ON (table that wnat to combine.same column = table want to show.same colun)
-- -------------
-- 1. Join order table and subscriptions table and select all columns. Join the subscription_id
SELECT *
FROM practice.orders o
JOIN practice.subscriptions s
  ON s.subscription_id = o.subscription_id

-- 2. Add condition that select only rows meet description 'Fashion Magazine'
SELECT *
FROM practice.orders o
JOIN practice.subscriptions s
  ON s.subscription_id = o.subscription_id
WHERE s.description = 'Fashion Magazine'

select * from practice.orders limit 10;

-- -------------
-- 3. Inner Join
--
-- combining columns by duplicaiton
-- inner join of two tables on table1.c2 = table2.c2:
-- if the data of two table does not match, eliminate. 
-- just print out the data that duplicate
-- -------------
SELECT *
FROM newspaper n
JOIN online o
  ON n.id = o.id
ORDER BY n.id DESC; -- no null value



-- -------------
-- 4. Left Joins
-- 
-- Inner Joins: keep the rows that only duplicate with two tables columns 
-- Left Joins : keep all the rows even it does not duplicate. The first table of daata usually keep in here.
-- -------------
-- 1. left join of newspaper table and online table on their id coluns and selecting all columns 
SELECT * 
FROM newspaper n
LEFT JOIN online o
  ON n.id = o.id
WHERE o.id IS NULL; -- left join by newspaper_id. so there should be null for online_id

select * from newspaper



-- -------------
-- 5. Primarky Key VS Foreign Key
-- 
-- PK requirements:
-- None of the values can be NULL
-- Each value must be unique and only one PK per table

-- If PK appears in the different table, it is called as Foreign Key 
-- SELECT * 
-- FROM pk
-- JOIN fk
   -- ON pk.attributes = fk.attributes
-- -------------
-- 1. Identify PK, FK
SELECT * FROM students ;
-- id, first_name, last_name, email, class_id(foreign key)
SELECT * FROM classes;
-- id(priamry key), description, weeks, enrollment_cap 
SELECT *
FROM classes -- pk
JOIN students -- fk
  ON classes.id = students.class_id;



-- -------------
-- 6. Cross Join 

-- CROSS JOIN: when we ened to compare each row of a table to a list of values.  
-- -------------
-- 1. Count people who subscribed during march
SELECT count(*)
FROM newspaper
WHERE start_month <=3 AND end_month >=3;

-- 2. show all the people from newspaper and cros join with months
SELECT count(*)
FROM newspaper
CROSS JOIN months;

-- 3. show all the people from newspaper and cross join the months to show which months did they subscribe
SELECT count(*)
FROM newspaper
CROSS JOIN months
WHERE start_month <= month AND end_month >= month;

-- 4. show how many subscribers during each month.
SELECT month,count(*) AS 'subscribers'
FROM newspaper
CROSS JOIN months
WHERE start_month <= month AND end_month >= month
GROUP BY month



-- -------------
-- 7. Union
-- 
-- SELECT *
-- FROM table 1
-- UNION
-- SELECT *
-- FROM table 2;
--
-- combine the tables. 
-- tables must have the same number of column
-- column must have the same data types in the same order as the first table 
-- -------------
-- 1. newspaper, online
SELECT *
FROM newspaper
UNION
SELECT *
FROM online;



-- -------------
-- 8. With
--
-- 
/* WITH previous_results AS (
   SELECT ...
   ...
   ...
   ...
)
SELECT *
FROM previous_results
JOIN customers
  ON _____ = _____; */
--
-- With statement allow us perform a seperate query
-- and save that query inside of the WITH clause
-- -------------
-- 1. Combine preivous_query and customers, and print out the customer_namem and subscriptions
WITH previous_query AS(
SELECT customer_id,
  COUNT(subscription_id) AS 'subscriptions'
FROM orders
GROUP BY customer_id)
SELECT customers.customer_name, previous_query.subscriptions
FROM previous_query
JOIN customers ON customers.customer_id = previous_query.customer_id

  

-- -------------





-- -------------

-- -------------





-- -------------


-- -------------

