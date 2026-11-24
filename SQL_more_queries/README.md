# SQL - More queries

MySQL users and privileges, column constraints (`NOT NULL`, `DEFAULT`,
`UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`, `AUTO_INCREMENT`), subqueries,
and combining tables with `JOIN` and `LEFT JOIN`.

Every script is run by piping it into the `mysql` client, for example:

```
cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
```

| File | Description |
| ---- | ----------- |
| `0-privileges.sql` | Lists the privileges of `user_0d_1` and `user_0d_2`. |
| `1-create_user.sql` | Creates `user_0d_1` with all privileges. |
| `2-create_read_user.sql` | Creates `hbtn_0d_2` and `user_0d_2` with only `SELECT` on it. |
| `3-force_name.sql` | Creates `force_name`, where `name` can't be null. |
| `4-never_empty.sql` | Creates `id_not_null`, where `id` defaults to 1. |
| `5-unique_id.sql` | Creates `unique_id`, where `id` defaults to 1 and is unique. |
| `6-states.sql` | Creates `hbtn_0d_usa` and its `states` table. |
| `7-cities.sql` | Creates the `cities` table, linked to `states` by a foreign key. |
| `8-cities_of_california_subquery.sql` | Lists the cities of California using a subquery (no `JOIN`). |
| `9-cities_by_state_join.sql` | Lists every city with its state name. |
| `10-genre_id_by_show.sql` | Lists the shows that have a genre, with the genre id. |
| `11-genre_id_all_shows.sql` | Lists every show with its genre ids, `NULL` if none. |
| `12-no_genre.sql` | Lists the shows that have no genre. |
| `13-count_shows_by_genre.sql` | Number of shows per genre, most common first. |
| `14-my_genres.sql` | Lists the genres of Dexter. |
| `15-comedy_only.sql` | Lists the Comedy shows. |
| `16-shows_by_genre.sql` | Lists every show with its genre names, `NULL` if none. |
