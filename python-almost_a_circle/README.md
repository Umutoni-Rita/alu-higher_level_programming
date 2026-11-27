# Python - Almost a circle

A small project that ties together classes, inheritance, properties,
`*args`/`**kwargs`, JSON serialization, file I/O and unit testing.

## Structure

```
models/
    __init__.py
    base.py        # Base: id management + JSON / file helpers
    rectangle.py   # Rectangle(Base): width, height, x, y
    square.py      # Square(Rectangle): size, x, y
tests/
    test_models/
        test_base.py
        test_rectangle.py
        test_square.py
```

## Classes

- **Base**: assigns ids (given or automatic), `to_json_string`,
  `from_json_string`, `save_to_file`, `create`, `load_from_file`.
- **Rectangle**: validated `width`, `height`, `x`, `y`; `area`, `display`,
  `__str__`, `update`, `to_dictionary`.
- **Square**: a Rectangle with equal sides; adds the `size` property and
  its own `__str__`, `update` and `to_dictionary`.

## Tests

```
python3 -m unittest discover tests
python3 -m unittest tests/test_models/test_base.py
```
