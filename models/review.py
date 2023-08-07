#!/usr/bin/python3
"""Module that defines the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class
    Attributes:
    place_id: string - empty string: it will be the Place.id
    user_id: string - empty string: it will be the User.id
    text: string - empty string
    """
    place_id = ""
    user_id = ""
    text = ""
