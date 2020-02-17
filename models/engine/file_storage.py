#!/usr/bin/python3
"""

"""

import json
from models.base_model import BaseModel
import models


class FileStorage:
    """

    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        Method returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """

        """
        new_1 = obj.__class__.__name__
        new_2 = obj.id
        new = new_1 + '.' + new_2
        self.__objects[new] = obj

    def save(self):
        """
        serialization
        """
        dict_add = {}
        with open(self.__file_path, 'w') as f:
            for key, value in self.__objects.items():
                dict_add[key] = value.to_dict()
            json.dump(dict_add, f)

    def reload(self):
        """
        deserialization
        """
        classes = {'BaseModel': BaseModel}
        try:
            with open(self.__file_path, 'r') as f1:
                file_store = json.load(f1)
                for key, value in file_store.items():
                    if '__class__' in value:
                        val = classes[value['__class__']](**value)
                        self.__objects[key] = val
        except:
            pass
