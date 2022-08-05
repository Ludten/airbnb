#!/usr/bin/python3
"""
A module defining the user class of the Airbnb console
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Class defining the User model

    Attr:
        id (str)
        created_at (datetime)
        updated_at (datetime)
        email (str)
        password (str)
        first_name (str)
        last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
