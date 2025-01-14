-- ------------
-- Project: Lyft Trip Data
-- Date: 2025.01.11 
-- Author: Jiyun Nam
-- Credit: codecademy
-- ------------

-- ------------
-- Data Info
-- trips: trips information
-- riders: user data
-- cars; autonomous cars
-- ------------

-- ------------
-- 0. Drop table if exist
-- ------------
DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS riders;
DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS riders2;


-- ------------
-- 1. Create Table 
-- Int: 4bytes, bight: 8 bytes, numerical(decimal): infinite
-- ------------
CREATE TABLE IF NOT EXISTS trips(
    id INT,
    date DATE,
    pickup TEXT,
    dropoff TEXT,
    rider_id INT,
    car_id INT,
    type TEXT,
    cost FLOAT)

CREATE TABLE IF NOT EXISTS riders(
    id INT,
    first TEXT,
    last TEXT,
    username TEXT,
    rating FLOAT,
    total_trips INT,
    referred INT
)

CREATE TABLE IF NOT EXISTS riders2(
    id INT,
    first TEXT,
    last TEXT,
    username TEXT,
    rating FLOAT,
    total_trips INT,
    referred INT)

CREATE TABLE IF NOT EXISTS cars(
    id INT,
    model TEXT,
    OS TEXT,
    status TEXT,
    trips_completed INT
)

-- ------------
-- 2. Select Data and combine tables by disntinguishing PK, FK
-- ------------
SELECT *
FROM trips
LEFT JOIN riders
    ON trips.rider_id = riders.id
JOIN cars
    ON trips.car_id = cars.id;
-- trips: id-PK, rider_id-FK, car_id-FK
-- rider: id-PK
-- cars: id-PK


-- ------------
-- 3. Combine tables 
-- ------------
SELECT * from riders;
SELECT * FROM riders2;

SELECT *
FROM riders
UNION
SELECT *
FROM riders2;



-- ------------
-- 4. 2+3 combined all the tables 
-- ------------
With combined_tables AS(
    SELECT *
    FROM riders
    UNION
    SELECT *
    FROM riders2
)
SELECT *
FROM trips
LEFT JOIN riders
    ON trips.rider_id = riders.id
JOIN cars
    ON trips.car_id = cars.id
ORDER BY trips.id ASC;


-- ------------
-- 5. Avg costs
-- ------------
With combined_tables AS(
    SELECT *
    FROM riders
    UNION
    SELECT *
    FROM riders2
)
SELECT avg(cost)
FROM trips
LEFT JOIN riders
    ON trips.rider_id = riders.id
JOIN cars
    ON trips.car_id = cars.id



-- ------------
-- 6. Find all the riders who have used lyft less than 500 times
-- ------------
With combined_tables AS(
    SELECT *
    FROM riders
    UNION
    SELECT *
    FROM riders2
)
SELECT trips.rider_id, total_trips
FROM trips
LEFT JOIN riders
    ON trips.rider_id = riders.id
JOIN cars
    ON trips.car_id = cars.id
WHERE total_trips < 500;



-- ------------
-- 7. Calculte the number of cars that active
-- ------------
With combined_tables AS(
    SELECT *
    FROM riders
    UNION
    SELECT *
    FROM riders2
)
SELECT count(status)
FROM trips
LEFT JOIN riders
    ON trips.rider_id = riders.id
JOIN cars
    ON trips.car_id = cars.id
WHERE status = 'active'


-- ------------
-- 7. Find two cars that have the highest trips_completed
-- ------------
With combined_tables AS(
    SELECT *
    FROM riders
    UNION
    SELECT *
    FROM riders2
)
SELECT cars.model, cars.id, cars.trips_completed
FROM trips
LEFT JOIN riders
    ON trips.rider_id = riders.id
JOIN cars
    ON trips.car_id = cars.id
GROUP BY cars.id, cars.model, cars.trips_completed
-- WE did not use aggregate function in the select, so we have to list all
ORDER BY trips_completed DESC
limit 2;


