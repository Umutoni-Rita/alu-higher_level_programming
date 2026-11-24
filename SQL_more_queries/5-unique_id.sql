-- Creates the table unique_id where id defaults to 1 and must be unique
-- UNIQUE rejects any second row with the same id
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
