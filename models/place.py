#!/usr/bin/env python3
"""
This is a modue for the Place class
"""
from base_model import BaseModel


class Place(BaseModel):
    """
    contains empty class attributes
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_per_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""
