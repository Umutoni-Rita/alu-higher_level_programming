-- Creates the database hbtn_0d_usa and the table cities in it
-- Create hbtn_0d_usa only if missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- cities: auto-numbered primary key id, state_id linked to states.id, required name
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, state_id INT NOT NULL, name VARCHAR(256) NOT NULL, FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));
