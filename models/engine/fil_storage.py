#!/usr/bin/python3
import uuid
import json

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    """
    def to_dict(self):
        """"""
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """"""
        instance_dict = {key: getattr(self, key) for key in self.__dict__}
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['id'] = self.id
        return instance_dict
    """

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        #from models.bas_model import to_dict
        obj_id = obj.id
        class_name = obj.__class__.__name__
        obj_class = f"{class_name}.{obj_id}"
        self.__objects[obj_class] = obj.to_dict()
        

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        #json_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        with open(FileStorage.__file_path, 'r') as file:
            FileStorage.__objects = json.load(file)
           #self.__objects = {key: obj for key, obj in json_obj.items()}
