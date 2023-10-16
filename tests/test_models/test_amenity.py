#!/usr/bin/python3
"""
    test_models/base_model.py of testing BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import pycodestyle
import os
import uuid
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Tests for Amenity class """
    @classmethod
    def setUpClass(cls):
        """ Setting up class instance """
        cls.a1 = Amenity()
        cls.a1.name = "Amenity1"

        cls.a2 = Amenity()
        cls.a2.name = "Amenity2"

        cls.d = cls.a2.to_dict()

        cls.a3 = Amenity(**cls.d)

    @classmethod
    def tearDownClass(cls):
        """ Tears down created instances """
        del cls.a1
        del cls.a2
        del cls.a3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """ Testing for documentation """
        self.assertTrue(len(Amenity.__doc__) >= 20, "short or no doc")

    def test_pycodestyle(self):
        """ Testing for pycodestyle format """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/amenity.py',
                                     'tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """ Testing for instances """
        self.assertIsInstance(self.a1, Amenity, "Not instance of Amenity")
        self.assertIsInstance(self.a2, Amenity, "Not instance of Amenity")
        self.assertIsInstance(self.a3, Amenity, "Not instance of Amenity")

    def test_subClass(self):
        """ Testing for a subclass """
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attribute0(self):
        """ Testing attr if is not none """
        self.assertIsNotNone(self.a1.id)
        self.assertIsNotNone(self.a1.created_at)
        self.assertIsNotNone(self.a1.updated_at)
        self.assertIsNotNone(self.a1.name)

    def test_attribute1(self):
        """ Testing for attribute """
        self.assertTrue(hasattr(self.a2, 'id'))
        self.assertTrue(hasattr(self.a2, 'created_at'))
        self.assertTrue(hasattr(self.a2, 'updated_at'))
        self.assertTrue(hasattr(self.a2, 'name'))

    def test_attribute_type(self):
        """ Testing attribute type """
        self.assertIsInstance(self.a2.name, str)
        self.assertIsInstance(self.a1.created_at, datetime)
        self.assertIsInstance(self.a1.updated_at, datetime)
        self.assertIsInstance(uuid.UUID(self.a1.id), uuid.UUID)

    def test_id_unique(self):
        """ Testing if two id's are unique """
        self.assertNotEqual(self.a1.id, self.a2.id)

    def test_str(self):
        """ Testing string return """
        s1 = f"[Amenity] ({self.a1.id}) {self.a1.__dict__}"
        s3 = f"[Amenity] ({self.a3.id}) {self.a3.__dict__}"
        self.assertEqual(str(self.a1), s1)
        self.assertEqual(str(self.a3), s3)

    def test_save(self):
        """ Testing save updated_time """
        self.a1.save()
        self.assertNotEqual(self.a1.updated_at, self.a1.created_at)

    def test_to_dict_class(self):
        """ Testing if __class__ added to to_dict """
        self.assertIsNotNone(self.d['__class__'])
        self.assertEqual(self.d['__class__'], 'Amenity')

    def test_kwargs_false(self):
        """ Testing if objects created by kwargs different """
        self.assertFalse(self.a3 is self.a2)


if __name__ == "__main__":
    unittest.main()
