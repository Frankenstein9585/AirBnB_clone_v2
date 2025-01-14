#!/usr/bin/python3
""" Review module for the HBNB project """
from os import getenv

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Review(BaseModel, Base):
        """ Review class to store review information """
        __tablename__ = 'reviews'
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)

        def __init__(self, obj_dict=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if obj_dict:
                for k, v in obj_dict.items():
                    setattr(self, k, v)
            else:
                return
else:
    class Review(BaseModel):
        place_id = ''
        user_id = ''
        text = ''

