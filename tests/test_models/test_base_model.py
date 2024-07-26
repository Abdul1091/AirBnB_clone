#!/usr/bin/python3
"""Unit tests for BaseModel class."""

from models.base_model import BaseModel
import unittest
import datetime
import json
import os


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize test case."""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Setup for tests."""
        pass

    def tearDown(self):
        """Clean up after each test."""
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_default(self):
        """Test default instantiation of BaseModel."""
        instance = self.value()
        self.assertIsInstance(instance, self.value)

    def test_kwargs(self):
        """Test instantiation of BaseModel with dictionary kwargs."""
        instance = self.value()
        copy = instance.to_dict()
        new_instance = BaseModel(**copy)
        self.assertFalse(new_instance is instance)

    def test_kwargs_int(self):
        """Test instantiation of BaseModel with invalid kwargs (int keys)."""
        instance = self.value()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            BaseModel(**copy)

    def test_save(self):
        """Test save method of BaseModel."""
        instance = self.value()
        instance.save()
        key = f"{self.name}.{instance.id}"
        with open('file.json', 'r') as f:
            json_data = json.load(f)
            self.assertEqual(json_data[key], instance.to_dict())

    def test_str(self):
        """Test string representation of BaseModel."""
        instance = self.value()
        expected_str = f"[{self.name}] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_str)

    def test_todict(self):
        """Test to_dict method of BaseModel."""
        instance = self.value()
        dict_representation = instance.to_dict()
        self.assertEqual(instance.to_dict(), dict_representation)

    def test_kwargs_none(self):
        """Test instantiation of BaseModel with None as key."""
        with self.assertRaises(TypeError):
            BaseModel(**{None: None})

    def test_kwargs_one(self):
        """Test instantiation of BaseModel with invalid single key."""
        with self.assertRaises(KeyError):
            BaseModel(**{'Name': 'test'})

    def test_id(self):
        """Test id attribute of BaseModel."""
        instance = self.value()
        self.assertIsInstance(instance.id, str)

    def test_created_at(self):
        """Test created_at attribute of BaseModel."""
        instance = self.value()
        self.assertIsInstance(instance.created_at, datetime.datetime)

    def test_updated_at(self):
        """Test updated_at attribute of BaseModel and ensure it updates."""
        instance = self.value()
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        dict_representation = instance.to_dict()
        new_instance = BaseModel(**dict_representation)
        self.assertFalse(new_instance.created_at == new_instance.updated_at)
