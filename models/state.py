#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship

import models
from models.base_model import BaseModel, Column, String, Base
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='states', cascade='all, delete')
    else:
        @property
        def cities(self):
            city_list = []
            for key, value in models.storage.all().items():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list

    def __init__(self, obj_dict=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if obj_dict:
            for k, v in obj_dict.items():
                setattr(self, k, v)
        else:
            return
