#!/usr/bin/python3
"""This module contains tests for the User Class"""
from unittest import TestCase, main
from models.base_model import BaseModel
from models.user import User
import uuid


class TestUser(TestCase):
    """Definition of Test Class of User"""

    def test_user_inherits_base_model(self):
        """test user inherits base model"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_with_valid_id(self):
        """test user with valid id"""
        user = User()
        self.assertEqual(str(uuid.UUID(user.id)), user.id)

    def test_user_check_attributes(self):
        """test user check attributes"""
        user = User()
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_user_set_first_name(self):
        """test user set first name"""
        user = User()
        user.first_name = "Yassine"
        self.assertEqual(user.first_name, "Yassine")

    def test_user_set_last_name(self):
        """test user set last name"""
        user = User()
        user.last_name = "Ait Mensour"
        self.assertEqual(user.last_name, "Ait Mensour")

    def test_user_set_email(self):
        """test user set email"""
        user = User()
        user.email = "Yassine@alx.com"
        self.assertEqual(user.email, "Yassine@alx.com")

    def test_user_set_password(self):
        """test user set password"""
        user = User()
        user.password = "Yassine@1990*$"
        self.assertEqual(user.password, "Yassine@1990*$")

    def test_user_to_dict(self):
        """test user to dict"""
        user = User()
        user_dict = {
                "__class__": "User",
                "id": user.id,
                "created_at": user.created_at.isoformat(),
                "updated_at": user.updated_at.isoformat()
                }
        self.assertDictEqual(user_dict, user.to_dict())
        user_dict["first_name"] = "Yassine"
        user.first_name = "Yassine"
        self.assertDictEqual(user_dict, user.to_dict())
        user_dict["last_name"] = "Ait Mensour"
        user.last_name = "Ait Mensour"
        self.assertDictEqual(user_dict, user.to_dict())


if __name__ == "__main__":
    main()
