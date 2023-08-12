#!/usr/bin/python3
"""This module contains tests for the Amenity Class"""
from unittest import TestCase, main
from models.base_model import BaseModel
from models.amenity import Amenity
import uuid


class TestAmenity(TestCase):
    """Definition of Test Class of Amenity"""

    def test_amenity_inherits_base_model(self):
        """test amenity inherits base model"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_with_valid_id(self):
        """test amenity with valid id"""
        amenity = Amenity()
        self.assertEqual(str(uuid.UUID(amenity.id)), amenity.id)

    def test_amenity_check_attributes(self):
        """test amenity check attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_set_name(self):
        """test amenity set name"""
        amenity = Amenity()
        amenity.name = "Towel"
        self.assertEqual(amenity.name, "Towel")

    def test_amenity_to_dict(self):
        """test amenity to dict"""
        amenity = Amenity()
        amenity_dict = {
                "__class__": "Amenity",
                "id": amenity.id,
                "created_at": amenity.created_at.isoformat(),
                "updated_at": amenity.updated_at.isoformat()
                }
        self.assertDictEqual(amenity_dict, amenity.to_dict())
        amenity_dict["name"] = "Towel"
        amenity.name = "Towel"
        self.assertDictEqual(amenity_dict, amenity.to_dict())

    def test_amenity_initialise_with_kwargs(self):
        """test initialise amenity with kwargs"""
        a_dict = {
                "id": str(uuid.uuid4()),
                "name": "Towel"
                }
        amenity = Amenity(**a_dict)
        self.assertEqual(a_dict["id"], amenity.id)
        self.assertEqual(amenity.name, "Towel")

    def test_amenity_initialise_with_args(self):
        """test initialise amenity by using args"""
        amenity = Amenity("xxxxxxxxxxxxxxxxxxx")
        self.assertNotIn("xxxxxxxxxxxxxxxxxxx", amenity.__dict__.values())

    def test_amenity_str_representation(self):
        """test amenity str representation"""
        amenity = Amenity()
        a_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(amenity.__str__(), a_str)

    def test_amenity_initialise_with_empty_kwargs(self):
        """test initialise amenity with empty kwargs"""
        a_dict = {}
        amenity = Amenity(**a_dict)
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    main()
