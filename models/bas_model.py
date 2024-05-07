#!/usr/bin/env python3
import uuid
from datetime import datetime
import json
from models import storage
"""
class BaseModel that defines all common attributes/methods for other classes
"""


class BaseModel:
    """
    Acts as the base class
    """
    def __init__(self, *args, **kwargs):
        """
        used for initialization
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        object representation
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                        kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                        kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

            if 'id' not in kwargs:
                self.id  = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                #storage.new(self)
                #storage.save()
                storage.new(self)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            #storage.save()
            storage.new(self)
            #storage.save()
    
    def str(self):
        """
        [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        from models import storage
        """
        Updates the updated_at with the current time
        """
        storage.save()
        self.updated_at = datetime.now()
        #storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        a key __class__ must be added to this dictionary with the class name of the object
        created_at and updated_at must be converted to string object in ISO format:
        format: %Y-%m-%dT%H:%M:%S.%f
        """
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict['__class__'] = self.__class__.__name__
        return obj_dict
