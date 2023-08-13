#!/usr/bin/python3
"""state model."""
from models.base_model import BaseModel
from models.city import City
import models

class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    def __init__(self, *args, **kwargs):
        """Instance Constructor."""
        super().__init__(*args, **kwargs)
        self.name = ""

    # Remove dependency on storage type
    @property
    def cities(self):
        """Getter attribute for cities"""
        if models.storage_type == "file":
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
        return []
