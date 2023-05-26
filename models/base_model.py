#!/usr/bin/python3
"""
Class BaseModel
Definitions
"""

<<<<<<< HEAD
import json
=======
>>>>>>> parent of 7366f22... added import JSON
from datetime import datetime
import models
import uuid


class BaseModel:
    """The BaseModel class Derivitives"""

    def __init__(self, *args, **kwargs):
        """ initialized the base model creayted_id and updated_id"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """Representation BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Change time current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        containing all keys/values of the instance"""
        dict_class = self.__dict__.copy()
        if "created_at" in dict_class:
            dict_class["created_at"] = dict_class["created_at"].strftime(time)
        if "updated_at" in dict_class:
            dict_class["updated_at"] = dict_class["updated_at"].strftime(time)
        dict_class["__class__"] = self.__class__.__name__
        return dict_class
