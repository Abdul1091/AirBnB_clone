#!/usr/bin/python3
"""
Unit tests for the Review class in the models.review module.
"""

from tests.test_models.test_base_model import TestBaseModel
from models.review import Review


class TestReview(TestBaseModel):
    """Tests for the Review class."""

    def __init__(self, *args, **kwargs):
        """
        Initializes the test case for the Review class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test that the place_id attribute of the Review class is of type str.
        """
        new_review = self.value()
        self.assertEqual(
            type(new_review.place_id), str
        )

    def test_user_id(self):
        """
        Test that the user_id attribute of the Review class is of type str.
        """
        new_review = self.value()
        self.assertEqual(
            type(new_review.user_id), str
        )

    def test_text(self):
        """
        Test that the text attribute of the Review class is of type str.
        """
        new_review = self.value()
        self.assertEqual(
            type(new_review.text), str
        )
