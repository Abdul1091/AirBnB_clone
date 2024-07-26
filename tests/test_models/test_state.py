#!/usr/bin/python3
"""
Unit tests for the State class in the models.state module.
"""

from tests.test_models.test_base_model import TestBaseModel
from models.state import State


class TestState(TestBaseModel):
    """Tests for the State class."""

    def __init__(self, *args, **kwargs):
        """
        Initializes the test case for the State class.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name_type(self):
        """
        Test that the name attribute of the State class is of type str.
        """
        new_state = self.value()
        self.assertEqual(type(new_state.name), str)
