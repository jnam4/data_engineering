-- ------------
-- Project: Trends in Startups
-- Date: 2025.01.06
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------


-- ------------
-- 0. Drop table if exist
-- ------------
DROP TABLE IF EXISTS startups; 


-- ------------
-- 1. Create Table 
-- Int: 4bytes, bight: 8 bytes, numerical(decimal): infinite
-- ------------
CREATE TABLE startups(
    name TEXT,
    location TEXT,
    category TEXT,
    employees INT,
    raised NUMERIC,
    valuation NUMERIC,
    founded INT,
    stage TEXT,
    ceo TEXT,
    info TEXT
);

SELECT * FROM startups; 
-- 10 columns exists 



-- ------------
-- 2. Simple Aggregation
-- ------------
-- 1. Total number of companies in the table
SELECT COUNT(*)
FROM startups;

-- 2. Total value of all companies 
SELECT SUM(valuation) FROM startups;

-- 3. Highest amount raised by startup while Seed stage 
SELECT MAX(raised)
FROM startups
WHERE stage = 'Seed'

-- 4. Oldest comapny on the list
select name, min(founded)
from startups;



-- ------------
-- 3. Valaution Among Different Sectors 
-- ------------
-- 1. Average valuation 
select AVG(valuation)
FROM startups;

-- 2. Average valuation in each category 
SELECT category, AVG(valuation)
FROM startups
WHERE valuation IS NOT NULL AND category IS NOT NULL
GROUP BY category;

-- 3. average valuation in each category, rounded with two decimal places
SELECT category, ROUND(AVG(valuation),2) AS valuation
FROM startups 
WHERE valuation IS NOT NULL AND category IS NOT NULL
GROUP BY category

-- 4. average valuation in each category, rounded with two decimal places and order list from highest averages to lowests
SELECT category, ROUND(AVG(valuation),2) AS valuation
FROM startups 
WHERE valuation IS NOT NULL AND category IS NOT NULL
GROUP BY category 
ORDER BY valuation DESC 



-- ------------
-- 4. Competitive Markets
-- ------------
-- 1. Name of category and total number of companies 
SELECT category, COUNT(*)
FROM startups
GROUP BY category

-- 2. Name of category and total number of companies where more than 3 companies in them and order COUNT(*) by descending order  
SELECT category, COUNT(*)
FROM startups
GROUP BY category
HAVING COUNT(*) > 3
ORDER BY 2 DESC;
-- Three competitive market is Social, Mobile, and Education



-- ------------
-- 5. Different startup size among different locations 
-- ------------
-- 1. Average size of startup in each location
SELECT location, ROUND(AVG(employees),2) AS employees
FROM startups
GROUP BY location

-- 2. Average size of startup in each location that average size above 500 
SELECT location, ROUND(AVG(employees),2) AS employees
FROM startups
GROUP BY location
HAVING AVG(employees) > 500
-- In Silion Valley, Brooklyn, New York, and San Franisco startsup have averagily more than 500 employees in the startups 