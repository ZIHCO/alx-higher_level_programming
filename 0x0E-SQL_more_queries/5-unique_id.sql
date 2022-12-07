-- create the table unique_id on server
-- id defaults to 1 and unique and name
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
