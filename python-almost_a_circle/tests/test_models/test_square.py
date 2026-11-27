#!/usr/bin/python3
"""Unittests for the Square class defined in models/square.py."""
import io
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


if __name__ == "__main__":
    unittest.main()
