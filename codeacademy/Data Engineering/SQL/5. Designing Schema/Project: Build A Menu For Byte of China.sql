-- ------------
-- Project: Build A Menu For Byte Of China
-- Date: 2025.01.11 
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------

/* Perform following tasks:
create tables
define relationships between tables
designate appropriate columns as keys
insert sample data and
make queries from the database */

-- ------------
-- 1. Create Tables and Primary Keys
-- ------------
CREATE TABLE IF NOT EXISTS restaurant(
  id INT PRIMARY KEY,
  name TEXT,
  explaination TEXT,
  ratings FLOAT,
  telephone TEXT,
  hours TEXT
);

CREATE TABLE IF NOT EXISTS address(
  id INT PRIMARY KEY,
  street_number INT,
  street_address TEXT,
  city TEXT,
  state TEXT,
  google_map TEXT,
  -- One to One Relationsihip with restaurant
  restaurant_id INT REFERENCES restaurant(id)
);

CREATE TABLE IF NOT EXISTS review(
  id INT PRIMARY KEY,
  rating FLOAT,
  description TEXT,
  date DATE,
  -- One to Many Relationship with restaurant
  restaurant_id INT REFERENCES restaurant(id)
);

CREATE TABLE IF NOT EXISTS category(
  id TEXT PRIMARY KEY,
  name TEXT,
  desciprion TEXT
);

CREATE TABLE IF NOT EXISTS dish(
  id INT PRIMARY KEY,
  name TEXT,
  description TEXT,
  spicy BOOLEAN
);

 -- Many to Many Relationship with category and dish -- create cross-reference table 
CREATE TABLE IF NOT EXISTS categories_dishes(
  category_id TEXT REFERENCES category(id),
  dish_id INT REFERENCES dish(id),
  price MONEY,
  PRIMARY KEY (category_id, dish_id)
);
  

-- ------------
-- 2. Define Relationships and Foreign Keys
-- ------------
-- One to One Relationship : Restaurant - Address
-- One to Many Relationship : Restaurant - Reviews
-- Many to Many Relationship : category - dish


-- ------------
-- 3. Insert Sample Data
-- ------------
/* 
 *--------------------------------------------
 Insert values for restaurant
 *--------------------------------------------
 */
INSERT INTO restaurant VALUES (
  1,
  'Bytes of China',
  'Delectable Chinese Cuisine',
  3.9,
  '6175551212',
  'Mon - Fri 9:00 am to 9:00 pm, Weekends 10:00 am to 11:00 pm'
);

/* 
 *--------------------------------------------
 Insert values for address
 *--------------------------------------------
 */
INSERT INTO address VALUES (
  1,
  '2020',
  'Busy Street',
  'Chinatown',
  'MA',
  'http://bit.ly/BytesOfChina',
  1
);

/* 
 *--------------------------------------------
 Insert values for review
 *--------------------------------------------
 */
INSERT INTO review VALUES (
  1,
  5.0,
  'Would love to host another birthday party at Bytes of China!',
  '05-22-2020',
  1
);

INSERT INTO review VALUES (
  2,
  4.5,
  'Other than a small mix-up, I would give it a 5.0!',
  '04-01-2020',
  1
);

INSERT INTO review VALUES (
  3,
  3.9,
  'A reasonable place to eat for lunch, if you are in a rush!',
  '03-15-2020',
  1
);

/* 
 *--------------------------------------------
 Insert values for category
 *--------------------------------------------
 */
INSERT INTO category VALUES (
  'C',
  'Chicken',
  null
);

INSERT INTO category VALUES (
  'LS',
  'Luncheon Specials',
  'Served with Hot and Sour Soup or Egg Drop Soup and Fried or Steamed Rice  between 11:00 am and 3:00 pm from Monday to Friday.'
);

INSERT INTO category VALUES (
  'HS',
  'House Specials',
  null
);

/* 
 *--------------------------------------------
 Insert values for dish
 *--------------------------------------------
 */
INSERT INTO dish VALUES (
  1,
  'Chicken with Broccoli',
  'Diced chicken stir-fried with succulent broccoli florets',
  false
);

INSERT INTO dish VALUES (
  2,
  'Sweet and Sour Chicken',
  'Marinated chicken with tangy sweet and sour sauce together with pineapples and green peppers',
  false
);

