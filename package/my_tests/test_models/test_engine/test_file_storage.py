#!/usr/bin/env python3
"""
This module contains tests for the module file storage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from pathlib import Path


class TestFileStorage(unittest.TestCase):
    """
    """

    @classmethod
    def setUp(cls):
        """
        initializes a new instance of FileStorage for each test
        """
        cls.storage = FileStorage()

    @classmethod
    def tearDown(cls):
        """
        clears up after every test
        """

        _path = Path(cls.storage._FileStorage__file_path)
        if _path.is_file():
            _path.unlink()

    def test_all(self):
        """
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        """
        checks the __objects attribute for the model key
        """
        obj = BaseModel()
        self.storage.new(obj)
        key = f"BaseModel.{obj.id}"
        self.assertIn(key, self.storage.all())
        retrieved = self.storage.all()[key]
        self.assertEqual(obj, retrieved)

    def test_save(self):
        """
        Checks if the file exists and if the models saved have the same id
        with the ones that reloaded
        """
        self.storage.save()
        _path = Path(self.storage._FileStorage__file_path)
        self.assertTrue(_path.is_file())

        _object = BaseModel()
        object_id = _object.id
        self.storage.new(_object)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(f"BaseModel.{object_id}", new_storage.all())

    def test_update_time(self):
        """
        tests for inconcistency in the updated_at attribute
        before and after calling the save method
        """

        _object = BaseModel()
        update_time = _object.updated_at
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        reloaded = new_storage.all()[f"BaseModel.{_object.id}"]
        self.assertEqual(update_time, reloaded.updated_at)


    if __name__ == '__main__':
        unittest.main()
