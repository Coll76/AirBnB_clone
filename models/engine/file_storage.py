#!/usr/bin/python3
"""
Now we can recreate a BaseModel from another one by using a dictionary representation
class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City


class FileStorage:
    """
    Private class attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - empty but will store all objects by <class name>.id
        (ex: to store a BaseModel object with id=12121212, the key will be BaseModel.12121212)
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        <obj class name>.id  create this using fstring
        obtain the obj id
        obtain the class name of obj using .__class__.__name___
        """
        obj_id = obj.id
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj_id}"
        self.__objects[key] = obj.to_dict()

    def save(self):
        """
        serialization process using json.dump
        save the objects to JSON file
        """
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(
                    {k: v for k, v in FileStorage.__objects.items()}, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists
        Loads objects from JSON file
        """
        current_classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Amenity': Amenity,
                'City': City,
                'State': State,
                'Place': Place,
                'Review': Review
                }

        with open(FileStorage.__file_path, 'r') as file:
            data = json.load(file)
            for k, v in data.items():
                class_nam, obj_id = k.split(".")
                if class_nam in current_classes:
                    class_obj = current_classes[class_nam]
                    FileStorage.__objects[k] = class_obj(**v)
