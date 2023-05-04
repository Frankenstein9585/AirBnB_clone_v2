#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Column, String, Base
from os import getenv, environ

from models.city import City

s = 'HBNB_TYPE_STORAGE'
if s in environ.keys() and environ[s] == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')

        def __init__(self, obj_dict=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if obj_dict:
                for k, v in obj_dict.items():
                    setattr(self, k, v)
            else:
                return
else:
    class State(BaseModel):
        name = ''

        @property
        def cities(self):
            city_list = []
            for key, value in models.storage.all(City).items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list



