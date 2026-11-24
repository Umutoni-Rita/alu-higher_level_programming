# SQL - Introduction

First steps with MySQL 8.0: creating and dropping databases and tables,
inserting, reading, updating and deleting rows, and simple aggregates
(`COUNT`, `AVG`, `GROUP BY`).

Every script is run by piping it into the `mysql` client, for example:

```
cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

| File | Description |
| ---- | ----------- |
| `0-list_databases.sql` | Lists all databases of the server. |
| `1-create_database_if_missing.sql` | Creates `hbtn_0c_0` if it does not exist. |
| `2-remove_database.sql` | Deletes `hbtn_0c_0` if it exists. |
| `3-list_tables.sql` | Lists all tables of the given database. |
| `4-first_table.sql` | Creates `first_table` (`id INT`, `name VARCHAR(256)`). |
| `5-full_table.sql` | Prints the full description of `first_table` without `DESCRIBE`. |
| `6-list_values.sql` | Lists all rows of `first_table`. |
| `7-insert_value.sql` | Inserts the row `89, Best School` into `first_table`. |
| `8-count_89.sql` | Counts the records with `id = 89` in `first_table`. |
| `9-full_creation.sql` | Creates `second_table` and fills it with four records. |
| `10-top_score.sql` | Lists `score, name` of `second_table`, best score first. |
| `11-best_score.sql` | Same as 10, only records with `score >= 10`. |
| `12-no_cheating.sql` | Sets Bob's score to 10, matching on his name. |
| `13-change_class.sql` | Deletes records with `score <= 5`. |
| `14-average.sql` | Average score, in a column named `average`. |
| `15-groups.sql` | Number of records per score, most common first. |
| `16-no_link.sql` | Lists `score, name` of records that have a name, best score first. |
