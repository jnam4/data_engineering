-- ------------
-- Project: Analyze Hacker News Trends
-- Date: 2025.01.06
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------

-- ------------
-- Brainstorming
-- ------------
/* 
title: the title of the story
user: the user who submitted the story
score: the score of the story
timestamp: the time of the story
url: the link of the story
*/

-- ------------
-- 0. Drop table if exist
-- ------------
DROP TABLE IF EXISTS hacker_news; 


-- ------------
-- 1. Create Table 
-- Int: 4bytes, bight: 8 bytes, numerical(decimal): infinite
-- ------------
CREATE TABLE hacker_news(
    title TEXT,
    "user" TEXT,
    score INT,
    timestamp TIMESTAMP,
    url TEXT
);

select * from hacker_news



-- ------------
-- 2. Understanding the dataset
-- ------------
-- 1. Top five stories with the highest scores
SELECT title, score, url
FROM hacker_news
WHERE score IS NOT NULL
ORDER BY score DESC
LIMIT 5;

/* Insights:
Penny Arcade – Surface Pro 3 update
Hacking The Status Game
Postgres CLI with autocompletion and syntax highlighting
Stephen Fry hits out at ‘infantile’ culture of trigger words and safe spaces
Reversal: Australian Govt picks ODF doc standard over Microsoft

are the top 5 stories with the highest score in the hacker_news
*/



-- ------------
-- 3. Hacker News Moderating 
-- ------------
-- 1. Find the total score of all the stories 
SELECT sum(score) -- 6366
FROM hacker_news;

-- 2-1. Find individual users who have gotten combined scores of more than 200
SELECT "user", score -- 304, 309, 517, 282
FROM hacker_news
WHERE score IS NOT NULL and score > 200;

-- 2.2 Combined their scores
SELECT user, sum(score) -- 1412
FROM hacker_news
WHERE score IS NOT NULL and score > 200
GROUP BY 1;

-- 2.3 Divide by the total get the percentage
SELECT 1412 / 6366.0;  -- 22%

-- 3. How many user post this URL?
SELECT DISTINCT "user", count(*)
from hacker_news
where url LIKE 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
Group by 1

/* Insights:
dmmalam, amirkhella, vxNsr, metafunctor are top user that produces meaningful articles as their total score is over 200. 
They are in charge of 22% of entire hacker_news. 

There are 2 users that write the article about https://www.youtube.com/watch?v=dQw4w9WgXcQ'.

-- ------------
-- 4. Which sites feed Hacker News?
-- ------------
-- 1. categorize each story baesd on the source
-- GitHub, Medium, New York Times
SELECT CASE 
    WHEN url LIKE '%github.com%' THEN 'Github'
    WHEN url LIKE '%medium.com%' THEN 'Medium'
    WHEN url LIKE '%nytimes.com%' THEN 'New York Times' 
    ELSE 'Other'
    END AS Source,
    COUNT(*)
FROM hacker_news
GROUP BY 1
ORDER BY 1 ASC;

/* Insights:
Somewhat other source feed Hacker News at the most as the count of 3952
*/



-- ------------
-- 5. Best time to post a story
-- ------------
-- 1. select all the timestamp  
SELECT timestamp
FROM hacker_news
LIMIT 10;
-- 2014-01-27T17:31:13Z
-- YYYY-MM-DD HH:MM:SS

-- 2. timestamp format 
-- SQRlite 
-- strftime(__, timestamp)
   -- %Y : year (YYYY)
   -- %m : month 
   -- %d : day 
   -- %H : 24 hour clock
   -- %M : minute
   -- %S : second
/* SELECT timestamp,
   strftime('%H', timestamp)
FROM hacker_news
GROUP BY 1
LIMIT 20; */

-- 3. extract hour from timestamp
SELECT timestamp,
        EXTRACT(HOUR FROM timestamp) AS hour
FROM hacker_news
GROUP BY timestamp
LIMIT 20;

-- 4. Hours from timestamp, average score, count of stories 
SELECT EXTRACT(HOUR FROM timestamp) AS hour, 
        ROUND(AVG(score),2),
        count(*)
FROM hacker_news
WHERE timestamp IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;

/* Insights: 
The best time to post based on average score is 18 PM.
The most common posting hours are:
15 PM (highest count: 268 articles).
18 PM (next highest count: 266 articles). 
*/