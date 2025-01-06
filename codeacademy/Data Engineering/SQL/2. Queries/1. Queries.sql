-- ------------
-- Chapter 2: Queries
-- Date: 2025.01.05
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------

-- ------------
-- 0. Drop table if exist
-- ------------
DROP TABLE IF EXISTS movies; 

-- ------------
-- 1. Create table
-- ------------
CREATE TABLE movies(
    id INTEGER,
    name TEXT,
    genre TEXT,
    year INTEGER,
    imdb_rating FLOAT
);



-- ------------
-- 2. SELECT 
-- * : all 
-- able to select as many columns you want 
-- ------------
SELECT name, genre 
FROM movies;

SELECT name, genre, year
FROM movies;



-- ------------
-- 3. As
-- renaming the columnb or table using an alias
-- not renaming table, but appear in results 
-- ------------
SELECT imdb_rating AS "imdb"
FROM movies;



-- ------------
-- 4. Distinct 
-- Filters out all duplicate values in the specified column and return unique values in the output. 
-- jiyun, jiyun, yunha, yunha -> jiyun, yunha
-- ------------
SELECT DISTINCT year
FROM movies; 



-- ------------
-- 5. Where 
-- conditional that meet the information that we want 
-- = Equal to 
-- != not equal to 
-- > greater than, < less than, 
-- >= greater than equal to, <= less than equal
-- ------------
SELECT * 
FROM movies
WHERE year > 2014;
-- Select everything from movies where year is greater than 2014



-- ------------
-- 6. Like 1
-- want to compare similar values. 
-- _ means can substitue any individual character. 
-- ex) Where name Like 'Se_en'
--     - will give Se7en, Seven similar values
-- ------------
SELECT * 
FROM movies 
WHERE name LIKE 'Se_en';



-- ------------
-- 7. Like 2
-- Like is not case sensitive
-- % : can be used with LIKE
--     matches zero or more missing characters in pattern. 
-- ex) A%: name begins with A
--     %a: name ends with a 
-- ------------
SELECT * 
FROM movies 
WHERE name LIKE '%man%';
-- SELECT everything FROM movies WHERE name contains "man" (not case senstivie)

SELECT * 
FROM movies 
WHERE name LIKE 'The %';
-- SEELCT everything FROm movies WHERE name contains "The "



-- ------------
-- 8. Is Null
-- Unknown values 
-- Not able to test with = or !=
-- Always with IS NULL or IS NOT NULL
-- ------------
SELECT name
FROM MOVIES
WHERE imdb_rating IS NULL
-- SELECT name FROM movies WHERE imdb_rating is NULL



-- ------------
-- 9. Between _ AND 
-- filter the results set within a certain range
-- accepts either numbers, text, or dates 
-- numbers, year: including both values 
-- text: does not include second value. 
--      If it is "G", have to type "H" for second value. 
-- ------------

SELECT *
FROM movies
WHERE name BETWEEN 'D' AND 'G';
-- SELECT all information FROM movies WHERE name is between 'D' and 'F'

SELECT * 
FROM movies 
WHERE year BETWEEN 1970 AND 1979;
-- SELECT all information FROM movies WHERE movies released in 1970's



-- ------------
-- 10. AND
-- want to combine multiple conditions 
-- ------------
SELECT *
FROM movies
WHERE year BETWEEN 1970 and 1979
  AND imdb_rating > 8;
-- SELECT all information FROM movies Where movie released in 1970s and imdb_rating is greater than 8

SELECT * 
FROM movies
WHERE year < 1985 
  AND genre = "horror"
-- SELECT all information FROM movies WHERE movie released before 1985 and genre is horror



-- ------------
-- 11. Or
-- AND : display a row if all the conditons are true 
-- OR : display a row if any of the conditions is true 
-- ------------
SELECT *
FROM movies
WHERE genre = "romance"
  OR genre = "comedy"
-- SELECT all information FROM movies WHERE genre is either romance or comedy



-- ------------
-- 12. ORDER BY (columns)
-- sort the result either alphabetically or numerically 
-- DESC: descending order
-- ASC: ascending order 
-- ------------
SELECT name, year, imdb_rating
FROM movies 
WHERE imdb_rating IS NOT NULL
ORDER BY imdb_rating DESC
-- return name, year, and imdb_rating columns of all the movies,
-- ordered highest to lowest by their rating, wheere imdb_rating is not null



-- ------------
-- 13. LIMIT
-- specify the maximum number of the rows of results set will have. 
-- ------------
SELECT * 
FROM movies 
ORDER BY imdb_rating DESC 
LIMIT 3
-- returns top 3 highest rated movies



-- ------------
-- 14. Case
-- if-then logic 
-- When: test conditions 
-- Then: if condition is ture, gives the string
-- Must end with END 
-- Rename it by AS, should not use ''
-- ------------
SELECT name,
CASE 
    WHEN imdb_rating > 8 THEN 'Fantastic'
    WHEN imdb_rating > 6 THEN 'Poorly Received'
    ELSE  'Avoid at All Costs'
END AS Reviews
FROM movies;

SELECT name, 
 CASE 
  WHEN genre = 'romance' THEN 'Chill'
  WHEN genre = 'comedy' THEN 'Chill'
  ELSE 'Intense'
 END AS Mood
 -- End case and rename it as Mood
FROM movies;


