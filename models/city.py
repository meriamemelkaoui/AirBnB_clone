#!/usr/bin/python3
"""the city class"""
from models.base_model import BaseModel

class City(BaseModel):
    """city class."""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.

        Keyword arguments:
        name : string city name
        state_id : string State.id
        """
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
