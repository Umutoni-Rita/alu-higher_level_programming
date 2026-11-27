#!/usr/bin/python3
"""Unittests for the Base class defined in models/base.py."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


def reset_counter():
    """Reset the private object counter of Base to 0 between tests."""
    Base._Base__nb_objects = 0


def remove_files():
    """Delete any JSON or CSV file the tests may have created."""
    for name in ("Base.json", "Rectangle.json", "Square.json",
                 "Base.csv", "Rectangle.csv", "Square.csv"):
        if os.path.exists(name):
            os.remove(name)


class TestBaseInstantiation(unittest.TestCase):
    """Tests for the Base constructor and id management."""

    def setUp(self):
        """Reset the object counter before each test."""
        reset_counter()

    def test_no_id(self):
        """A Base without id gets id 1 when it is the first one."""
        self.assertEqual(Base().id, 1)

    def test_sequential_ids(self):
        """Ids are assigned in increasing order."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual((b1.id, b2.id, b3.id), (1, 2, 3))

    def test_given_id(self):
        """A given id is used as is."""
        self.assertEqual(Base(12).id, 12)

    def test_given_id_does_not_increment(self):
        """Giving an id does not change the automatic counter."""
        Base()
        Base(12)
        self.assertEqual(Base().id, 2)

    def test_none_id(self):
        """Passing None explicitly behaves like no id."""
        self.assertEqual(Base(None).id, 1)

    def test_zero_id(self):
        """An id of 0 is kept (it is not None)."""
        self.assertEqual(Base(0).id, 0)

    def test_negative_id(self):
        """A negative id is kept as is."""
        self.assertEqual(Base(-5).id, -5)

    def test_non_int_id(self):
        """Base does not check the type of id."""
        self.assertEqual(Base("hello").id, "hello")

    def test_id_is_public(self):
        """The id attribute can be changed directly."""
        b = Base()
        b.id = 99
        self.assertEqual(b.id, 99)

    def test_nb_objects_is_private(self):
        """The counter cannot be accessed by its plain name."""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_too_many_args(self):
        """Base accepts at most one argument."""
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestToJsonString(unittest.TestCase):
    """Tests for the static method Base.to_json_string."""

    def setUp(self):
        """Reset the object counter before each test."""
        reset_counter()

    def test_none(self):
        """None gives the string '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        """An empty list gives the string '[]'."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_returns_string(self):
        """The result is a str."""
        d = Rectangle(10, 7, 2, 8).to_dictionary()
        self.assertIsInstance(Base.to_json_string([d]), str)

    def test_one_dict(self):
        """A list with one dictionary is converted correctly."""
        d = Rectangle(10, 7, 2, 8).to_dictionary()
        self.assertEqual(json.loads(Base.to_json_string([d])), [d])

    def test_two_dicts(self):
        """A list with two dictionaries is converted correctly."""
        d1 = Rectangle(10, 7, 2, 8).to_dictionary()
        d2 = Square(3).to_dictionary()
        result = Base.to_json_string([d1, d2])
        self.assertEqual(json.loads(result), [d1, d2])

    def test_exact_string(self):
        """The output uses double quotes like real JSON."""
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_no_args(self):
        """Calling without argument raises TypeError."""
        with self.assertRaises(TypeError):
            Base.to_json_string()


