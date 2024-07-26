#!/usr/bin/python3
""" Module defining the City class for the HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ Represents a city with a state ID and name """
    state_id = ""
    name = ""
