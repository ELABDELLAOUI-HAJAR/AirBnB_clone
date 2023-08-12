"""This module contains tests for the State Class"""
from unittest import TestCase, main
from models.base_model import BaseModel
from models.state import State
import uuid


class TestState(TestCase):
    """Definition of Test Class of State"""

    def test_state_inherits_base_model(self):
        """test_state_inherits_base_model"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_with_valid_id(self):
        """test_state_with_valid_id"""
        state = State()
        self.assertEqual(str(uuid.UUID(state.id)), state.id)

    def test_state_check_attributes(self):
        """test_state_check_attributes"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))

    def test_state_set_name(self):
        """test_state_set_name"""
        state = State()
        state.name = "Marrakech-Safi"
        self.assertEqual(state.name, "Marrakech-Safi")

    def test_state_to_dict(self):
        """test_state_to_dict"""
        state = State()
        state_dict = {
                "__class__": "State",
                "id": state.id,
                "created_at": state.created_at.isoformat(),
                "updated_at": state.updated_at.isoformat()
                }
        self.assertDictEqual(state_dict, state.to_dict())
        state_dict["name"] = "Marrakech-Safi"
        state.name = "Marrakech-Safi"
        self.assertDictEqual(state_dict, state.to_dict())


if __name__ == "__main__":
    main()
