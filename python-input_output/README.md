# Python - Input/Output

Reading and writing files with the `with` statement, JSON serialization
and deserialization, command-line arguments, and turning class instances
into dictionaries (and back).

| File | Description |
| ---- | ----------- |
| `0-read_file.py` | `read_file(filename)` prints a UTF-8 text file to stdout. |
| `1-write_file.py` | `write_file(filename, text)` overwrites a file and returns the number of characters written. |
| `2-append_write.py` | `append_write(filename, text)` appends to a file and returns the number of characters added. |
| `3-to_json_string.py` | `to_json_string(my_obj)` returns the JSON string of an object. |
| `4-from_json_string.py` | `from_json_string(my_str)` returns the object a JSON string represents. |
| `5-save_to_json_file.py` | `save_to_json_file(my_obj, filename)` writes an object to a file as JSON. |
| `6-load_from_json_file.py` | `load_from_json_file(filename)` creates an object out of a JSON file. |
| `7-add_item.py` | Script that adds its arguments to a list stored in `add_item.json`. |
| `8-class_to_json.py` | `class_to_json(obj)` returns the dictionary description of an instance. |
| `9-student.py` | `Student` class with `to_json()`. |
| `10-student.py` | `Student` with `to_json(attrs=None)` that can filter attributes. |
| `11-student.py` | `Student` with `reload_from_json(json)` to restore attributes. |
| `12-pascal_triangle.py` | `pascal_triangle(n)` returns Pascal's triangle of `n` rows. |
