-- Creates the database hbtn_0d_usa and the table states in it
-- Create hbtn_0d_usa only if missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- states: auto-numbered primary key id and a required name
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY, name VARCHAR(256) NOT NULL);
