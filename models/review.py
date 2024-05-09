#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represemts the review
    """
    def __init__(self):
        """
        For initialization
        """
        place_id = ""
        user_id = ""
        text = ""
