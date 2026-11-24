-- Lists the number of records with the same score in the table second_table
-- One row per score with its count, most common score first
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
