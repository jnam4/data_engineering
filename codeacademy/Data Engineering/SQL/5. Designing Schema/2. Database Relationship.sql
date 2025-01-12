-- ------------
-- Chapter 5: 2. Database Relationship
-- Date: 2025.01.11
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------
-- Relationship
-- one to one 
-- one to many
-- many to many

-- ------------
-- 0. Drop Table
-- ------------
DROP TABLE IF EXISTS book_details;

-- ------------
-- 1. One-to-One Relationship
-- UNIQUE 
--
-- column1 type REFERENCES table2(column) UNIQUE
-- ------------
CREATE TABLE book_details (
  id integer PRIMARY KEY,
  book_isbn varchar(50) REFERENCES book(isbn) UNIQUE,
  rating decimal,
  language varchar(10),
  keywords text[],
  date_published date
);

SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'book_details'
-- why foreign key listed twice? 
-- has two constraints, foreign key, and unique

INSERT INTO book VALUES (
  'Learn PostgreSQL',
  '123457890',
  100,
  2.99,
  'Great course',
  'Codecademy'
);

INSERT INTO book_details VALUES (
  1,
  '123457890',
  3.95,
  'English',
  '{sql, postgresql, database}',
  '2020-05-20'
);

--  displays common data available in both book and book_details based on their shared identifier, book.isbn and book_details.book_isbn.
select book.title, book.price, book_details.language, book_details.rating
from book, book_details
where book.isbn = book_details.book_isbn
-- instead of WHERE, you can use
-- FROM table1
-- JOIN table2
-- ON table1.primary_key = talbe2.foreign_key



-- ------------
-- 2. One to Many Relationship
-- ------------
-- Create page table take id as primary key 
-- and chapter id as foreign key
CREATE TABLE IF NOT EXISTS page(
  id INT PRIMARY KEY,
  chapter_id INT REFERENCES chapter(id),
  content TEXT,
  header VARCHAR(20),
  footer VARCHAR(20)
);

-- Column drop off
-- ALTER TABLE table_name DROP COLUMN column_name;
ALTER TABLE chapter DROP COLUMN content;

-- validate existence of key
SELECT constraint_name, table_name, column_name
FROM information_schema.key_column_usage
WHERE table_name = 'page';

-- Insert Data
INSERT INTO book VALUES (
  'Learn PostgreSQL',
  '0-9673-4537-5',
  100,
  2.99,
  'Dive into Postgres for Beginners',
  'Codecademy Publishing'
);

INSERT INTO book VALUES (
  'Postgres Made Easy',
  '0-3414-4116-3',
  255,
  5.99,
  'Learn Postgres the Easy Way',
  'Codecademy Press'
);

INSERT INTO chapter VALUES (
  1,
  '0-9673-4537-5',
  1,
  'Chapter 1'
);

INSERT INTO chapter VALUES (
  2,
  '0-3414-4116-3',
  1,
  'Chapter 1'
);

INSERT INTO page VALUES (
  1,
  1,
  'Chapter 1 Page 1',
  'Page 1 Header',
  'Page 1 Footer'
);

INSERT INTO page VALUES (
  2,
  1,
  'Chapter 1 Page 2',
  'Page 2 Header',
  'Page 2 Footer'
);

INSERT INTO page VALUES (
  3,
  2,
  'Chapter 1 Page 1',
  'Page 1 Header',
  'Page 1 Footer'
);

INSERT INTO page VALUES (
  4,
  2,
  'Chapter 1 Page 2',
  'Page 2 Header',
  'Page 2 Footer'
);


-- Inner join book, chapter, page 
select book.title as book_title,
 chapter.title as chapter_title, 
 page.content as page_content
from book
inner join chapter
on book.isbn = chapter.book_isbn
inner join page
on chapter.id = page.chapter_id;


-- ------------
-- 3. Many to Many Relationship #1
-- 
-- create third cross reference table, call it as joint table 
-- foreign key referencing primary key as well 
-- a composite primary key made up of the two foreign keys
-- ------------
-- Create a cross-reference table
drop table if EXISTS books_authors;
CREATE TABLE books_authors(
  book_isbn varchar(50) REFERENCES book(isbn),
  author_email varchar(20) REFERENCES author(email),
  PRIMARY KEY(book_isbn, author_email)
);

-- Validate existence 
select constraint_name, table_name, column_name
from information_schema.key_column_usage
where table_name = 'books_authors'

-- ------------
-- 4. Many to Many Relationship #2
-- ------------
SELECT * FROM book;
SELECT * FROM author; 

INSERT INTO author VALUES (
'James Key', 'Guru in database management with PostgreSQL', 'jkey@db.com'),
('Clara Index',	'Guru in database management with PostgreSQL', 'cindex@db.com');

INSERT INTO book values('Learn PostgreSQL Volume 2', '987654321', 200, 3.99, 'Manage database part two	Codecademy');
INSERT INTO books_authors VALUES ('123457890', 'jkey@db.com'); 
INSERT INTO books_authors VALUES ('123457890', 'cindex@db.com');
INSERT INTO books_authors VALUES ('987654321', 'cindex@db.com');

select * from books_authors;


-- Write a query to show one to many relationship between book and author
select book.title as book_title, author.name as author_name, book.description as book_description
from book, author, books_authors
where book.isbn = books_authors.book_isbn
and author.email = books_authors.author_email;

select author.name as author_name, author.email as author_email, book.title as book_title
from book, author, books_authors
where book.isbn = books_authors.book_isbn
and author.email = books_authors.author_email;
