#!/usr/bin/python3
"""This module defines a class BaseModel"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class BaseModel defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Initialise BaseModel attributes
        Arguments:
        args: Not used
        kwargs: Dictionary representation of BaseModel instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            elif key == "created_at":
                self.created_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            elif key == "updated_at":
                self.updated_at = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Return string representation of BaseModel"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """update the attribute updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns BaseModel dictionary"""
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return my_dict
