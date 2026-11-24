-- Lists all the cities of California without using JOIN
-- The subquery finds the id of California, the outer query uses it to filter cities
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
