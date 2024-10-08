"""
This module defines the Pydantic model for a role.

The `Roles` class represents a role and includes attributes such as name and description.
This model is used for data validation and serialization within the application.
"""

from pydantic import BaseModel

class Roles(BaseModel):
    """
    A Pydantic model representing a role.

    Attributes:
        name (str): The name of the role.
        description (str): A description of the role.
    """

    name: str
    description: str
