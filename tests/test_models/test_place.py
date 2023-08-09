"""This module contains tests for the Place Class"""
from unittest import TestCase, main
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
import uuid


class TestPlace(TestCase):
    """Definition of Test Class of Place"""

    def test_place_inherits_base_model(self):
        """test_place_inherits_base_model"""
        self.assertTrue(issubclass(Place, BaseModel))

    def test_place_with_valid_id(self):
        """test_place_with_valid_id"""
        place = Place()
        self.assertEqual(str(uuid.UUID(place.id)), place.id)

    def test_place_check_attributes(self):
        """test_place_check_attributes"""
        place = Place()
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_place_set_name(self):
        """test_place_set_name"""
        place = Place()
        place.name = "Hotel de france"
        self.assertEqual(place.name, "Hotel de france")

    def test_place_set_city_id(self):
        """test_place_set_city_id"""
        city = City()
        place = Place()
        place.city_id = city.id
        self.assertEqual(place.city_id, city.id)

    def test_place_set_user_id(self):
        """test_place_set_user_id"""
        user = User()
        place = Place()
        place.user_id = user.id
        self.assertEqual(place.user_id, user.id)

    def test_place_set_description(self):
        """test_place_set_description"""
        place = Place()
        desc = "Hotel de France est le meilleur Hotel au Marrakech"
        place.description = desc
        self.assertEqual(place.description, desc)

    def test_place_set_number_rooms(self):
        """test_place_set_description"""
        place = Place()
        place.number_rooms = 450
        self.assertEqual(place.number_rooms, 450)

    def test_place_set_number_bathrooms(self):
        """test_place_set_bathrooms"""
        place = Place()
        place.number_bathrooms = 650
        self.assertEqual(place.number_bathrooms, 650)

    def test_place_set_max_guest(self):
        """test_place_max_guest"""
        place = Place()
        place.max_guest = 900
        self.assertEqual(place.max_guest, 900)

    def test_place_set_price_by_night(self):
        """test_place_price_by_night"""
        place = Place()
        place.price_by_night = 1000
        self.assertEqual(place.price_by_night, 1000)

    def test_place_set_latitude(self):
        """test_place_latitude"""
        place = Place()
        place.latitude = 145.66
        self.assertEqual(place.latitude, 145.66)
    
    def test_place_set_longitude(self):
        """test_place_longitude"""
        place = Place()
        place.longitude = -45.89
        self.assertEqual(place.longitude, -45.89)

    def test_place_set_longitude(self):
        """test_place_longitude"""
        place = Place()
        amenity_dict = [Amenity().id for i in range(3)]
        place.amenity_ids = amenity_dict
        self.assertEqual(place.amenity_ids, amenity_dict)

    def test_place_to_dict(self):
        """test_place_to_dict"""
        place = Place()
        place_dict = {
                "__class__": "Place",
                "id": place.id,
                "created_at": place.created_at.isoformat(),
                "updated_at": place.updated_at.isoformat()
                }
        self.assertDictEqual(place_dict, place.to_dict())
        place_dict["name"] = "Hotel Farah"
        place.name = "Hotel Farah"
        self.assertDictEqual(place_dict, place.to_dict())
        place_dict["latitude"] = 85.20
        place.latitude = 85.20
        self.assertDictEqual(place_dict, place.to_dict())
        place_dict["max_guest"] = 643
        place.max_guest = 643
        self.assertDictEqual(place_dict, place.to_dict())