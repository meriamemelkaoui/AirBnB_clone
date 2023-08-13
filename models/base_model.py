#!/usr/bin/python3
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                setattr(self, "id", str(uuid.uuid4()))
            time = datetime.now()
            if "created_at" not in kwargs.keys():
                setattr(self, "created_at", time)
            if "updated_at" not in kwargs.keys():
                setattr(self, "updated_at", time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        dic = self.to_dict()
        # del dic['__class__']
        # dic['created_at'] = datetime.strptime(dic['created_at'],
        #                                       "%Y-%m-%dT%H:%M:%S")
        # dic['updated_at'] = datetime.strptime(dic['updated_at'],
        #                                       "%Y-%m-%dT%H:%M:%S")
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, dic)
    def __str__(self):
        """returns a string
        Return:
            returns a string of class name, id, and dictionary
        """
        dic = self.to_dict()
        # del dic['__class__']
        # dic['created_at'] = datetime.strptime(dic['created_at'],
        #                                       "%Y-%m-%dT%H:%M:%S")
        # dic['updated_at'] = datetime.strptime(dic['updated_at'],
        #                                       "%Y-%m-%dT%H:%M:%S")
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, dic)
    def __repr__(self):
        """return a string representaion
        """
        return self.__str__()

    def save(self):
        """updates the public instance attribute updated_at to current
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
    def to_dict(self):
        """creates dictionary of the class  and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        if '_sa_instance_state' in my_dict.keys():
            my_dict.pop('_sa_instance_state', None)
        return my_dict
