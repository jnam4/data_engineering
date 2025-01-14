-- ------------
-- Chapter 6: 1.Constraints
-- Date: 2025.01.12
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------

-- ------------
-- 0. Introduction
-- ------------
-- Databaase(DB) schema store information for a conference
-- constraints method
-- rules defined as part of the data model to control what values are allowed in specific columns and tables.
-- reject inserts or updates containing values that shouldn't be inserted. 
-- raise an error when violated, which can help with debugging application that write to DB 

-- Data types 
-- NOT NULL
-- UNIQUE
-- PRIMARY KEY
-- CHECK
-- FOREIGN KEY



-- ------------
-- 1. Data types
-- ------------
/*
Name            Description
boolean         true/false
varchar(n)      text with variable length
                up to n charcters
date            calendar date
integer         whole number between 
                4 Bytes
bigint          8 Bytes
numeric(a,b)   decimal with total digits(a) 
                and digits after the decimal point(b)
time            time of the day (no time zone) */
-- ------------
CREATE TABLE attendees (
  id INTEGER,
  name VARCHAR,
  total_tickets_reserved INTEGER,
  standard_tickets_reserved INTEGER,
  vip_tickets_reserved INTEGER
);

INSERT INTO attendees VALUES (1, 'John Smith', 2, 1, 1);


-- ------------
-- 2. Nullability Constraints 
-- ------------

CREATE TABLE speakers (
  id INT NOT NULL,
  email VARCHAR NOT NULL,
  name VARCHAR NOT NULL,
  organization VARCHAR,
  title VARCHAR,
  years_in_role INT
);

INSERT INTO speakers (id, email, name, organization, title, years_in_role)
VALUES (1, 'awilson@ABCcorp.com', 'A. Wilson', 'ABC Corp.', 'CTO', 6);

-- ------------
-- 3. Improving Tables with Constraints -- UPDATE NOT NULL, NULL
-- ------------
/* Update no longer any nulls in title 
ALTER TABLE talks
ALTER COLUMN title SET NOT NULL;

UPDATE talks
SET title = 'TBD'
WHERE title IS NULL;

*/
-- Set Table Column is Not Null
ALTER TABLE speakers
ALTER COLUMN name SET NOT NULL;

-- Update statement that fills the null values in organization with a placeholder value
UPDATE speakers
SET organization = 'Unaffiliated'
WHERE organization IS NULL;

-- Write Alter table stateent adds a not null constraint
ALTER TABLE speakers
ALTER COLUMN organization SET NOT NULL;




-- ------------
-- 4. Check Constrains
-- Check whether statement is either T/F
-- estimated_length -> an integer, not null, positive
-- ------------
ALTER TABLE speakers
ADD check (years_in_role < 100)



-- ------------
-- 5. Check Constraints 
-- make comparision between columns within the table 
-- logical operations-AND, OR
-- ------------
ALTER TABLE speakers
ADD CHECK (years_in_role < 100 AND years_in_role > 0);

ALTER TABLE attendees 
ADD CHECK (standard_tickets_reserved + vip_tickets_reserved = total_tickets_reserved)



-- ------------
-- 6. Using Unique Constraints
--
-- uniquely identify rows of the table
-- ------------
/* 
ALTER TABLE attendees 
ADD UNIQUE (email);

*/

ALTER TABLE speakers
ADD UNIQUE (email);

CREATE TABLE registrations (
    id integer NOT NULL,
    attendee_id integer NOT NULL,
    session_timeslot timestamp NOT NULL,
    talk_id integer NOT NULL,
    UNIQUE (attendee_id, session_timeslot)
);

-- ------------
-- 7. Primary Keys
--
-- Essentia to defining relationship
-- Uniquely identifies a row within a database table & No null values
-- ------------
/*
ALTER TABLE attendees
ADD PRIMARY KEY (id); 
*/

ALTER TABLE speakers
ADD PRIMARY KEY (id);

-- INSERT INTO speakers VALUES (
--   1, 'J.Saunders@ABCTech.com', 'Joan Saunders', 'ABC Tech', 'Sr. Data Scientist', 6
-- );
-- ERROR:  duplicate key value violates unique constraint “speakers_pkey”
-- DETAIL:  Key (id)=(1) already exists



-- ------------

-- ------------
