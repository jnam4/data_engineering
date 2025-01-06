-- ------------
-- Chapter 1: Intro
-- Date: 2025.01.05
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------



-- ----------------
-- 1. CREATE 
-- Allow us to create new table in the database
-- CREATE TABLE name (column_name datatype, ...);
-- ----------------
SELECT * FROM celebs; 
-- show everything from the table 
-- create table after know that database is empty

CREATE TABLE celebs (
  id INTEGER,
  name TEXT,
  age INTEGER
);
-- create table with data type



-- ----------------
-- 2. INSERT
-- add new records
-- ----------------
INSERT INTO celebs (id, name, age)
VALUES (1, 'Justin Bieber', 29);
-- Total records : 1

INSERT INTO celebs (id, name, age) 
VALUES (2, 'Beyonce Knowles', 42); 

INSERT INTO celebs (id, name, age) 
VALUES (3, 'Jeremy Lin', 35); 

INSERT INTO celebs (id, name, age) 
VALUES (4, 'Taylor Swift', 33); 
-- Total records : 4



-- ----------------
-- 3. SELECT 
-- fetch data from a database 
-- SELECT name of column FROM table.
-- ----------------
SELECT * FROM celebs; 



-- ----------------
-- 4. Alter
-- add new column to the table 
-- ----------------
ALTER TABLE celebs
ADD COLUMN twitter_handle TEXT;
-- add twitter_handle column that has text data type on the celebs table 

SELECT * FROM celebs; 
-- we did not add data here, so show up as null



-- ----------------
-- 5. Update
-- use it when you want to change existing records
-- ----------------
UPDATE celebs
SET twitter_handle = '@taylorswift13'
WHERE id = 4;
-- update in celebs table 
-- change the value for the id = 4
-- change twitter_handle column record as '@talyorswift13'

SELECT * FROM celebs;



-- ----------------
-- 6. DELETE
-- deletes one or more rows from table 
-- ----------------
DELETE FROM celebs
WHERE twitter_handle IS NULL;
-- deletes allo records in the celebs table with no value on twitter_handle column 

SELECT * FROM celebs
-- only one record left



-- ----------------
-- 7. Constraints 
-- add information about how a column can be used are invoked after specifying the data type for a column 
-- PK, FK, UNIQUE, NOT NULL, DEFAULT
-- DEFAULT : columns take an additional argument that will be the assumed value for an inserted row if the new row does not specify value. 
-- ----------------
CREATE TABLE awards (
   id INTEGER PRIMARY KEY,
   recipient TEXT NOT NULL,
   award_name TEXT DEFAULT 'Grammy'
);

SELECT * FROM awards

