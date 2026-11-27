#!/usr/bin/python3
"""Unittests for the Rectangle class defined in models/rectangle.py."""
import io
import json
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


def capture(func, *args):
    """Call func with args and return everything it printed to stdout."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        func(*args)
    return buf.getvalue()


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for the Rectangle constructor."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_is_base(self):
        """Rectangle is a subclass of Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_auto_ids(self):
        """Ids come from Base and increase automatically."""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual((r1.id, r2.id), (1, 2))

    def test_given_id(self):
        """A given id is used."""
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """All arguments are stored in the right attribute."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_default_x_y(self):
        """x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_private_attributes(self):
        """The private attributes cannot be accessed directly."""
        r = Rectangle(1, 2)
        for name in ("__width", "__height", "__x", "__y"):
            with self.assertRaises(AttributeError):
                getattr(r, name)

    def test_setters(self):
        """Setters change the values."""
        r = Rectangle(1, 2)
        r.width = 10
        r.height = 20
        r.x = 3
        r.y = 4
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 20, 3, 4))

    def test_no_args(self):
        """width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        """height is required."""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        """More than 5 arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)


class TestRectangleValidation(unittest.TestCase):
    """Tests for the validation of width, height, x and y."""

    def check(self, error, message, *args):
        """Assert that Rectangle(*args) raises error with message."""
        with self.assertRaises(error) as ctx:
            Rectangle(*args)
        self.assertEqual(str(ctx.exception), message)

    def test_width_types(self):
        """A non-integer width raises TypeError."""
        for bad in ("1", 1.5, None, [1], {}, (1,), True, float("nan")):
            self.check(TypeError, "width must be an integer", bad, 1)

    def test_height_types(self):
        """A non-integer height raises TypeError."""
        for bad in ("2", 2.5, None, [2], {}, (2,), False):
            self.check(TypeError, "height must be an integer", 1, bad)

    def test_x_types(self):
        """A non-integer x raises TypeError."""
        for bad in ("3", 3.5, None, [3], {}):
            self.check(TypeError, "x must be an integer", 1, 1, bad)

    def test_y_types(self):
        """A non-integer y raises TypeError."""
        for bad in ("4", 4.5, None, [4], {}):
            self.check(TypeError, "y must be an integer", 1, 1, 0, bad)

    def test_width_zero_or_negative(self):
        """A width <= 0 raises ValueError."""
        self.check(ValueError, "width must be > 0", 0, 1)
        self.check(ValueError, "width must be > 0", -1, 1)

    def test_height_zero_or_negative(self):
        """A height <= 0 raises ValueError."""
        self.check(ValueError, "height must be > 0", 1, 0)
        self.check(ValueError, "height must be > 0", 1, -1)

    def test_x_negative(self):
        """A negative x raises ValueError."""
        self.check(ValueError, "x must be >= 0", 1, 1, -1)

    def test_y_negative(self):
        """A negative y raises ValueError."""
        self.check(ValueError, "y must be >= 0", 1, 1, 3, -1)

    def test_x_y_zero_allowed(self):
        """x and y can be 0."""
        r = Rectangle(1, 1, 0, 0)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_order_width_first(self):
        """width is validated before height."""
        self.check(TypeError, "width must be an integer", "a", "b")

    def test_order_height_before_x(self):
        """height is validated before x."""
        self.check(ValueError, "height must be > 0", 1, -1, "x")

    def test_order_x_before_y(self):
        """x is validated before y."""
        self.check(TypeError, "x must be an integer", 1, 2, "x", -1)

    def test_type_before_value(self):
        """The type error is raised before any value error."""
        self.check(TypeError, "y must be an integer", 1, 1, 0, "-1")

    def test_setter_validation(self):
        """Setters validate the same way as the constructor."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "3"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -1

    def test_failed_setter_keeps_value(self):
        """A rejected value does not change the attribute."""
        r = Rectangle(10, 2)
        with self.assertRaises(ValueError):
            r.width = 0
        self.assertEqual(r.width, 10)


class TestRectangleArea(unittest.TestCase):
    """Tests for Rectangle.area."""

    def test_small(self):
        """Area of small rectangles."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_with_offset_and_id(self):
        """x, y and id do not affect the area."""
        self.assertEqual(Rectangle(8, 7, 3, 4, 12).area(), 56)

    def test_large(self):
        """Area of a large rectangle."""
        self.assertEqual(Rectangle(10 ** 6, 10 ** 6).area(), 10 ** 12)

    def test_after_change(self):
        """Area follows changes to width and height."""
        r = Rectangle(2, 2)
        r.width = 5
        r.height = 3
        self.assertEqual(r.area(), 15)

    def test_with_arg(self):
        """area takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for Rectangle.display."""

    def test_no_offset(self):
        """A 4x6 rectangle without offset."""
        r = Rectangle(4, 6)
        self.assertEqual(capture(r.display), "####\n" * 6)

    def test_small(self):
        """A 2x2 rectangle."""
        self.assertEqual(capture(Rectangle(2, 2).display), "##\n##\n")

    def test_one(self):
        """A 1x1 rectangle."""
        self.assertEqual(capture(Rectangle(1, 1).display), "#\n")

    def test_x_y(self):
        """Offsets with both x and y."""
        r = Rectangle(2, 3, 2, 2)
        self.assertEqual(capture(r.display), "\n\n  ##\n  ##\n  ##\n")

    def test_x_only(self):
        """Offset with x only."""
        r = Rectangle(3, 2, 1, 0)
        self.assertEqual(capture(r.display), " ###\n ###\n")

    def test_y_only(self):
        """Offset with y only."""
        r = Rectangle(1, 1, 0, 3)
        self.assertEqual(capture(r.display), "\n\n\n#\n")

    def test_with_arg(self):
        """display takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(1)


class TestRectangleStr(unittest.TestCase):
    """Tests for Rectangle.__str__."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_all_values(self):
        """String with every value given."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")

    def test_defaults(self):
        """String with default y and automatic id."""
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_print(self):
        """print uses __str__."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(capture(print, r), "[Rectangle] (5) 3/4 - 1/2\n")

    def test_after_change(self):
        """The string follows attribute changes."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.width = 7
        r.id = 3
        self.assertEqual(str(r), "[Rectangle] (3) 0/0 - 7/1")


class TestRectangleUpdate(unittest.TestCase):
    """Tests for Rectangle.update with *args and **kwargs."""

    def setUp(self):
        """Create a fresh rectangle with id 1 for each test."""
        Base._Base__nb_objects = 0
        self.r = Rectangle(10, 10, 10, 10)

    def test_no_args(self):
        """update() without arguments changes nothing."""
        self.r.update()
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 10/10")

    def test_args_one_by_one(self):
        """Each positional argument sets the next attribute."""
        expected = [
            ((89,), "[Rectangle] (89) 10/10 - 10/10"),
            ((89, 2), "[Rectangle] (89) 10/10 - 2/10"),
            ((89, 2, 3), "[Rectangle] (89) 10/10 - 2/3"),
            ((89, 2, 3, 4), "[Rectangle] (89) 4/10 - 2/3"),
            ((89, 2, 3, 4, 5), "[Rectangle] (89) 4/5 - 2/3"),
        ]
        for args, result in expected:
            self.r.update(*args)
            self.assertEqual(str(self.r), result)

    def test_extra_args_ignored(self):
        """Positional arguments after the 5th are ignored."""
        self.r.update(89, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/5 - 2/3")

    def test_args_validated(self):
        """Values from update are validated by the setters."""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.update(89, "2")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.update(89, 2, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r.update(89, 2, 3, -4)

    def test_kwargs(self):
        """Keyword arguments set the named attributes."""
        self.r.update(height=1)
        self.assertEqual(str(self.r), "[Rectangle] (1) 10/10 - 10/1")
        self.r.update(width=1, x=2)
        self.assertEqual(str(self.r), "[Rectangle] (1) 2/10 - 1/1")
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 3/1 - 2/1")
        self.r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(self.r), "[Rectangle] (89) 1/3 - 4/2")

    def test_kwargs_validated(self):
        """Keyword values are validated by the setters."""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.update(y="1")

    def test_args_skip_kwargs(self):
        """kwargs are ignored when args are given."""
        self.r.update(89, 2, width=50, id=7)
        self.assertEqual(str(self.r), "[Rectangle] (89) 10/10 - 2/10")

    def test_unknown_kwarg_ignored(self):
        """Unknown keys do not create new attributes."""
        self.r.update(color="red")
        self.assertFalse(hasattr(self.r, "color"))

    def test_update_from_dictionary(self):
        """update(**to_dictionary()) copies another rectangle."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 == r2)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary."""

    def test_content(self):
        """The dictionary holds id, width, height, x and y."""
        r = Rectangle(10, 2, 1, 9, 5)
        self.assertEqual(r.to_dictionary(),
                         {"id": 5, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_type(self):
        """The result is a dict."""
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)

    def test_new_dict_each_call(self):
        """Changing the returned dict does not change the rectangle."""
        r = Rectangle(1, 1, 0, 0, 1)
        d = r.to_dictionary()
        d["width"] = 100
        self.assertEqual(r.width, 1)

    def test_with_arg(self):
        """to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).to_dictionary(1)


class TestRectangleJson(unittest.TestCase):
    """Tests for to_json_string and from_json_string called on Rectangle."""

    def test_to_json_string(self):
        """Rectangle.to_json_string converts Rectangle dictionaries."""
        d = Rectangle(10, 7, 2, 8, 1).to_dictionary()
        self.assertEqual(json.loads(Rectangle.to_json_string([d])), [d])

    def test_to_json_string_none_and_empty(self):
        """Rectangle.to_json_string returns '[]' for None and []."""
        self.assertEqual(Rectangle.to_json_string(None), "[]")
        self.assertEqual(Rectangle.to_json_string([]), "[]")

    def test_from_json_string(self):
        """Rectangle.from_json_string reverses to_json_string."""
        data = [{"id": 89, "width": 10, "height": 4}]
        self.assertEqual(
            Rectangle.from_json_string(Rectangle.to_json_string(data)), data)

    def test_from_json_string_none_and_empty(self):
        """Rectangle.from_json_string returns [] for None and ''."""
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string(""), [])


class TestRectangleSaveToFile(unittest.TestCase):
    """Tests for Rectangle.save_to_file."""

    def setUp(self):
        """Reset the counter and remove Rectangle.json before each test."""
        Base._Base__nb_objects = 0
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def tearDown(self):
        """Remove Rectangle.json after each test."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def read(self):
        """Return the raw text of Rectangle.json."""
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            return f.read()

    def test_none(self):
        """Rectangle.save_to_file(None) writes an empty list."""
        Rectangle.save_to_file(None)
        self.assertEqual(self.read(), "[]")

    def test_empty_list(self):
        """Rectangle.save_to_file([]) writes an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(self.read(), "[]")

    def test_one_rectangle(self):
        """Rectangle.save_to_file([Rectangle(1, 2)]) writes it."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertEqual(json.loads(self.read()),
                         [{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}])

    def test_two_rectangles(self):
        """Rectangle.save_to_file writes every rectangle in the list."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertEqual(json.loads(self.read()),
                         [r1.to_dictionary(), r2.to_dictionary()])

    def test_overwrite(self):
        """Saving again replaces the old content of Rectangle.json."""
        Rectangle.save_to_file([Rectangle(1, 1), Rectangle(2, 2)])
        Rectangle.save_to_file(None)
        self.assertEqual(self.read(), "[]")


class TestRectangleCreate(unittest.TestCase):
    """Tests for Rectangle.create."""

    def setUp(self):
        """Reset the Base object counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_only(self):
        """Rectangle.create(**{'id': 89}) sets only the id."""
        r = Rectangle.create(**{"id": 89})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

    def test_id_width(self):
        """Rectangle.create(**{'id': 89, 'width': 1})."""
        r = Rectangle.create(**{"id": 89, "width": 1})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")

    def test_id_width_height(self):
        """Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})."""
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2})
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/2")

    def test_id_width_height_x(self):
        """Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})."""
        r = Rectangle.create(**{"id": 89, "width": 1, "height": 2, "x": 3})
        self.assertEqual(str(r), "[Rectangle] (89) 3/0 - 1/2")

    def test_all(self):
        """Rectangle.create with every key set."""
        r = Rectangle.create(
            **{"id": 89, "width": 1, "height": 2, "x": 3, "y": 4})
        self.assertEqual(str(r), "[Rectangle] (89) 3/4 - 1/2")
        self.assertIsInstance(r, Rectangle)

    def test_new_object(self):
        """create returns a different object with the same values."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)


class TestRectangleLoadFromFile(unittest.TestCase):
    """Tests for Rectangle.load_from_file."""

    def setUp(self):
        """Reset the counter and remove Rectangle.json before each test."""
        Base._Base__nb_objects = 0
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def tearDown(self):
        """Remove Rectangle.json after each test."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_no_file(self):
        """Rectangle.load_from_file() returns [] when the file is missing."""
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_file_exists(self):
        """Rectangle.load_from_file() rebuilds the saved rectangles."""
        inputs = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        Rectangle.save_to_file(inputs)
        outputs = Rectangle.load_from_file()
        self.assertEqual(len(outputs), 2)
        for before, after in zip(inputs, outputs):
            self.assertIsInstance(after, Rectangle)
            self.assertIsNot(before, after)
            self.assertEqual(str(before), str(after))

    def test_saved_none(self):
        """Loading after Rectangle.save_to_file(None) returns []."""
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
