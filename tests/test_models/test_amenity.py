#!/usr/bin/python3
"""
Unit tests for the Amenity class in the models.amenity module.
"""

from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class TestAmenity(TestBaseModel):
    """Tests for the Amenity class."""

    def __init__(self, *args, **kwargs):
        """
        Initializes the test case for the Amenity class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_type(self):
        """
        Test that the name attribute of the Amenity class is of type str.
        """
        new_amenity = self.value()
        self.assertEqual(type(new_amenity.name), str)
