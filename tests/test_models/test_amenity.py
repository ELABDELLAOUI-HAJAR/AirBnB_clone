"""This module contains tests for the Amenity Class"""
from unittest import TestCase, main
from models.base_model import BaseModel
from models.amenity import Amenity
import uuid


class TestAmenity(TestCase):
    """Definition of Test Class of Amenity"""

    def test_amenity_inherits_base_model(self):
        """test_amenity_inherits_base_model"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_with_valid_id(self):
        """test_amenity_with_valid_id"""
        amenity = Amenity()
        self.assertEqual(str(uuid.UUID(amenity.id)), amenity.id)

    def test_amenity_check_attributes(self):
        """test_amenity_check_attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_set_name(self):
        """test_amenity_set_name"""
        amenity = Amenity()
        amenity.name = "Towel"
        self.assertEqual(amenity.name, "Towel")

    def test_amenity_to_dict(self):
        """test_amenity_to_dict"""
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


if __name__ == "__main__":
    main()
