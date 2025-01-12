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