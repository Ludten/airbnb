#!/usr/bin/python3
"""
A module defining the base class of the Airbnb console
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
    Class defining the base model

    Attr:
        id (str)
        created_at (datetime)
        updated_at (datetime)
    """

    def __init__(self, *args, **kwargs):
        if (kwargs != {} and len(kwargs) > 0):
            for i, j in kwargs.items():
                if i != '__class__':
                    if i == 'created_at' or i == 'updated_at':
                        k = datetime.fromisoformat(j)
                        setattr(self, i, k)
                    else:
                        setattr(self, i, j)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return "[{:s}] ({:s}) {:s}".format(
            self.__class__.__name__, self.id, str(self.__dict__))

    def save(self):
        """
        Updates the updated_at attributes after changes have been made
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """
        Returns the dictionary representation of the class

        Returns:
            dict
        """
        basedict = self.__dict__.copy()
        basedict['__class__'] = self.__class__.__name__
        basedict['created_at'] = self.created_at.isoformat()
        basedict['updated_at'] = self.updated_at.isoformat()
        return basedict
