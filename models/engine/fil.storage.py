#!/usr/bin/env python3
import uuid
import json

class FileStorage:
    __file_path = 'f.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        obj_id = obj.id
        class_name = obj.__class__.__name__
        obj_class = f"{obj_id}.{class_name}"
        return obj_class

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        with open(self.__path, 'r') as file:
            self.__objects = json.load(file)
