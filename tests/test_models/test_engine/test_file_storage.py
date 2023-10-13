#!/usr/bin/python3
"""
    test_models/test_engine/test_file_storage.py of testing FileStorage class
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import pycodestyle
import os
import uuid
from datetime import datetime
from json import load


class TestFileStorage(unittest.TestCase):
    """ Testing our FileStorage class """
    maxdiff = None

    @classmethod
    def setUpClass(cls):
        """ Set up class instance """
        cls.bm1 = BaseModel()
        cls.bm1.color = "pink"
        cls.bm1.size = 10

        cls.bm2 = BaseModel()
        cls.bm2.colour = "blue"
        cls.bm2.size = 8.45

        cls.store = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """ It tears down created instances """
        del cls.bm1
        del cls.bm2
        try:
            os.remove("_file.json")
        except FileNotFoundError:
            pass

    def test_documentation(self):
        """ Testing documentation """
        self.assertTrue(len(FileStorage.__doc__) >= 20, "Short or no doc")
        self.assertTrue(len(FileStorage.new.__doc__) >= 20, "Short doc")
        self.assertTrue(len(FileStorage.save.__doc__) >= 20, "Short doc")
        self.assertTrue(len(FileStorage.reload.__doc__) >= 20, "Short doc")

    def test_pycodestyle(self):
        """ Testing pycodestyle format """
        pystyle = pycodestyle.StyleGuide(quite=True)
        y = "tests/test_models/test_engine/test_file_storage.py"
        result = pystyle.check_files(["models/engine/file_storage.py", y])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_instance(self):
        """ Testing is it's instance """
        self.assertIsInstance(self.store, FileStorage)

    def test_all(self):
        """ Testing if all dictionary of _objects returns """
        k1 = f"BaseModel.{self.bm1.id}"
        k2 = f"BaseModel.{self.bm2.id}"
        all = {x: y for x, y in self.store.all().items() if x in [k1, k2]}
        z = {k1: self.bm1, k2: self.bm2}
        self.assertEqual(all, z)

    def test_all_type(self):
        """ Tests if all dictionary returns """
        dt = self.store.all()
        self.assertIsInstance(dt, dict)

    def test_new(self):
        """ Testing if new adds to __objects dictionary """
        new_obj = BaseModel()
        self.store.new(new_obj)
        new_key = f"BaseModel.{new_obj.id}"
        keys = [x for x in self.store.all().keys()]
        values = [y for y in self.store.all().values()]
        self.assertIn(new_key, keys)
        self.assertIn(new_obj, values)

    def test_save_file(self):
        """ Testing if object is saved in a file """
        sav_obj = BaseModel()
        sav_key = f"BaseModel.{sav_obj.id}"
        self.store.save()
        with open("file.json", encoding="UTF-8") as _file:
            from_json = load(_file)
            keys = [x for x in from_json.keys()]
            values = [y for y in from_json.values()]
            self.assertIn(sav_key, keys)
            self.assertIn(sav_obj.to_dict(), values)

    def test_reload(self):
        """ Testing if reload saves to _objects """
        self.store.save()
        self.store.reload()
        key_obj = [x for x in self.store.all().keys()]
        with open("file.json", encoding="UTF-8") as _file:
            from_json = load(_file)
            keys = [x for x in from_json.keys()]
            self.assertEqual(keys, keys_obj)

    def test_reload_no_file(self):
        """ Testing reload if there is no file """
        self.store.save()
        os.remove("file.json")
        self.store.reload()
        keys_obj = [x for x in self.store.all().keys()]
        self.assertIsNotNone(self.store.all())
