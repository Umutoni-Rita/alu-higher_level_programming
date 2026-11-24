-- Lists all records with a score >= 10 in the table second_table
-- Score and name of records scoring at least 10, highest score first
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
