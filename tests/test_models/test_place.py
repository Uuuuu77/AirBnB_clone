#!/usr/bin/python3
"""
    test_models/base_model.py of testing BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
import pycodestyle
import os
import uuid
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ Testing Place class """
    @classmethod
    def setUpClass(cls):
        """ Set up class instances """
        cls.p1 = Place()
        cls.p1.name = "Place1"
        cls.p1.city_id = "1234"
        cls.p1.user_id = "12345"
        cls.p1.description = "good"
        cls.p1.number_rooms = 5
        cls.p1.number_bathrooms = 2
        cls.p1.max_guest = 7
        cls.p1.price_by_night = 400
        cls.p1.latitude = 4.55
        cls.p1.longitude = 1.24
        cls.p1.amenity_ids = [123, 1111]

        cls.p2 = Place()

        cls.d = cls.p2.to_dict()

        cls.p3 = Place(**cls.d)

    @classmethod
    def tearDownClass(cls):
        """ Tears down created instances """
        del cls.p1
        del cls.p2
        del cls.p3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """ Testing for documentation """
        self.assertTrue(len(Place.__doc__) >= 20, "Short or no doc")

    def test_pycodestyle(self):
        """ Testing for pycodestyle format """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/place.py',
                                     'tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """ Testing for instances """
        self.assertIsInstance(self.p1, Place, "Not instance of Place")
        self.assertIsInstance(self.p2, Place, "Not instance of Place")
        self.assertIsInstance(self.p3, Place, "Not instance of Place")

    def test_subclass(self):
        """ Testing for subclass """
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes(self):
        """ Testing attributes is is not None """
        self.assertIsNotNone(self.p1.id)
        self.assertIsNotNone(self.p1.created_at)
        self.assertIsNotNone(self.p1.updated_at)
        self.assertIsNotNone(self.p1.name)

    def test_attributes_2(self):
        """ Testing attributes """
        self.assertTrue(hasattr(self.p2, 'id'))
        self.assertTrue(hasattr(self.p2, 'created_at'))
        self.assertTrue(hasattr(self.p2, 'updated_at'))
        self.assertTrue(hasattr(self.p2, 'name'))
        self.assertTrue(hasattr(self.p2, 'city_id'))
        self.assertTrue(hasattr(self.p2, 'user_id'))
        self.assertTrue(hasattr(self.p2, 'amenity_ids'))
        self.assertTrue(hasattr(self.p2, 'description'))
        self.assertTrue(hasattr(self.p2, 'number_rooms'))
        self.assertTrue(hasattr(self.p2, 'number_bathrooms'))
        self.assertTrue(hasattr(self.p2, 'max_guest'))
        self.assertTrue(hasattr(self.p2, 'price_by_night'))
        self.assertTrue(hasattr(self.p2, 'latitude'))
        self.assertTrue(hasattr(self.p2, 'longitude'))

    def test_attribute_type(self):
        """ Testing for attributes types """
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p1.city_id, str)
        self.assertIsInstance(self.p1.user_id, str)
        self.assertIsInstance(self.p1.description, str)
        self.assertIsInstance(self.p1.number_rooms, int)
        self.assertIsInstance(self.p1.number_bathrooms, int)
        self.assertIsInstance(self.p1.max_guest, int)
        self.assertIsInstance(self.p1.price_by_night, int)
        self.assertIsInstance(self.p1.latitude, float)
        self.assertIsInstance(self.p1.longitude, float)
        self.assertIsInstance(self.p1.amenity_ids, list)
        self.assertIsInstance(self.p1.created_at, datetime)
        self.assertIsInstance(self.p1.updated_at, datetime)
        self.assertIsInstance(uuid.UUID(self.p1.id), uuid.UUID)

    def test_id_unique(self):
        """ Testing if two id's are unique """
        self.assertNotEqual(self.p1.id, self.p2.id)

    def test_str(self):
        """ Testing string[__str__] returns """
        s1 = f"[Place] ({self.p1.id}) {self.p1.__dict__}"
        s3 = f"[Place] ({self.p3.id}) {self.p3.__dict__}"
        self.assertEqual(str(self.p1), s1)
        self.assertEqual(str(self.p3), s3)

    def test_save(self):
        """ Testing saving updated_time """
        self.p1.save()
        self.assertNotEqual(self.p1.updated_at, self.p1.created_at)

    def test_to_dict_class(self):
        """ Testing if __class__ added to [to_dict] """
        self.assertIsNotNone(self.d['__class__'])
        self.assertEqual(self.d['__class__'], 'Place')

    def test_kwargs_false(self):
        """ Testing if object created by kwargs is different """
        self.assertFalse(self.p3 is self.p2)


if __name__ == "__main__":
    unittest.main()
