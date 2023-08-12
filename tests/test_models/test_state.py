#!/usr/bin/python3
"""This module contains tests for the State Class"""
from unittest import TestCase, main
from models.base_model import BaseModel
from models.state import State
import uuid


class TestState(TestCase):
    """Definition of Test Class of State"""

    def test_state_inherits_base_model(self):
        """test state inherits base model"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_with_valid_id(self):
        """test state with valid id"""
        state = State()
        self.assertEqual(str(uuid.UUID(state.id)), state.id)

    def test_state_check_attributes(self):
        """test state check attributes"""
        state = State()
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))
        self.assertTrue(hasattr(state, "name"))

    def test_state_set_name(self):
        """test state set name"""
        state = State()
        state.name = "Marrakech-Safi"
        self.assertEqual(state.name, "Marrakech-Safi")

    def test_state_to_dict(self):
        """test state to dict"""
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

    def test_state_initialise_with_kwargs(self):
        """test initialise state with kwargs"""
        s_dict = {
                "id": str(uuid.uuid4()),
                "name": "SALE"
                }
        state = State(**s_dict)
        self.assertEqual(s_dict["id"], state.id)
        self.assertEqual(state.name, "SALE")
        
    def test_state_initialise_with_args(self):
        """test initialise state by using args"""
        state = State("xxxxxxxxxxxxxxxxxxx")
        self.assertNotIn("xxxxxxxxxxxxxxxxxxx", state.__dict__.values())
        
    def test_state_str_representation(self):
        """test state str representation"""
        state = State()
        s_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(state.__str__(), s_str)
        
    def test_state_initialise_with_empty_kwargs(self):
        """test initialise state with empty kwargs"""
        s_dict = {}
        state = State(**s_dict)
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    main()
