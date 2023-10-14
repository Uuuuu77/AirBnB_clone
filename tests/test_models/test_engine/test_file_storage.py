#!/usr/bin/env python3
"""
This module contains tests for the module file storage
"""
import unittest
from models.file_storage import FileStorage
fropm models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    """

    def setUp(self):
        """
        initializes a new instance of FileStorage for each test
        """
        self.storage = FileStorage()

