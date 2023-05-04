#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)

        place_amenities = relationship('Place', secondary=place_amenity)

        def __init__(self, obj_dict=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if obj_dict:
                for k, v in obj_dict.items():
                    setattr(self, k, v)
            else:
                return
else:
    class Amenity(BaseModel):
        name = ''
