#!/usr/bin/python3
"""
Unit tests for the City class in the models.city module.
"""

from tests.test_models.test_base_model import TestBaseModel
from models.city import City


class TestCity(TestBaseModel):
    """Tests for the City class."""

    def __init__(self, *args, **kwargs):
        """
        Initializes the test case for the City class.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id_type(self):
        """
        Test that the state_id attribute of the City class is of type str.
        """
        new_city = self.value()
        self.assertEqual(type(new_city.state_id), str)

    def test_name_type(self):
        """
        Test that the name attribute of the City class is of type str.
        """
        new_city = self.value()
        self.assertEqual(type(new_city.name), str)
