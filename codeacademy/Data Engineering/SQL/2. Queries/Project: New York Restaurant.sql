-- ------------
-- Project: New York Restaurant 
-- Date: 2025.01.06
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------


-- ------------
-- 0. Drop table if exist
-- ------------
DROP TABLE IF EXISTS nomnom; 


-- ------------
-- 1. Create Table 
-- ------------
CREATE TABLE nomnom(
    name TEXT, 
    neighborhood TEXT,
    cuisine TEXT,
    review float,
    price TEXT,
    health Text
);

-- After this, import csv file from pgAdmin into the table 


-- ------------
-- 2. Select Information
-- ------------
-- 1. Select all information
SELECT * FROM nomnom;

-- 2. Select distint neighborhood
SELECT DISTINCT neighborhood 
FROM nomnom;

-- 3. Select distinct cuisine
SELECT DISTINCT cuisine
FROM nomnom;

-- 4. Show option where Chinese takeout 
SELECT *
FROM nomnom
WHERE cuisine = 'Chinese';

-- 5. Show options where review is 4 and above.
SELECT *
FROM nomnom
WHERE review >= 4;

-- 6. Show options where Italian and $$$ 
SELECT *
FROM nomnom
WHERE cuisine = 'Italian' and Price = '$$$'

-- 7. Find restaurant that contains the word 'meatball' 
SELECT * 
FROM nomnom
WHERE name LIKE '% Meatball %' -- need to contain space

-- 8. Find restaurant near by Midtown, Downtown or Chinatown
SELECT * 
FROM nomnom
WHERE neighborhood = 'Midtown'
  OR neighborhood = 'Downtown'
  OR neighborhood = 'Chinatown';

-- 9. Find restuarant that health grade is pending 
SELECT *
FROM nomnom
WHERE health IS NULL;

-- 10. Top 10 Restaurnat based on reviews
SELECT * 
FROM nomnom
ORDER BY review DESC
LIMIT 10

-- 11. Case statement rating system to 
SELECT *, 
 CASE 
  WHEN review > 4.5 THEN 'Extraordinary'
  WHEN review > 4 THEN 'Excellent'
  WHEN review > 3 THEN 'Good'
  WHEN review > 2 THEN 'Fair'
  ELSE 'Poor'
  END AS Rating
FROM nomnom






