#!/usr/bin/python3
"""
Package initializer for the models package.

This file sets up the appropriate storage engine based on the environment
variable `HBNB_TYPE_STORAGE`. It imports necessary modules and classes and
initializes the storage engine for the package.
"""

from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

# Determine which storage engine to use based on the environment variable
if getenv("HBNB_TYPE_STORAGE", "fs") == "db":
    from models.engine import db_storage
    storage = db_storage.DBStorage()
else:
    from models.engine import file_storage
    storage = file_storage.FileStorage()

# Map class names to their corresponding class objects
classes = {
    "User": User, 
    "BaseModel": BaseModel,
    "Place": Place, 
    "State": State,
    "City": City, 
    "Amenity": Amenity,
    "Review": Review
}

# Reload storage to ensure it is properly initialized
storage.reload()
