#!/usr/bin/python3
"""Module that defines the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class
    Attributes:
    name: The name of the city
    state_id: The id of the state the city belongs to
    """
    name = ""
    state_id = ""
