-- Creates the table force_name where name can not be null
-- name is NOT NULL, so every row must have one
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
