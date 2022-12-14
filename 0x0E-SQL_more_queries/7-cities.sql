-- script creates the database hbtn_0d_usa and table cities on hbtn_0d_usa
-- id unique, auto generated can't be null and pk, name not null
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
	state_id INT, FOREIGN KEY(state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL);
