#!/usr/bin/python3
"""
    Module of base_class the mother of all project
"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """ It defines all attributes/metods for other classes """
    def __init__(self, *args, **kwargs):
        """ Initialize BaseModel class """
        if kwargs:
            attr = {x: y for x, y in kwargs.items() if x != '__class__'}
            for key, val in attr.items():
                if key in ["created_at", "updated_at"]:
                    dt_obj = datetime.strptime(val, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, dt_obj)
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ IT implement string output """
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                      self.__dict__))

    def save(self):
        """ It updates [updated_at] with current datetime """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns dictionary of object instance """
        dt = {}
        dt["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if type(val) == datetime:
                dt[key] = val.isoformat()
            else:
                dt[key] = val
        return dt
