#!/usr/bin/env python3
"""
A module for the class user
"""
from models.base_model import BaseModel



class User(BaseModel):
    """
    A class that inherits from BaseModel
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
