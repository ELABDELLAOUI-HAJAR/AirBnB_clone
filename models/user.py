#!/usr/bin/python3
"""Module that define the User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Definition of the User Class

    Attributes:
        email: User mail
        password: User account password
        first_name: User first name
        last_name: User last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
