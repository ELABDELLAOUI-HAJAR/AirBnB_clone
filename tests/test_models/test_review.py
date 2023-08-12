#!/usr/bin/python3
"""This module contains tests for the Review Class"""
from unittest import TestCase, main
from models.base_model import BaseModel
from models.review import Review
from models.place import Place
from models.user import User
import uuid


class TestReview(TestCase):
    """Definition of Test Class of Review"""

    def test_review_inherits_base_model(self):
        """test_place_inherits_base_model"""
        self.assertTrue(issubclass(Review, BaseModel))

    def test_review_with_valid_id(self):
        """test_review_with_valid_id"""
        review = Review()
        self.assertEqual(str(uuid.UUID(review.id)), review.id)

    def test_review_check_attributes(self):
        """test_review_check_attributes"""
        review = Review()
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_set_text(self):
        """test_review_set_text"""
        review = Review()
        review.text = "This is a dump review"
        self.assertEqual(review.text, "This is a dump review")

    def test_review_set_place_id(self):
        """test_review_set_place_id"""
        place = Place()
        review = Review()
        review.place_id = place.id
        self.assertEqual(review.place_id, place.id)

    def test_review_set_user_id(self):
        """test_review_set_user_id"""
        user = User()
        review = Review()
        review.user_id = user.id
        self.assertEqual(review.user_id, user.id)

    def test_review_to_dict(self):
        """test_review_to_dict"""
        review = Review()
        review_dict = {
                "__class__": "Review",
                "id": review.id,
                "created_at": review.created_at.isoformat(),
                "updated_at": review.updated_at.isoformat()
                }
        self.assertDictEqual(review_dict, review.to_dict())

        review_dict["text"] = "Test review"
        review.text = "Test review"
        self.assertDictEqual(review_dict, review.to_dict())


if __name__ == "__main__":
    main()
