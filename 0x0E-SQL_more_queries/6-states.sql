-- script creates the database hbtn_0d_usa and table states on hbtn_0d_usa
-- id unique, auto generated can't be null and pk, name not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
	name VARCHAR(256) NOT NULL);
