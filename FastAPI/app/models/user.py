"""
This module defines the Pydantic model for a user.

The `User` class represents a user and includes attributes
such as name, email, password, profile_photo, account_type, and role_id.
This model is used for data validation and serialization within the application.
"""

from pydantic import BaseModel

class User(BaseModel):
    """
    A Pydantic model representing a user.

    Attributes:
        name (str): The name of the user.
        email (str): The email address of the user.
        password (str): The user's password.
        profile_photo (str): The URL or path to the user's profile photo.
        account_type (str): The type of account (e.g., admin, regular user).
        role_id (int): The role ID associated with the user.
    """

    name: str
    email: str
    password: str
    profile_photo: str
    account_type: str
    role_id: int
