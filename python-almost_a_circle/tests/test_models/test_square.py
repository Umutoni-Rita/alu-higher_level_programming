#!/usr/bin/python3
"""Unittests for the Square class defined in models/square.py."""
import io
import json
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


def capture(func, *args):
    """Call func with args and return everything it printed to stdout."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        func(*args)
    return buf.getvalue()


class TestSquareInstantiation(unittest.TestCase):
    """Tests for the Square constructor."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_rectangle(self):
        """Square is a subclass of Rectangle and Base."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_auto_ids(self):
        """Ids are assigned automatically."""
        self.assertEqual((Square(1).id, Square(2).id), (1, 2))

    def test_attributes(self):
        """size sets both width and height."""
        s = Square(5, 1, 2, 9)
        self.assertEqual((s.width, s.height, s.size, s.x, s.y, s.id),
                         (5, 5, 5, 1, 2, 9))

    def test_default_x_y(self):
        """x and y default to 0."""
        s = Square(3)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_no_new_attributes(self):
        """Square does not create a private __size attribute."""
        s = Square(3)
        self.assertFalse(hasattr(s, "_Square__size"))

    def test_no_args(self):
        """size is required."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        """More than 4 arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)


class TestSquareValidation(unittest.TestCase):
    """Tests for the validation inherited from Rectangle."""

    def check(self, error, message, *args):
        """Assert that Square(*args) raises error with message."""
        with self.assertRaises(error) as ctx:
            Square(*args)
        self.assertEqual(str(ctx.exception), message)

    def test_size_types(self):
        """A non-integer size raises the width TypeError."""
        for bad in ("1", 1.5, None, [1], {}, True):
            self.check(TypeError, "width must be an integer", bad)

    def test_size_zero_or_negative(self):
        """A size <= 0 raises the width ValueError."""
        self.check(ValueError, "width must be > 0", 0)
        self.check(ValueError, "width must be > 0", -3)

    def test_x(self):
        """x must be an integer >= 0."""
        self.check(TypeError, "x must be an integer", 1, "2")
        self.check(ValueError, "x must be >= 0", 1, -2)

    def test_y(self):
        """y must be an integer >= 0."""
        self.check(TypeError, "y must be an integer", 1, 2, "3")
        self.check(ValueError, "y must be >= 0", 1, 2, -3)

    def test_order(self):
        """size is validated before x, and x before y."""
        self.check(TypeError, "width must be an integer", "1", "2")
        self.check(ValueError, "x must be >= 0", 1, -2, "y")


class TestSquareSize(unittest.TestCase):
    """Tests for the size getter and setter."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_getter(self):
        """size returns the width."""
        self.assertEqual(Square(5).size, 5)

    def test_setter(self):
        """Setting size changes width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_setter_type(self):
        """A non-integer size gives the width error message."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_setter_value(self):
        """A size <= 0 gives the width error message."""
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = 0


class TestSquareAreaDisplay(unittest.TestCase):
    """Tests for area and display inherited from Rectangle."""

    def test_area(self):
        """Area is size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_display_no_offset(self):
        """Display a square without offset."""
        self.assertEqual(capture(Square(2).display), "##\n##\n")

    def test_display_x(self):
        """Display a square with an x offset."""
        self.assertEqual(capture(Square(2, 2).display), "  ##\n  ##\n")

    def test_display_x_y(self):
        """Display a square with x and y offsets."""
        self.assertEqual(capture(Square(3, 1, 3).display),
                         "\n\n\n ###\n ###\n ###\n")


class TestSquareStr(unittest.TestCase):
    """Tests for Square.__str__."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_defaults(self):
        """String with automatic id and default offsets."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")

    def test_all_values(self):
        """String with every value given."""
        self.assertEqual(str(Square(3, 1, 3, 12)), "[Square] (12) 1/3 - 3")

    def test_print(self):
        """print uses __str__."""
        self.assertEqual(capture(print, Square(2, 2, 0, 4)),
                         "[Square] (4) 2/0 - 2\n")


class TestSquareUpdate(unittest.TestCase):
    """Tests for Square.update with *args and **kwargs."""

    def setUp(self):
        """Create a fresh square with id 1 for each test."""
        Base._Base__nb_objects = 0
        self.s = Square(5)

    def test_no_args(self):
        """update() without arguments changes nothing."""
        self.s.update()
        self.assertEqual(str(self.s), "[Square] (1) 0/0 - 5")

    def test_args(self):
        """Positional arguments are id, size, x, y."""
        expected = [
            ((10,), "[Square] (10) 0/0 - 5"),
            ((1, 2), "[Square] (1) 0/0 - 2"),
            ((1, 2, 3), "[Square] (1) 3/0 - 2"),
            ((1, 2, 3, 4), "[Square] (1) 3/4 - 2"),
        ]
        for args, result in expected:
            self.s.update(*args)
            self.assertEqual(str(self.s), result)

    def test_kwargs(self):
        """Keyword arguments set the named attributes."""
        self.s.update(1, 2, 3, 4)
        self.s.update(x=12)
        self.assertEqual(str(self.s), "[Square] (1) 12/4 - 2")
        self.s.update(size=7, y=1)
        self.assertEqual(str(self.s), "[Square] (1) 12/1 - 7")
        self.s.update(size=7, id=89, y=1)
        self.assertEqual(str(self.s), "[Square] (89) 12/1 - 7")

    def test_size_sets_width_and_height(self):
        """Updating size keeps width and height equal."""
        self.s.update(1, 8)
        self.assertEqual((self.s.width, self.s.height), (8, 8))

    def test_args_skip_kwargs(self):
        """kwargs are ignored when args are given."""
        self.s.update(3, size=9)
        self.assertEqual(str(self.s), "[Square] (3) 0/0 - 5")

    def test_validated(self):
        """Values from update are validated."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.s.update(1, "2")
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.s.update(y=-1)

    def test_unknown_kwarg_ignored(self):
        """Unknown keys do not create new attributes."""
        self.s.update(color="red")
        self.assertFalse(hasattr(self.s, "color"))


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_content(self):
        """The dictionary holds id, size, x and y only."""
        self.assertEqual(Square(10, 2, 1).to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_type(self):
        """The result is a dict."""
        self.assertIsInstance(Square(1).to_dictionary(), dict)

    def test_update_from_dictionary(self):
        """update(**to_dictionary()) copies another square."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s2), "[Square] (1) 2/1 - 10")
        self.assertFalse(s1 == s2)


