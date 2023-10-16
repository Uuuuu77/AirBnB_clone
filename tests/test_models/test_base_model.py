#!/usr/bin/python3
"""
    test_models/base_model.py of testing BaseModel class.
"""
import unittest
from models.base_model import BaseModel
import pycodestyle
import os
import uuid
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Testing BaseModel class """
    def setUpClass(cls):
        """ Set up class instances """
        cls.bm1 = BaseModel()
        cls.bm1.color = "pink"
        cls.bm1.size = 10

        cls.bm2 = BaseModel()
        cls.bm2.color = 'blue'
        cls.bm2.size = 8.45
        cls.d = cls.bm2.to_dict()

        cls.bm3 = BaseModel(**cls.d)

    @classmethod
    def tearDownClass(cls):
        """ Tears down created instances """
        del cls.bm1
        del cls.bm2
        del cls.bm3
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """ Testing for documentation """
        self.assertTrue(len(BaseModel.__doc__) >= 20, "Short or no doc")
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 20, "Short doc")
        self.assertTrue(len(BaseModel.save.__doc__) >= 20, "Short doc")
        self.assertTrue(len(BaseModel.to_dict.__doc__) >= 20, "Short doc")
        self.assertTrue(len(BaseModel.__str__.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        """ Testing for pycodestyle format """
        pystyle = pycodestyle.StyleGuide(quiet=True)
        result = pystyle.check_files(['models/base_model.py',
                                     'tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """ Testing our instances """
        self.assertIsInstance(self.bm1, BaseModel, "Not instance of BaseModel")
        self.assertIsInstance(self.bm2, BaseModel, "Not instance of BaseModel")
        self.assertIsInstance(self.bm3, BaseModel, "Not instance of BaseModel")

    def test_attributes(self):
        """ Testing for attributes if is not None """
        self.assertIsNotNone(self.bm1.id)
        self.assertIsNotNone(self.bm1.created_at)
        self.assertIsNotNone(self.bm1.updated_at)
        self.assertIsNotNone(self.bm1.color)
        self.assertIsNotNone(self.bm1.size)

    def test_id_str(self):
        """ Testing id is a class str """
        self.assertIsInstance(self.bm1.id, str)

    def test_id_unique(self):
        """ Testing if two id's are unique """
        self.assertNotEqual(self.bm1.id, self.bm2.id)

    def test_id_uuid(self):
        """ Testing if id is uuid """
        self.assertIsInstance(uuid.UUID(self.bm1.id), uuid.UUID)

    def test_created_at_datetime(self):
        """ Testing if [created_at] is datetime object """
        self.assertIsInstance(self.bm1.created_at, datetime)

    def test_updated_at_datetime(self):
        """ Testing if [updated_at] is datetime object """
        self.assertIsInstance(self.bm1.updated_at, datetime)

    def test_str(self):
        """ Testing __str__ returns """
        s1 = f"[BaseModel] ({self.bm1.id}) {self.bm1.__dict__}"
        s3 = f"[BaseModel] ({self.bm3.id}) {self.bm3.__dict__}"
        self.assertEqual(str(self.bm1), s1)
        self.assertEqual(str(self.bm3), s3)

    def test_save(self):
        """ Testing saving update_time """
        self.bm1.save()
        self.assertNotEqual(self.bm1.updated_at, self.bm1.created_at)

    def test_to_dict_class(self):
        """ Testing if __class__ added to [to_dict] """
        self.assertIsNotNone(self.d['__class__'])
        self.assertEqual(self.d['__class__'], 'BaseModel')

    def test_to_dict_created_at(self):
        """ Testing if [created_at] is converted to isoformat """
        self.assertEqual(self.d['created_at'], self.bm2.created_at.isoformat())
        self.assertIsInstance(self.d['created_at'], str)

    def test_to_dict_updated_at(self):
        """ Testing if [updated_at] is converted to isoformat """
        self.assertEqual(self.d['updated_at'], self.bm2.updated_at.isoformat())
        self.assertIsInstance(self.d['updated_at'], str)

    def test_to_dict_id(self):
        """ Testing if id is the same """
        self.assertEqual(self.d['id'], self.bm2.id)

    def test_to_dict_added_attributes(self):
        """ Testing if added attributes are the same """
        self.assertEqual(self.d['color'], 'blue')
        self.assertEqual(self.d['size'], 8.45)

    def test_to_dict_type(self):
        """ Testing if [to_dict] returns a dictionary """
        self.assertIsInstance(self.d, dict)

    def test_kwargs_attributes(self):
        """ Testing if attributes of created instance by kwargs is equal """
        self.assertEqual(self.bm3.id, self.bm2.id)
        self.assertEqual(self.bm3.created_at, self.bm2.created_at)
        self.assertEqual(self.bm3.updated_at, self.bm2.updated_at)
        self.assertEqual(self.bm3.color, self.bm2.color)
        self.assertEqual(self.bm3.size, self.bm2.size)

    def test_kwargs_classname_not_added(self):
        """ Testing if __class__ name not added as attribute """
        self.assertEqual(self.bm3.__dict__, self.bm2.__dict__)

    def test_kwargs_false(self):
        """ Testing if object created by kwargs differently """
        self.assertFalse(self.bm3 is self.bm2)
