#!/usr/bin/python3
"""
user module defines class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    inherits from BaseModel
    Contains user credentials
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
