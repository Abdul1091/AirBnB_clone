#!/usr/bin/python3
"""Module for the review functionality in the HolbertonBnB project"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class to manage review details"""
    place_id = ""
    user_id = ""
    text = ""
