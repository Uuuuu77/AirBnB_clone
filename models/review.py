#!/usr/bin/env python3
"""
A module for my Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    this is my review class
    """
    place_id = ""
    user_id = ""
    text = ""