class TestSquareJson(unittest.TestCase):
    """Tests for to_json_string and from_json_string called on Square."""

    def test_to_json_string(self):
        """Square.to_json_string converts Square dictionaries."""
        d = Square(10, 2, 1, 1).to_dictionary()
        self.assertEqual(json.loads(Square.to_json_string([d])), [d])

    def test_to_json_string_none_and_empty(self):
        """Square.to_json_string returns '[]' for None and []."""
        self.assertEqual(Square.to_json_string(None), "[]")
        self.assertEqual(Square.to_json_string([]), "[]")

    def test_from_json_string(self):
        """Square.from_json_string reverses to_json_string."""
        data = [{"id": 89, "size": 10, "x": 1, "y": 2}]
        self.assertEqual(
            Square.from_json_string(Square.to_json_string(data)), data)

    def test_from_json_string_none_and_empty(self):
        """Square.from_json_string returns [] for None and ''."""
        self.assertEqual(Square.from_json_string(None), [])
        self.assertEqual(Square.from_json_string(""), [])


class TestSquareSaveToFile(unittest.TestCase):
    """Tests for Square.save_to_file."""

    def setUp(self):
        """Reset the counter and remove Square.json before each test."""
        Base._Base__nb_objects = 0
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        """Remove Square.json after each test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def read(self):
        """Return the raw text of Square.json."""
        with open("Square.json", "r", encoding="utf-8") as f:
            return f.read()

    def test_none(self):
        """Square.save_to_file(None) writes an empty list."""
        Square.save_to_file(None)
        self.assertEqual(self.read(), "[]")

    def test_empty_list(self):
        """Square.save_to_file([]) writes an empty list."""
        Square.save_to_file([])
        self.assertEqual(self.read(), "[]")

    def test_one_square(self):
        """Square.save_to_file([Square(1)]) writes that square."""
        Square.save_to_file([Square(1)])
        self.assertEqual(json.loads(self.read()),
                         [{"id": 1, "size": 1, "x": 0, "y": 0}])

    def test_two_squares(self):
        """Square.save_to_file writes every square in the list."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        self.assertEqual(json.loads(self.read()),
                         [s1.to_dictionary(), s2.to_dictionary()])

    def test_overwrite(self):
        """Saving again replaces the old content of Square.json."""
        Square.save_to_file([Square(1), Square(2)])
        Square.save_to_file(None)
        self.assertEqual(self.read(), "[]")

    def test_file_name(self):
        """Square.save_to_file writes to Square.json, not Rectangle.json."""
        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.exists("Square.json"))


class TestSquareCreate(unittest.TestCase):
    """Tests for Square.create."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_only(self):
        """Square.create(**{'id': 89}) sets only the id."""
        s = Square.create(**{"id": 89})
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")

    def test_id_size(self):
        """Square.create(**{'id': 89, 'size': 1})."""
        s = Square.create(**{"id": 89, "size": 1})
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")

    def test_id_size_x(self):
        """Square.create(**{'id': 89, 'size': 1, 'x': 2})."""
        s = Square.create(**{"id": 89, "size": 1, "x": 2})
        self.assertEqual(str(s), "[Square] (89) 2/0 - 1")

    def test_all(self):
        """Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})."""
        s = Square.create(**{"id": 89, "size": 1, "x": 2, "y": 3})
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")
        self.assertIsInstance(s, Square)

    def test_new_object(self):
        """create returns a different object with the same values."""
        s1 = Square(3, 1, 2)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


class TestSquareLoadFromFile(unittest.TestCase):
    """Tests for Square.load_from_file."""

    def setUp(self):
        """Reset the counter and remove Square.json before each test."""
        Base._Base__nb_objects = 0
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def tearDown(self):
        """Remove Square.json after each test."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_no_file(self):
        """Square.load_from_file() returns [] when the file is missing."""
        self.assertEqual(Square.load_from_file(), [])

    def test_file_exists(self):
        """Square.load_from_file() rebuilds the saved squares."""
        inputs = [Square(5), Square(7, 9, 1)]
        Square.save_to_file(inputs)
        outputs = Square.load_from_file()
        self.assertEqual(len(outputs), 2)
        for before, after in zip(inputs, outputs):
            self.assertIsInstance(after, Square)
            self.assertIsNot(before, after)
            self.assertEqual(str(before), str(after))

    def test_saved_none(self):
        """Loading after Square.save_to_file(None) returns []."""
        Square.save_to_file(None)
        self.assertEqual(Square.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
