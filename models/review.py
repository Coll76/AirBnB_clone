#!/usr/bin/python3
"""
review module defines class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represemts the review
    """
    place_id = ""
    user_id = ""
    text = ""