class TestFromJsonString(unittest.TestCase):
    """Tests for the static method Base.from_json_string."""

    def test_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_empty_json_list(self):
        """The string '[]' gives an empty list."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_returns_list(self):
        """The result is a list."""
        result = Base.from_json_string('[{"id": 89, "width": 10}]')
        self.assertIsInstance(result, list)

    def test_round_trip(self):
        """from_json_string undoes to_json_string."""
        data = [{"id": 89, "width": 10, "height": 4},
                {"id": 7, "width": 1, "height": 7}]
        json_str = Rectangle.to_json_string(data)
        self.assertEqual(Rectangle.from_json_string(json_str), data)

    def test_no_args(self):
        """Calling without argument raises TypeError."""
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestSaveToFile(unittest.TestCase):
    """Tests for the class method Base.save_to_file."""

    def setUp(self):
        """Reset the object counter before each test."""
        reset_counter()

    def tearDown(self):
        """Remove the JSON files created by the tests."""
        remove_files()

    def read(self, filename):
        """Return the parsed JSON content of filename."""
        with open(filename, "r", encoding="utf-8") as f:
            return json.loads(f.read())

    def test_rectangles(self):
        """A list of rectangles is saved to Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertEqual(self.read("Rectangle.json"),
                         [r1.to_dictionary(), r2.to_dictionary()])

    def test_squares(self):
        """A list of squares is saved to Square.json."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        self.assertEqual(self.read("Square.json"),
                         [s1.to_dictionary(), s2.to_dictionary()])

    def test_none(self):
        """None saves an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_empty_list(self):
        """An empty list saves an empty list."""
        Square.save_to_file([])
        with open("Square.json", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_overwrite(self):
        """Saving again replaces the previous content."""
        Rectangle.save_to_file([Rectangle(1, 1), Rectangle(2, 2)])
        r = Rectangle(3, 3)
        Rectangle.save_to_file([r])
        self.assertEqual(self.read("Rectangle.json"), [r.to_dictionary()])

    def test_base_none(self):
        """Base.save_to_file(None) writes an empty list to Base.json."""
        Base.save_to_file(None)
        self.assertEqual(self.read("Base.json"), [])

    def test_no_args(self):
        """Calling without argument raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestCreate(unittest.TestCase):
    """Tests for the class method Base.create."""

    def setUp(self):
        """Reset the object counter before each test."""
        reset_counter()

    def test_rectangle(self):
        """create builds an equal but distinct Rectangle."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertIsInstance(r2, Rectangle)

    def test_square(self):
        """create builds an equal but distinct Square."""
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)
        self.assertIsInstance(s2, Square)

    def test_partial_dictionary(self):
        """Missing keys keep the dummy values."""
        r = Rectangle.create(id=89, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 4/1")

    def test_invalid_value(self):
        """Invalid values are still validated."""
        with self.assertRaises(ValueError):
            Rectangle.create(width=-1)


class TestLoadFromFile(unittest.TestCase):
    """Tests for the class method Base.load_from_file."""

    def setUp(self):
        """Reset the counter and remove old files before each test."""
        reset_counter()
        remove_files()

    def tearDown(self):
        """Remove the JSON files created by the tests."""
        remove_files()

    def test_no_file(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_rectangles(self):
        """Saved rectangles are loaded back as new equal Rectangles."""
        inputs = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        Rectangle.save_to_file(inputs)
        outputs = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in inputs], [str(r) for r in outputs])
        for r in outputs:
            self.assertIsInstance(r, Rectangle)

    def test_squares(self):
        """Saved squares are loaded back as new equal Squares."""
        inputs = [Square(5), Square(7, 9, 1)]
        Square.save_to_file(inputs)
        outputs = Square.load_from_file()
        self.assertEqual([str(s) for s in inputs], [str(s) for s in outputs])
        for s in outputs:
            self.assertIsInstance(s, Square)

    def test_empty_file_list(self):
        """A file saved from None loads as an empty list."""
        Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_too_many_args(self):
        """load_from_file takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle.load_from_file("Rectangle.json")


class TestCsv(unittest.TestCase):
    """Tests for Base.save_to_file_csv, load_from_file_csv, csv_fields."""

    def setUp(self):
        """Reset the counter and remove old CSV files before each test."""
        reset_counter()
        remove_files()

    def tearDown(self):
        """Remove the CSV files created by the tests."""
        remove_files()

    def test_csv_fields(self):
        """Each class uses its own column order."""
        self.assertEqual(Rectangle.csv_fields(),
                         ["id", "width", "height", "x", "y"])
        self.assertEqual(Square.csv_fields(), ["id", "size", "x", "y"])

    def test_file_names(self):
        """The file is named after the class that calls the method."""
        Rectangle.save_to_file_csv([Rectangle(1, 1)])
        Square.save_to_file_csv([Square(1)])
        self.assertTrue(os.path.exists("Rectangle.csv"))
        self.assertTrue(os.path.exists("Square.csv"))

    def test_base_none(self):
        """Base.save_to_file_csv(None) writes an empty list to Base.csv."""
        Base.save_to_file_csv(None)
        with open("Base.csv", "r", encoding="utf-8") as f:
            self.assertEqual(f.read(), "[]")

    def test_load_no_file(self):
        """A missing CSV file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file_csv(), [])
        self.assertEqual(Square.load_from_file_csv(), [])

    def test_load_empty_file(self):
        """An empty CSV file gives an empty list."""
        open("Rectangle.csv", "w").close()
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_round_trip_ids(self):
        """Ids follow the 100-main example (dummies use ids 3 and 4)."""
        Rectangle.save_to_file_csv([Rectangle(10, 7, 2, 8), Rectangle(2, 4)])
        Rectangle.load_from_file_csv()
        squares = [Square(5), Square(7, 9, 1)]
        self.assertEqual([s.id for s in squares], [5, 6])
        Square.save_to_file_csv(squares)
        loaded = Square.load_from_file_csv()
        self.assertEqual([str(s) for s in loaded],
                         ["[Square] (5) 0/0 - 5", "[Square] (6) 9/1 - 7"])

    def test_save_no_args(self):
        """Calling save_to_file_csv without argument raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()


if __name__ == "__main__":
    unittest.main()
