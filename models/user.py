#!/usr/bin/python3
"""This module defines the User class, which inherits from BaseModel."""

from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''
