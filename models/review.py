#!/usr/bin/python3
""" It defines review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Customer's review class inheriting BaseModel """
    place_id = ""
    user_id = ""
    text = ""
