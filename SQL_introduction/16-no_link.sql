-- Lists all records of second_table that have a name, by descending score
-- Skip rows whose name is NULL or empty
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
