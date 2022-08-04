#!/usr/bin/python3
"""
A mdoule for serialization and deserialization of JSON files
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    A class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns objects

        Returns:
            dict
        """
        return self.__objects

    def new(self, obj):
        """
        sets an object id in the objects dictionary
        """
        kid = '{:s}.{:s}'.format(obj.__class__.__name__, obj.id)
        self.__objects[kid] = obj

    def save(self):
        """
        Serializes objects to the JSON file
        """
        print(self.__objects)
        objdict = {k: v.to_dict() for k, v in self.__objects.items()}
        print(objdict)
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(objdict))

    def reload(self):
        """
        deserializes the JSON file to objects
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                s_json = f.read()
                if s_json != "" and s_json is not None:
                    newobject = json.loads(s_json)
                    for k, v in newobject.items():
                        if 'BaseModel' in k:
                            newcls = BaseModel(**v)
                    self.__objects.update(newcls)
        except Exception:
            pass
