-- ------------
-- Chapter 5: 1. Database Schema
-- Date: 2025.01.11
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------
DROP TABLE IF EXISTS profile;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS chapter;
DROP TABLE IF EXISTS author; 
DROP TABLE IF EXISTS popular_books;
-- ------------
-- 0. Data figuration
-- ------------
SELECT * FROM profile;
-- columns are name, age, home_address, phone, home_email
-- work_address, work_position, work_phone, work_id, 
-- school_id, school_email, school_address
-- Therefore this data can be seperate into profile, work, school


-- ------------
-- 1. Creating table practice
-- ------------
CREATE TABLE IF NOT EXISTS book (
  title VARCHAR(100),
  isbn VARCHAR(50),
  pages INT,
  price money,
  description VARCHAR(256),
  publisher VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS chapter(
  id INT,
  number INT,
  title VARCHAR(50),
  content VARCHAR(1024)
);
CREATE TABLE IF NOT EXISTS author(
  name VARCHAR(50),
  bio VARCHAR(100),
  email VARCHAR(20)
);
CREATE TABLE IF NOT EXISTS profile(
    name TEXT,
    age	INT,
    home_address TEXT,
    phone TEXT, 
    home_email TEXT,
    work_address TEXT,
    work_position	TEXT,
    work_phone	TEXT,
    work_id	TEXT,
    school_id	INT,
    school_email TEXT,
    school_address TEXT
)


-- ------------
-- 2. Insert Data
--
-- INSERT INTO table_name VALUES (....)
-- ------------
-- INSERT INTO table_name VALUES (....)
INSERT INTO book VALUES(
  'Postgres for Beginners',
  '0-5980-6249-1',
  25,
  4.99,
  'Learn Postgres the Easy Way',
  'Codecademy Publishing'
  );

SELECT * FROM book
WHERE title = 'Postgres for Beginners';
SELECT * FROM book
WHERE isbn = '0-5980-6249-1'
-- multiple rows cme out: ensure isbn contain only uique values. 



-- ------------
-- 3. PRIMARY KEY
--
/* CREATE TABLE recipe (
  id integer PRIMARY KEY,
  name varchar(20),
  ...
);*/    
-- ------------
-- Setting up primary key in book, chapter, author table 
CREATE TABLE book (
  title varchar(100),
  isbn varchar(50) PRIMARY KEY,
  pages integer,
  price money,
  description varchar(256),
  publisher varchar(100)
);

CREATE TABLE chapter (
  id integer PRIMARY KEY,
  number integer,
  title varchar(50),
  content varchar(1024)
);

CREATE TABLE author (
  name varchar(50),
  bio varchar(100),
  email varchar(20) PRIMARY KEY
);

-- ------------
-- 4. KEY VALIDATION
--
-- key_column_usage
/* 
SELECT
  constraint_name, table_name, column_name
FROM
  information_schema.key_column_usage
WHERE
  table_name = 'recipe';

 constraint_name | table_name | column_name 
-----------------+------------+-------------
 recipe_pkey     | recipe     | id
(1 row)
*/
-- ------------
--  check in book table for key_column_usage
SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'book';

SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'chapter';

SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'author';



-- ------------
-- 5. COMPOSITE PRIMARY KEY
-- 
-- To design multiple columns as composite primary key,
-- PRIMARY KEY (column_one, column_two)
-- ------------
CREATE TABLE popular_books (
  book_title VARCHAR(100),
  author_name VARCHAR(50),
  number_sold INTEGER,
  number_previewed INTEGER,
  PRIMARY KEY (book_title, author_name)
);

SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'popular_books';
-- ------------
-- 6-1. Foreing Key #1
--
-- key that references a column in another table. 
-- use column_name type REFERENES table(column)
-- Make book related to its chapters
-- ------------
CREATE TABLE book (
  title varchar(100),
  isbn varchar(50) PRIMARY KEY,
  pages integer,
  price money,
  description varchar(256),
  publisher varchar(100)
);

CREATE TABLE chapter (
  id integer PRIMARY KEY,
  book_isbn varchar(50) REFERENCES book(isbn),
  number integer,
  title varchar(50),
  content varchar(1024)
);

SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'chapter'

-- ------------
-- 6-2. Foreign Key Part #2
-- 
-- use this after connecting foriegn key
-- this is for differentiating names
-- ------------
select * from book;
select * from chapter;
select book.title as book, chapter.title as chapters
from book, chapter
where book.isbn = chapter.book_isbn;