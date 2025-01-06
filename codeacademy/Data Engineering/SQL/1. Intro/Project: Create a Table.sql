-- ------------
-- Project: Create a Table
-- Date: 2025.01.05
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------

-- ------------
-- 0. Drop table if exist
-- ------------
DROP TABLE IF EXISTS celebs; 


-- ------------
-- 1. Create Table 
-- ------------
CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE 
);


-- ------------
-- 2. Add information 
-- ------------
INSERT INTO friends (id, name, birthday)
VALUES (1, 'Ororo Munroe', '1940-05-30');

INSERT INTO friends (id, name, birthday)
VALUES (2, 'Jiyun Nam', '1999-02-16');

INSERT INTO friends (id, name, birthday)
VALUES (3, 'Yunha Nam', '2023-12-12');


-- ------------
-- 3. Update information 
-- ------------
UPDATE friends 
SET name = 'Storm'
WHERE id = 1; 
-- Ororo Munroe decided to change her name into "Storm"


-- ------------
-- 4. Add new column 
-- ------------
ALTER TABLE friends
ADD COLUMN email TEXT;


-- ------------
-- 5. Update information 
-- ------------
UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;


-- ------------
-- 6. Remove information 
-- ------------
DELETE FROM friends
WHERE id = 1;


-- ------------
-- Check Data
-- ------------
SELECT * FROM friends;
