"""
This module defines the Pydantic model for a group.

The `Groups` class represents a group and includes attributes such as name and description.
This model is used for data validation and serialization within the application.
"""

from pydantic import BaseModel

class Groups(BaseModel):
    """
    A Pydantic model representing a group.

    Attributes:
        name (str): The name of the group.
        description (str): A description of the group.
    """

    name: str
    description: str
