#!/usr/bin/python3
"""
Module for task_01_pickle
"""


class CustomObject:
    """
    A class to represent a custom object
    """

    def __init__(self, name, age, is_student):
        """
        Initializes the object with a name
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Displays the object's attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes an object to a text file, using a JSON representation
        """
        import json
        try:
            with open(filename, 'w') as file:
                json.dump({
                    'name': self.name,
                    'age': self.age,
                    'is_student': self.is_student
                }, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes a JSON representation from a text file
        """
        import json
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            obj = cls(data['name'], data['age'], data['is_student'])
            return obj
        except Exception:
            return None
