#!/usr/bin/python3
""" A module for serialization/deserialization """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """ serializes instances to a JSON file and deserializes
    JSON file to instances"""

    __file_path = "HA_YA_FILE.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file """
        objs_dict = {k: self.__objects[k].to_dict()
                     for k in self.__objects.keys()}

        with open(self.__file_path, "w") as f:
            json.dump(objs_dict, f)

    def reload(self):
        """ eserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as f:
                dicts = json.load(f)
                for dict in dicts.values():
                    className = dict["__class__"]
                    del dict["__class__"]
                    self.new(eval(className)(**dict))
        except FileNotFoundError:
            pass
