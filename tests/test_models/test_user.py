#!/usr/bin/python3
"""
Unit tests for the User class in the models.user module.
"""

from tests.test_models.test_base_model import TestBaseModel
from models.user import User


class TestUser(TestBaseModel):
    """Tests for the User class."""

    def __init__(self, *args, **kwargs):
        """
        Initializes the test case for the User class.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Test that the first_name attribute of the User class is of type str.
        """
        new_user = self.value()
        self.assertEqual(
            type(new_user.first_name), str
        )

    def test_last_name(self):
        """
        Test that the last_name attribute of the User class is of type str.
        """
        new_user = self.value()
        self.assertEqual(
            type(new_user.last_name), str
        )

    def test_email(self):
        """
        Test that the email attribute of the User class is of type str.
        """
        new_user = self.value()
        self.assertEqual(
            type(new_user.email), str
        )

    def test_password(self):
        """
        Test that the password attribute of the User class is of type str.
        """
        new_user = self.value()
        self.assertEqual(
            type(new_user.password), str
        )
