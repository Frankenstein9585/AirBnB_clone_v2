#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', backref='user',
                          cascade='all, delete, delete-orphan')
    reviews = relationship('Review', backref='user',
                           cascade='all, delete, delete-orphan')

    def __init__(self, obj_dict=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if obj_dict:
            for k, v in obj_dict.items():
                setattr(self, k, v)
        else:
            return
