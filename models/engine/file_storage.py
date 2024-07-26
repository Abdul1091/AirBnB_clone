#!/usr/bin/python3
"""This module defines a class to manage file storage for the AirBnB clone."""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """This class manages storage of AirBnB models in JSON format."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to storage dictionary."""
        key = f"{obj.to_dict()['__class__']}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file."""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file."""
        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }
        
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                try:
                    obj_dict = json.load(f)
                    for key, val in obj_dict.items():
                        class_name = val.pop('__class__', None)
                        if class_name and class_name in classes:
                            cls = classes[class_name]
                            FileStorage.__objects[key] = cls(**val)
                except json.JSONDecodeError:
                    pass  # Handle JSON decoding errors if necessary
