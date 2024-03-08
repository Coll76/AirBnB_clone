#!/usr/bin/python3

import json

"""
class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
"""


class FileStorage:
    """
    Serialization and deserialization
    """
    __file_path = None
    __objects = {}

    """
    returns the dictionary __objects
    """
    def __init__(self):
        FileStorage.__file_path = "file.json"
    def all(self):
        """
        return dictionary __objects
        """
        return FileStorage.__objects
    """
    sets in __objects the obj with key <obj class name>.id
    """
    def new(self, obj):
        """
        creates a hey according to <obj class name>.id
        so necessity to obtain class name using .__class__.__name__
        necessity to obtain obj id using getattr
        creation of key based on specification <obj class name>.id so long obj has an id
        combination of class name and obj id to form a key
        Assigning the object obj to dictionary __objects based on key e have created
        """
        class_name = obj.__class__.__name__
        obj_id = getattr(obj, 'id')

        if obj_id is not None:
            key = f"{class_name}.{obj_id}"
            self.__objects[key] = obj

        """
        serializes __objects to the JSON file (path: __file_path)
        """
    def save(self):
        """
        json.dump is used to write JSON data to a file-like object based on the path self.__path
        serializes __objects to the JSON file (path: __file_path)
        e shall write in JSON file by name file after opening using with open()
        """
        with open(self.__path, 'w') as file:
            json.dump(self.__objects, file)

        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path)
        exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
    def reload(self):
        """
        deserialize JSON file we shall use json.load to read data from JSON file as ell as deserialize it
        Then update the self.__objects to keep it up to date ith the JSON content
        """
        with open(self.__path, 'r') as file:
            self.__objects = json.load(file)
