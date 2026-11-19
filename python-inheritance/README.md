# Python - Inheritance

Introduction to inheritance in Python: subclasses, `super()`, method
overriding, `isinstance` / `issubclass` / `type`, and doctest-based tests.

| File | Description |
| ---- | ----------- |
| `0-lookup.py` | `lookup(obj)` returns the list of attributes and methods of an object. |
| `1-my_list.py` | `MyList`, a subclass of `list` with `print_sorted()`. |
| `2-is_same_class.py` | True if an object is exactly an instance of a class. |
| `3-is_kind_of_class.py` | True if an object is an instance of a class or one of its subclasses. |
| `4-inherits_from.py` | True only if the object's class is a strict subclass of the given class. |
| `5-base_geometry.py` | Empty class `BaseGeometry`. |
| `6-base_geometry.py` | `BaseGeometry` with `area()` that raises an Exception. |
| `7-base_geometry.py` | `BaseGeometry` with `integer_validator(name, value)`. |
| `8-rectangle.py` | `Rectangle(BaseGeometry)` with private, validated width and height. |
| `9-rectangle.py` | `Rectangle` with `area()` and `__str__`. |
| `10-square.py` | `Square(Rectangle)` with a validated size. |
| `11-square.py` | `Square` with its own `__str__`. |
| `tests/1-my_list.txt` | Doctests for `MyList`. |
| `tests/7-base_geometry.txt` | Doctests for `BaseGeometry`. |

Run the tests with:

```bash
python3 -m doctest ./tests/*
```
