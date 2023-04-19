#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, obj_dict=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if obj_dict:
            for k, v in obj_dict.items():
                setattr(self, k, v)
        else:
            return