INSERT INTO dish VALUES (
  3,
  'Chicken Wings',
  'Finger-licking mouth-watering entree to spice up any lunch or dinner',
  true
);

INSERT INTO dish VALUES (
  4,
  'Beef with Garlic Sauce',
  'Sliced beef steak marinated in garlic sauce for that tangy flavor',
  true
);

INSERT INTO dish VALUES (
  5,
  'Fresh Mushroom with Snow Peapods and Baby Corns',
  'Colorful entree perfect for vegetarians and mushroom lovers',
  false
);

INSERT INTO dish VALUES (
  6,
  'Sesame Chicken',
  'Crispy chunks of chicken flavored with savory sesame sauce',
  false
);

INSERT INTO dish VALUES (
  7,
  'Special Minced Chicken',
  'Marinated chicken breast sauteed with colorful vegetables topped with pine nuts and shredded lettuce.',
  false
);

INSERT INTO dish VALUES (
  8,
  'Hunan Special Half & Half',
  'Shredded beef in Peking sauce and shredded chicken in garlic sauce',
  true
);

/*
 *--------------------------------------------
 Insert valus for cross-reference table, categories_dishes
 *--------------------------------------------
 */
INSERT INTO categories_dishes VALUES (
  'C',
  1,
  6.95
);

INSERT INTO categories_dishes VALUES (
  'C',
  3,
  6.95
);

INSERT INTO categories_dishes VALUES (
  'LS',
  1,
  8.95
);

INSERT INTO categories_dishes VALUES (
  'LS',
  4,
  8.95
);

INSERT INTO categories_dishes VALUES (
  'LS',
  5,
  8.95
);

INSERT INTO categories_dishes VALUES (
  'HS',
  6,
  15.95
);

INSERT INTO categories_dishes VALUES (
  'HS',
  7,
  16.95
);

INSERT INTO categories_dishes VALUES (
  'HS',
  8,
  17.95
);

SELECT * FROM restaurant;
SELECT * FROM address;
SELECT * FROM review;
SELECT * FROM dish;
SELECT * FROM category;
SELECT * FROM categories_dishes;


-- ------------
-- 4. Make Sample Questions
-- ------------
-- restaurant name, address(street number and name), telephone, best_rating 
SELECT restaurant.name AS restaurant_name, 
address.street_number AS street_number,
address.street_address AS street_address,
restaurant.telephone AS telephone,
review.rating AS best_rating
FROM restaurant, address, review
WHERE restaurant.id = address.restaurant_id
AND restaurant.id = review.restaurant_id
ORDER BY best_rating DESC
LIMIT 1;

-- dish_name, price, category
SELECT 
dish.name AS dish_name, categories_dishes.price AS price, category.name AS category
FROM categories_dishes, dish, category
WHERE categories_dishes.dish_id = dish.id
AND categories_dishes.category_id = category.id;

-- category, dish_name, price
SELECT category.name AS category,
dish.name AS dish_name, categories_dishes.price AS price
FROM categories_dishes, dish, category
WHERE categories_dishes.dish_id = dish.id
AND categories_dishes.category_id = category.id;

-- spicy_dish_name, category, price
SELECT dish.name AS spicy_dish_name, category.name AS category, categories_dishes.price AS price
FROM categories_dishes, dish, category
WHERE categories_dishes.dish_id = dish.id
AND categories_dishes.category_id = category.id
AND dish.spicy = 't';

-- dish_id, count(dish_id) as dish_count from categories_dish table -- use AS 
WITH ca_di AS
(SELECT 
    category.id AS category_id, dish.id AS dish_id, category.name AS category,
    dish.name AS dish_name, categories_dishes.price AS price
FROM 
    categories_dishes
JOIN dish
    ON categories_dishes.dish_id = dish.id
JOIN category
    ON categories_dishes.category_id = category.id
)
SELECT 
    ca_di.dish_id AS dish_id, 
    ca_di.dish_name AS dish_name,
count(ca_di.dish_id) AS dish_count
FROM ca_di
GROUP BY ca_di.dish_name, ca_di.dish_id
ORDER BY ca_di.dish_id ASC
LIMIT 5;


-- best_rating and description
SELECT restaurant.id, review.rating AS best_rating, review.description
from review, restaurant
where review.restaurant_id = restaurant.id
and review.rating = (select max(review.rating) from review)
