#!/usr/bin/python3
"""
    test_models/base_model,py of testing BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
import pycodestyle
import os
import uuid
from datetime import datetime


class TestReview(unittest.TestCase):
    """ Testing Review class """
    @classmethod
    def setUpClass(cls):
        """ Set up class instances """
        cls.r1 = Review()
        cls.r1.place_id = "234"
        cls.r1.user_id = "123"
        cls.r1.text = "hello"

        cls.r2 = Review()

        cls.d = cls.r2.to_dict()

        cls.r3 = Review(**cls.d)

    @classmethod
    def tearDownClass(cls):
        """ Tears down created instances """
        del cls.r1
        del cls.r2
        del cls.r3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """ Testing for documentation """
        self.assertTrue(len(Review.__doc__) >= 20, "Short or no doc")

    def test_pycodestyle(self):
        """ Testing for pycodestyle format """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/review.py',
                                     'tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instances(self):
        """ Testing for instances """
        self.assertIsInstance(self.r1, Review, "Not instance of Review")
        self.assertIsInstance(self.r2, Review, "Not instance of Review")
        self.assertIsInstance(self.r3, Review, "Not instance of Review")

    def test_subclass(self):
        """ Testing for subclass """
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attributes(self):
        """ Testing attributes if is not None """
        self.assertIsNotNone(self.r1.id)
        self.assertIsNotNone(self.r1.created_at)
        self.assertIsNotNone(self.r1.updated_at)
        self.assertIsNotNone(self.r1.text)

    def test_attributes_2(self):
        """ Testing for attributes """
        self.assertTrue(hasattr(self.r2, 'id'))
        self.assertTrue(hasattr(self.r2, 'created_at'))
        self.assertTrue(hasattr(self.r2, 'updated_at'))
        self.assertTrue(hasattr(self.r2, 'place_id'))
        self.assertTrue(hasattr(self.r2, 'user_id'))
        self.assertTrue(hasattr(self.r2, 'text'))

    def test_attribute_type(self):
        """ Testing attributes types """
        self.assertIsInstance(self.r1.place_id, str)
        self.assertIsInstance(self.r1.user_id, str)
        self.assertIsInstance(self.r1.text, str)
        self.assertIsInstance(self.r1.created_at, datetime)
        self.assertIsInstance(self.r1.updated_at, datetime)
        self.assertIsInstance(uuid.UUID(self.r1.id), uuid.UUID)

    def test_id_unique(self):
        """ Testing if two id's are unique """
        self.assertNotEqual(self.r1.id, self.r2.id)

    def test_str(self):
        """ Testing string[__str__] return """
        s1 = f"[Review] ({self.r1.id}) {self.r1.__dict__}"
        s3 = f"[Review] ({self.r3.id}) {self.r3.__dict__}"
        self.assertEqual(str(self.r1), s1)
        self.assertEqual(str(self.r3), s3)

    def test_save(self):
        """ Testing saving updated_time """
        self.r1.save()
        self.assertNotEqual(self.r1.updated_at, self.r1.created_at)

    def test_to_dict_class(self):
        """ Testing is __class__ added to [to_dict] """
        self.assertIsNotNone(self.d['__class__'])
        self.assertEqual(self.d['__class__'], 'Review')

    def test_kwargs_false(self):
        """ Testing if object created by kwargd is different """
        self.assertFalse(self.r3 is self.r2)


if __name__ == "__main__":
    unittest.main()
