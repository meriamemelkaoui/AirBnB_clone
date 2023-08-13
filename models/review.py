#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: string - empty string: it will be the Place.id
        user_id: string - empty string: it will be the User.id
        text: string - empty string
    """
    def __init__(self, *args, **kwargs):
        """Instance Constructor."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
