-- Creates the MySQL server user user_0d_1 with all privileges
-- Create user_0d_1 only if missing, with its password
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Give user_0d_1 every privilege on every database and table
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
