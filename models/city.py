#!/usr/bin/python3
""" Defines city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ It shors that city class is inheriting BaseModel """
    state_id = ""
    name = ""
