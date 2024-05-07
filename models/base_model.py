#!/usr/bin/python3
"""
models/base_model.py

This module defines the BaseModel class that serves as the base class
from which other classes inherit. It provides a UUID for each instance
and includes common attributes and methods.
"""

import uuid
import cmd
from datetime import datetime, timedelta, timezone
import json
import models


class BaseModel:
    """
    class BaseModel serves as the base class from
    which other classes inherit.
    It provides a UUID for each instance created.

    Parameters:
        my_number: A class attribute with a default value of 8
        name: A class attribute with a default value of "Model"
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Parameters:
            id: string assign with an uuid when an instance is created
                you can use uuid.uuid4() to generate unique id
                but don’t forget to convert to a string
                the goal is to have unique id for each BaseModel
                created_at: datetime - assign with the current
                datetime when an instance is created
                updated_at: datetime - assign with the current
                datetime when an instance is created
                and it will be updated every time you change your object
        """
        if kwargs:
            for key, value in kwargs.items():
                # Exclude '__class__'
                if key == '__class__':
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

            """
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        )
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'
                        )
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                models.storage.new(self)
                #storage.save()
            """

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        informal string representation of object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        update updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        #storage.new(self)
        models.storage.save()
        

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        instance_dict = {key: getattr(self, key) for key in self.__dict__}
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['id'] = self.id
        return instance_dict
