#!/usr/bin/python3
from models.base_model import BaseModel

class Amenity(BaseModel):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    def __init__(self, *args, **kwargs):
        """Instance Constructor."""
        super().__init__(*args, **kwargs)
        self.name = ""
