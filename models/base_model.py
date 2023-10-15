#!/usr/bin/env python3
"""
This module contains the class BaseModel which defines
all common attributes/methods for other classes
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    this class defines all common attributes/methods for all classes
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    new_val = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, new_val)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from . import storage
            storage.new(self)

    def __str__(self):
        """
        Prints a string in a specific format
        Return:
            the format to print
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """
        updates the public instance attribute 'updated_at'
        with the current datetime
        """

        self.updated_at = datetime.now()
        from . import storage
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        my_dict = {}

        my_dict["__class__"] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if type(value) is datetime:
                my_dict[key] = value.isoformat()
            else:
                my_dict[key] = value

        return my_dict
