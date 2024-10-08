"""
This module defines the Pydantic model for the relationship between users and groups.

The `UserGroups` class represents the association of a user with a group and includes
the attributes `user_id` and `group_id`. This model is used for data validation
and serialization within the application.
"""

from pydantic import BaseModel

class UserGroups(BaseModel):
    """
    A Pydantic model representing the association between a user and a group.

    Attributes:
        user_id (int): The ID of the user.
        group_id (int): The ID of the group.
    """

    user_id: int
    group_id: int
