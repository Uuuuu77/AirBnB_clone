#!/usr/bin/python3
"""
    models/user.py module of user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ It show that user class inherits BaseModel & creates new users """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
