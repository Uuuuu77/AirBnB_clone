#!/usr/bin/python3
"""
    models/engine/file_storage.py of JSON serialization and deserialization.
"""
from os.path import isfile
from json import dump, load
import sys


class FileStorage:
    """
        Serialize instance to a JSON file & deserialize JSON file to instance.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ It sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        sav_dict = {}
        for key, val in FileStorage.__objects.items():
            sav_dict.update({key: val.to_dict()})
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as f:
            dump(sav.dict, f)

    def reload(self):
        """ Deserialize the JSON file to __objects if it exists """
        from models import base_model, user, amenity
        from models import place, city, state, review
        cls = {'BaseModel': base_model, 'User': user, 'Amenity': amenity,
               'Place': place, 'City': city, 'State': state, 'Review': review}
        if is_file(FileStorage.__file_path):
            with open(FileStorage.__file_path, encoding="UTF-8") as _file:
                from_json = load(_file)
                for val in from_json.values():
                    cls_name = val["__class__"]
                    cls_obj = getattr(cls[cls_name], cls_name)
                    # if cls_name == "BaseModel":
                    # cls_obj = getattr(base_model, cls_name)
                    # elif cls_name == "User":
                    # cls_obj = getattr(user, cls_name)
                    self.new(cls_obj(**val))
