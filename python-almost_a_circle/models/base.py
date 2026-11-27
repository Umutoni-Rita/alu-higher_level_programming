#!/usr/bin/python3
"""This module defines the Base class, the parent of every shape class.

It manages the id of each object and provides JSON and CSV serialization
helpers to save instances to files and load them back.
"""
import csv
import json


class Base:
    """Base class that manages the id attribute of all future classes.

    It also converts lists of objects to and from JSON strings and files.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance with a given or automatic id.

        Args:
            id (int): the id to use; if None, the next automatic id is used.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries.

        Returns the string "[]" if list_dictionaries is None or empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries represented by a JSON string.

        Returns an empty list if json_string is None or empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of list_objs to <Class name>.json.

        If list_objs is None, an empty list is saved. The file is overwritten.
        """
        if list_objs is None:
            list_objs = []
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance of cls with all attributes from dictionary.

        A dummy instance is created first, then update() sets the real values.
        """
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of cls instances loaded from <Class name>.json.

        Returns an empty list if the file does not exist.
        """
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                list_dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def csv_fields(cls):
        """Return the CSV column order used for instances of cls.

        Square: id,size,x,y - Rectangle (and others): id,width,height,x,y.
        """
        if cls.__name__ == "Square":
            return ["id", "size", "x", "y"]
        return ["id", "width", "height", "x", "y"]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write list_objs to <Class name>.csv, one object per line.

        If list_objs is None or empty, "[]" is written, like the JSON version.
        """
        with open(cls.__name__ + ".csv", "w", newline="",
                  encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
                return
            writer = csv.DictWriter(f, fieldnames=cls.csv_fields())
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of cls instances loaded from <Class name>.csv.

        Returns an empty list if the file does not exist or holds no objects.
        """
        try:
            with open(cls.__name__ + ".csv", "r", newline="",
                      encoding="utf-8") as f:
                content = f.read()
        except FileNotFoundError:
            return []
        if content.strip() in ("", "[]"):
            return []
        reader = csv.DictReader(content.splitlines(),
                                fieldnames=cls.csv_fields())
        instances = []
        for row in reader:
            values = {key: int(value) for key, value in row.items()}
            instances.append(cls.create(**values))
        return instances
