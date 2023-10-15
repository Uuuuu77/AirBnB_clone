#!/usr/bin/env python3
"""
This module contains the class filestorage where we will do the serialization
and deserialization.
"""
from pathlib import Path
from contextlib import suppress
import json
from models.base_model import BaseModel


class FileStorage:
    """
    This is the FileStorage class which handles how objects are stored
    in a file so as to  maintain data persistency
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary stored in __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        to_json = {}

        for key, value in FileStorage.__objects.items():
            to_json[key] = value.to_dict()

            with open(self.__file_path, 'w', encoding='utf-8') as file:
                json.dump(to_json, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        """

        with suppress(FileNotFoundError):
            path = Path(FileStorage.__file_path)
            if path.is_file():
                with open(self.__file_path, 'r', encoding='utf-8') as f:
                    from_json = json.load(f)

                    for i, j in from_json.items():
                        class_name = j.get("__class__")
                        if class_name is not None:
                            cls = eval(class_name)
                            if isinstance(cls, type):

                                instance = cls(**j)

                                self.__objects[i] = instance
