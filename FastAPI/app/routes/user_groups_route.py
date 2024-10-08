"""
This module defines the API routes for user group management.

Routes provided:
- GET /user_groups: Retrieve a list of all user groups.
- GET /user_groups/{user_group_id}: Retrieve a specific user group by ID.
- POST /user_groups: Create a new user group record.
- PUT /user_groups/{user_group_id}: Update an existing user group record by ID.
- DELETE /user_groups/{user_group_id}: Delete a user group record by ID.
"""

from fastapi import APIRouter, Body
from models.user_groups import UserGroups
from services.user_groups_service import UserGroupsService

user_groups_route = APIRouter()

@user_groups_route.get("/")
def get_user_groups():
    """
    Retrieve a list of all user groups.

    Returns:
        List[UserGroups]: A list of all user group records in the database.
    """
    return UserGroupsService.get_user_groups()

@user_groups_route.get("/{user_group_id}")
def get_user_group(user_group_id: int):
    """
    Retrieve a specific user group by their ID.

    Args:
        user_group_id (int): The ID of the user group to retrieve.

    Returns:
        UserGroups: The user group record with the specified ID.

    Raises:
        HTTPException: 404 error if the user group with the given ID is not found.
    """
    return UserGroupsService.get_user_group(user_group_id)

@user_groups_route.post("/")
def create_user_group(user_group: UserGroups = Body(...)):
    """
    Create a new user group record.

    Args:
        user_group (UserGroups): The user group data to create.

    Returns:
        UserGroups: The newly created user group record.
    """
    return UserGroupsService.create_user_group(user_group)

@user_groups_route.put("/{user_group_id}")
def update_user_group(user_group_id:int,user_group: UserGroups = Body(...)):
    """
        Update a user group by its ID with new user and group information

    Args:
        user_group_id (int): The ID of the user group to update.
        user_group (UserGroups, optional): A body parameter containing the new user and group.

    Returns:
        UserGroupsModel: The updated user group object handled by the UserGroupsService.
    """
    return UserGroupsService.update_user_group(user_group_id,user_group)


@user_groups_route.delete("/{user_group_id}")
def delete_user_group(user_group_id: int):
    """
    Delete a user group record by their ID.

    Args:
        user_group_id (int): The ID of the user group to delete.

    Returns:
        dict: A message indicating the result of the delete operation.

    Raises:
        HTTPException: 404 error if the user group with the given ID is not found.
    """
    return UserGroupsService.delete_user_group(user_group_id)
