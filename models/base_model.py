#!/usr/bin/python3
"""This module defines a class BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


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

        if len(kwargs) != 0:
            frmt = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, frmt)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, frmt)
                else:
                    self.__dict__[key] = value
        models.storage.new(self)

    def __str__(self):
        """Return string representation of BaseModel"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """update the attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns BaseModel dictionary"""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
