#!/usr/bin/python3
"""
Unit tests for the Place class in the models.place module.
"""

from tests.test_models.test_base_model import TestBaseModel
from models.place import Place


class TestPlace(TestBaseModel):
    """Tests for the Place class."""

    def __init__(self, *args, **kwargs):
        """
        Initializes the test case for the Place class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Test that the city_id attribute of the Place class is of type str.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.city_id), str
        )

    def test_user_id(self):
        """
        Test that the user_id attribute of the Place class is of type str.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.user_id), str
        )

    def test_name(self):
        """
        Test that the name attribute of the Place class is of type str.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.name), str
        )

    def test_description(self):
        """
        Test that the description attribute of the Place class is of type str.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.description), str
        )

    def test_number_rooms(self):
        """
        Test that the number_rooms attribute of the Place class is of type int.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.number_rooms), int
        )

    def test_number_bathrooms(self):
        """
        Test that number_bathrooms attribute of Place class is of type int.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.number_bathrooms), int
        )

    def test_max_guest(self):
        """
        Test that the max_guest attribute of the Place class is of type int.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.max_guest), int
        )

    def test_price_by_night(self):
        """
        Test that price_by_night attribute of Place class is of type int.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.price_by_night), int
        )

    def test_latitude(self):
        """
        Test that the latitude attribute of the Place class is of type float.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.latitude), float
        )

    def test_longitude(self):
        """
        Test that the longitude attribute of the Place class is of type float.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.longitude), float
        )

    def test_amenity_ids(self):
        """
        Test that the amenity_ids attribute of the Place class is of type list.
        """
        new_place = self.value()
        self.assertEqual(
            type(new_place.amenity_ids), list
        )
