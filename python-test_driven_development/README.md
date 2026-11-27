# Python - Test-driven development

Writing functions together with their tests: interactive tests with
`doctest` (`tests/*.txt`) and unit tests with `unittest` (`tests/*.py`).

| File | Description |
| --- | --- |
| `0-add_integer.py` | Adds 2 integers (floats are cast to int) |
| `2-matrix_divided.py` | Divides all elements of a matrix by a number |
| `3-say_my_name.py` | Prints `My name is <first name> <last name>` |
| `4-print_square.py` | Prints a square with the character `#` |
| `5-text_indentation.py` | Prints a text with 2 new lines after `.`, `?` and `:` |
| `6-max_integer.py` | Returns the max integer in a list (given) |
| `tests/6-max_integer_test.py` | Unittests for `max_integer` |

Run the tests:

```
python3 -m doctest ./tests/*.txt
python3 -m unittest tests.6-max_integer_test
```
