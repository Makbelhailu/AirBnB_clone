#!usr/bin/python3
"""BaseModel"""

import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage as storage


class BaseModel():
    """BaseModel class defines common attr/mtds for other classes"""

    def __init__(self, *args, **kwargs):
        """Constructor  - initializes BaseModel instance"""
        if kwargs and kwargs is not None:
            for i in kwargs:
                if i == "created_at":
                    mode = '%Y-%m-%dT%H:%M:%S.%f'
                    date = datetime.strptime(kwargs["created_at"], mode)
                    self.__dict__["created_at"] = date
                elif k == "updated_at":
                    mode = '%Y-%m-%dT%H:%M:%S.%f'
                    date = datetime.strptime(kwargs["updated_at"], mode)
                    self.__dict__["updated_at"] = date
                else:
                    self.__dict__[k] = kwargs[k]

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Prints a string representation of class"""
        name, ids, dic = type(self).__name__, self.id, self.__dict__
        return "[{}] ({}) {}".format(name, ids, dic)

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dict of all keys/vals of __dict__"""
        dict = self.__dict__.copy()
        dict["__class__"] = type(self).__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dict
