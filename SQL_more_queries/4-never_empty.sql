-- Creates the table id_not_null where id defaults to 1
-- id takes the value 1 when an INSERT leaves it out
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
