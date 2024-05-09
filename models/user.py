#!/usr/bin/python3
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
