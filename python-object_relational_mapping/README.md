# Python - Object-relational mapping

Connecting Python scripts to a MySQL database, first with raw SQL through
`MySQLdb`, then through the SQLAlchemy ORM.

Every script takes `<mysql user> <mysql password> <database>` (plus a state
name for some) and connects to `localhost:3306`.

## MySQLdb (raw SQL)

| File | Description |
| --- | --- |
| `0-select_states.py` | Lists all states |
| `1-filter_states.py` | Lists states whose name starts with `N` |
| `2-my_filter_states.py` | Lists states matching an argument (built with `format`, injectable) |
| `3-my_safe_filter_states.py` | Same as 2, but safe from SQL injection |
| `4-cities_by_state.py` | Lists all cities with their state name |
| `5-filter_cities.py` | Lists the cities of a given state |

## SQLAlchemy (ORM)

| File | Description |
| --- | --- |
| `model_state.py` | `Base` and the `State` class mapped to `states` |
| `model_city.py` | `City` class mapped to `cities` |
| `7-model_state_fetch_all.py` | Lists all `State` objects |
| `8-model_state_fetch_first.py` | Prints the first `State` |
| `9-model_state_filter_a.py` | Lists states containing the letter `a` |
| `10-model_state_my_get.py` | Prints the id of the state with a given name |
| `11-model_state_insert.py` | Adds the state `Louisiana` |
| `12-model_state_update_id_2.py` | Renames the state with id 2 to `New Mexico` |
| `13-model_state_delete_a.py` | Deletes states containing the letter `a` |
| `14-model_city_fetch_by_state.py` | Lists all cities with their state |
