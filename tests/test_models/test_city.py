#!/usr/bin/python3
"""This module contains tests for the City Class"""
from unittest import TestCase, main
from models.base_model import BaseModel
from models.city import City
from models.state import State
import uuid


class TestCity(TestCase):
    """Definition of Test Class of City"""

    def test_city_inherits_base_model(self):
        """test city inherits base model"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_with_valid_id(self):
        """test city with valid id"""
        city = City()
        self.assertEqual(str(uuid.UUID(city.id)), city.id)

    def test_city_check_attributes(self):
        """test city check attributes"""
        city = City()
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_city_set_name(self):
        """test city set name"""
        city = City()
        city.name = "Marrakech"
        self.assertEqual(city.name, "Marrakech")

    def test_city_set_state_id(self):
        """test city set name"""
        city = City()
        state = State()
        city.state_id = state.id
        self.assertEqual(city.state_id, state.id)

    def test_city_to_dict(self):
        """test city to dict"""
        city = City()
        city_dict = {
                "__class__": "City",
                "id": city.id,
                "created_at": city.created_at.isoformat(),
                "updated_at": city.updated_at.isoformat()
                }
        self.assertDictEqual(city_dict, city.to_dict())
        city_dict["name"] = "Marrakech"
        city.name = "Marrakech"
        self.assertDictEqual(city_dict, city.to_dict())


if __name__ == "__main__":
    main()
