#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

from models.review import Review

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Place(BaseModel, Base):
        """ A place to stay """

        if getenv('HBNB_TYPE_STORAGE') == 'db':
            __tablename__ = 'places'
            city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
            user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
            name = Column(String(128), nullable=False)
            description = Column(String(1024), nullable=True)
            number_rooms = Column(Integer, default=0, nullable=False)
            number_bathrooms = Column(Integer, default=0, nullable=False)
            max_guest = Column(Integer, default=0, nullable=False)
            price_by_night = Column(Integer, default=0, nullable=False)
            latitude = Column(Float, nullable=True)
            longitude = Column(Float, nullable=True)
            amenity_ids = []

            reviews = relationship('Review', backref='place',
                                   cascade='all, delete, delete-orphan')

            amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)

        def __init__(self, obj_dict=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if obj_dict:
                for k, v in obj_dict.items():
                    setattr(self, k, v)
            else:
                return
else:
    class Place(BaseModel):
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = list(str())

        @property
        def reviews(self):
            review_list = []
            for key, value in models.storage.all(Review).items():
                if value.place_id == self.id:
                    review_list.append(value)
            return review_list

        @property
        def amenities(self):
            from models.amenity import Amenity
            amenity_list = []
            for key, value in models.storage.all(Amenity).items():
                if value.place_id == self.id:
                    amenity_list.append(value)
            return amenity_list
