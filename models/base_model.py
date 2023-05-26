#!/usr/bin/python3
"""
This BaseModel class defines the attributes/method of the other classes
in this project
"""

from uuid import uuid4
from datetime import datetime
import models


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
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        This is a python method called when we use print/str.to convert
        object into a string. here it Return the print/str
        representation of the BaseModel instance
        """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

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
        dict_ = dict(self.__dict__)
        dict_.update({"__class__": self.__class__.__name__,
                      "created_at": str(((self.created_at).isoformat())),
                      "updated_at": str(((self.updated_at).isoformat()))})
        return dict_
