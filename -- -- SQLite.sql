-- -- SQLite
-- CREATE TABLE users (
--   id INTEGER NOT NULL PRIMARY KEY,
--   username TEXT NOT NULL,
--   hash TEXT NOT NULL,
--   cash NUMERIC NOT NULL DEFAULT 10000.00
-- );

-- SQLite

--  CREATE TABLE product (
-- 	pid INTEGER PRIMARY KEY NOT NULL,
-- 	name TEXT NOT NULL,
-- 	price REAL NOT NULL,
-- 	stock INTEGER NOT NULL,
--     vid INTEGER,
--     cid INTEGER
-- );

--  Multiple insert
-- SQLite
-- INSERT INTO
--     product(pid,name,price,stock,vid,cid)
-- VALUES
--     ('1',	'Shirt',	'10.0',	'48',	'NULL',	'1'),
-- ('2',	'pant',	'20.0'	,'75',	'NULL',	'1'),
-- ('3',	'Shoes',	'100.0',	'48',	'Hamza',	'Test'),
-- ('4',	'Kurta',	'20.0'	,'75',	'NULL',	'4'), 
-- ('6',	'Kameez',	'30.0'	,'35',	'NULL',	'4'),
-- ('7',	'Shalwar',	'10.0'	,'35',	'NULL',	'1'),
-- ('8',	'Sock',	'10.0'	,'30',	'NULL',	'7');


--  DROP TABLE product

-- SELECT * FROM product

-- CREATE TABLE cart(

--     cart_id INTEGER PRIMARY KEY NOT NULL,
--     quantity INTEGER NOT NULL,
--     pid INTEGER,
--     user_id INTEGER

-- );

-- CREATE TABLE invoice(
--     invoice_id INTEGER PRIMARY KEY,
--     inv_date DATETIME,
--     total real,
--     pid INTEGER,
--     user_id INTEGER

-- );

-- CREATE TABLE trancation(
      
--     pname TEXT NOT NULL,
--     total_BUY real,
--     total_price INTEGER,
--     total_cost INTEGER,
--     pid INTEGER,
--     user_id INTEGER,
--     time  TIMESTAMP DEFAULT CURRENT_TIMESTAMP

-- );
--  DROP TABLE trancation