-- Creates the database hbtn_0d_2 and the read-only user user_0d_2
-- Create hbtn_0d_2 only if missing
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user_0d_2 only if missing, with its password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Allow user_0d_2 to read (SELECT) every table of hbtn_0d_2, nothing else
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
