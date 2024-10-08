"""
This module defines the API routes for group management.

Routes provided:
- GET /groups: Retrieve a list of all groups.
- GET /groups/{group_id}: Retrieve a specific group by ID.
- POST /groups: Create a new group record.
- PUT /groups/{group_id}: Update an existing group record by ID.
- DELETE /groups/{group_id}: Delete a group record by ID.
"""


from fastapi import APIRouter, Body
from models.groups import Groups
from services.groups_service import GroupsService

groups_route = APIRouter()

@groups_route.get("/")
def get_groups():
    """
    Retrieve a list of all groups.

    Returns:
        List[Groups]: A list of all group records in the database.
    """
    return GroupsService.get_groups()

@groups_route.get("/{group_id}")
def get_group(group_id: int):
    """
    Retrieve a specific group by their ID.

    Args:
        group_id (int): The ID of the group to retrieve.

    Returns:
        Groups: The group record with the specified ID.

    Raises:
        HTTPException: 404 error if the group with the given ID is not found.
    """
    return GroupsService.get_group(group_id)

@groups_route.post("/")
def create_group(group: Groups = Body(...)):
    """
    Create a new group record.

    Args:
        group (Groups): The group data to create.

    Returns:
        Groups: The newly created group record.
    """
    return GroupsService.create_group(group)

@groups_route.put("/{group_id}")
def update_group(group_id: int, group: Groups = Body(...)):
    """
    Update an existing group record by their ID.

    Args:
        group_id (int): The ID of the group to update.

    Returns:
        Groups: The updated group record.

    Raises:
        HTTPException: 404 error if the group with the given ID is not found.
    """
    return GroupsService.update_group(group_id, group)

@groups_route.delete("/{group_id}")
def delete_group(group_id: int):
    """
    Delete a group record by their ID.

    Args:
        group_id (int): The ID of the group to delete.

    Returns:
        dict: A message indicating the result of the delete operation.

    Raises:
        HTTPException: 404 error if the group with the given ID is not found.
    """
    return GroupsService.delete_group(group_id)
