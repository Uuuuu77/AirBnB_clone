#!/usr/bin/python3
"""
    test_models/base_model.py of testing BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models.state import State
import pycodestyle
import os
import uuid
from datetime import datetime


class TestState(unittest.TestCase):
    """ Testing State class """
    @classmethod
    def setUpClass(cls):
        """ Set up class instances """
        cls.s1 = State()
        cls.s1.name = "State1"

        cls.s2 = State()
        cls.s2.name = "State2"

        cls.d = cls.s2.to_dict()

        cls.s3 = State(**cls.d)

    @classmethod
    def tearDownClass(cls):
        """ Tears down created instances """
        del cls.s1
        del cls.s2
        del cls.s3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """ Testing for documentation """
        self.assertTrue(len(State.__doc__) >= 20, "Short or no doc")

    def test_pycodestyle(self):
        """ Testing for pycodestyle format """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/state.py',
                                     'tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instances(self):
        """ Testing for instances """
        self.assertIsInstance(self.s1, State, "Not instance of State")
        self.assertIsInstance(self.s2, State, "Not instance of State")
        self.assertIsInstance(self.s3, State, "Not instance of State")

    def test_subClass(self):
        """ Testing for subclass """
        self.assertTrue(issubclass(State, BaseModel))

    def test_attributes(self):
        """ Testing attributes if is not None """
        self.assertIsNotNone(self.s1.id)
        self.assertIsNotNone(self.s1.created_at)
        self.assertIsNotNone(self.s1.updated_at)
        self.assertIsNotNone(self.s1.name)

    def test_attributes_2(self):
        """ Testing attributes """
        self.assertTrue(hasattr(self.s2, 'id'))
        self.assertTrue(hasattr(self.s2, 'created_at'))
        self.assertTrue(hasattr(self.s2, 'updated_at'))
        self.assertTrue(hasattr(self.s2, 'name'))

    def test_attributes_type(self):
        """ Testing attributes types """
        self.assertIsInstance(self.s2.name, str)
        self.assertIsInstance(self.s1.created_at, datetime)
        self.assertIsInstance(self.s1.updated_at, datetime)
        self.assertIsInstance(uuid.UUID(self.s1.id), uuid.UUID)

    def test_id_unique(self):
        """ Testing if two id's are unique """
        self.assertNotEqual(self.s1.id, self.s2.id)

    def test_str(self):
        """ Testing string[__str__] return """
        s1 = f"[State] ({self.s1.id}) {self.s1.__dict__}"
        s3 = f"[State] ({self.s3.id}) {self.s3.__dict__}"
        self.assertEqual(str(self.s1), s1)
        self.assertEqual(str(self.s3), s3)

    def test_save(self):
        """ Testing save updated_time """
        self.s1.save()
        self.assertNotEqual(self.s1.updated_at, self.s1.created_at)

    def test_to_dict_class(self):
        """ Testing if __class__ added to [to_dict] """
        self.assertIsNotNone(self.d['__class__'])
        self.assertEqual(self.d['__class__'], 'State')

    def test_kwargs_false(self):
        """ Testing if object created by kwargs is different """
        self.assertFalse(self.s3 is self.s2)


if __name__ == "__main__":
    unittest.main()
