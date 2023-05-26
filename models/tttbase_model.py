#!/usr/bin/python3
"""
This BaseModel class defines the attributes/method of the other classes
in this project
"""

from datetime import datetime
import models
import uuid
import json
isoform_time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    This BaseModel defines the base class from which other classes
        will inherit the following  atributes:
        id -> Public instance attributes
        created_at -> Public instance attributes
        updated_at -> Public instance attributes
    """

    def __init__(self, *args, **kwargs):
        """
        This Initializes the following object/instance attributes
            id: contains the object's identification
            created_at: the datetime in which the object was created
            updated_at: the datetime in which the object was modified
        """
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
        """
        This is a python method called when we use print/str.to convert
        object into a string. here it Return the print/str
        representation of the BaseModel instance
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """
        This Public instance methods, updates the public instance
        attribute(updated_at) with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        This public instance methods updates and returns a returns a
        dictionary containing all keys/values of __dict__ of the
        instance with self.__dict__ we are making a copy. This
        method will be the first piece of the serialization/
        deserialization prcess which creates a dictionary
        representation with a "simple object type” of our BaseModel
        """
        dict_class = self.__dict__.copy()
        if "created_at" in dict_class:
            dict_class["created_at"] = dict_class["created_at"].strftime(time)
        if "updated_at" in dict_class:
            dict_class["updated_at"] = dict_class["updated_at"].strftime(time)
        dict_class["__class__"] = self.__class__.__name__
        return dict_class
