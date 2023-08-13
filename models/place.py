#!/usr/bin/python3
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.review import Review
import models

class Place(BaseModel):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night: price for a staying in int
        latitude: latitude in float
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    def __init__(self, *args, **kwargs):
        """Instance Constructor."""
        super().__init__(*args, **kwargs)
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []

    # Remove dependency on storage type
    @property
    def reviews(self):
        """Getter attribute for reviews"""
        if models.storage_type == "file":
            return [review for review in models.storage.all(Review)
                    if review.place_id == self.id]
        return []

    @property
    def amenities(self):
        """Getter attribute for amenities"""
        if models.storage_type == "file":
            return [amenity for amenity in models.storage.all(Amenity)
                    if amenity.id in self.amenity_ids]
        return []

    @amenities.setter
    def amenities(self, obj):
        """Setter method for amenities"""
        if models.storage_type == "file" and isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
