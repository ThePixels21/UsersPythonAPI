"""
This module provides a service class for managing group-related operations,
including retrieving, creating, updating, and deleting group records from the database.
"""

from peewee import DoesNotExist, IntegrityError
from fastapi import Body, HTTPException
from models.groups import Groups
from config.database import GroupsModel


class GroupsService:
    """
    Service class for handling business logic related to groups.

    This class provides methods to manage group records, including operations
    such as creating, updating, retrieving, and deleting group information
    from the database.

    Methods:
        get_groups()
            Retrieve a list of all groups.

        get_group(group_id: int)
            Retrieve a specific group by its ID.

        create_group(group: Groups)
            Create a new group record.

        update_group(group_id: int, group_data: Dict[str, str])
            Update an existing group record by its ID.

        delete_group(group_id: int)
            Delete a group record by its ID.
    """

    @staticmethod
    def get_groups():
        """
        Retrieve a list of all groups.

        Returns:
            List[Groups]: A list of all group records in the database.
        """
        groups = list(GroupsModel.select())
        return groups

    @staticmethod
    def get_group(group_id: int):
        """
        Retrieve a specific group by its ID.

        Args:
            group_id (int): The ID of the group to retrieve.

        Returns:
            Groups: The group record with the specified ID.

        Raises:
            HTTPException: 404 error if the group with the given ID is not found.
        """
        try:
            group = GroupsModel.get(GroupsModel.id == group_id)
            return group
        except DoesNotExist as exc:
            raise HTTPException(
                status_code=404,
                detail="Group not found"
            ) from exc

    @staticmethod
    def create_group(group: Groups = Body(...)):
        """
        Create a new group record.

        Args:
            group (Groups): The group data to create.

        Returns:
            Groups: The newly created group record.
        """
        try:
            created_group = GroupsModel.create(
                name=group.name,
                description=group.description
            )
            return created_group
        except IntegrityError as exc:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while creating the group"
            ) from exc

    @staticmethod
    def update_group(group_id: int, group: Groups = Body(...)):
        """
        Update an existing group record by its ID.

        Args:
            group_id (int): The ID of the group to update.

        Returns:
            Groups: The updated group record.

        Raises:
            HTTPException: 404 error if the group with the given ID is not found.
        """
        try:
            u_group = GroupsModel.get(GroupsModel.id == group_id)
            u_group.name = group.name
            u_group.description = group.description
            u_group.save()
            return u_group
        except DoesNotExist as exc:
            raise HTTPException(
                status_code=404,
                detail="Group not found"
            ) from exc

    @staticmethod
    def delete_group(group_id: int):
        """
        Delete a group record by its ID.

        Args:
            group_id (int): The ID of the group to delete.

        Returns:
            dict: A message indicating the result of the delete operation.

        Raises:
            HTTPException: 404 error if the group with the given ID is not found.
        """
        try:
            GroupsModel.delete().where(GroupsModel.id == group_id).execute()
            return {"status": "Group deleted"}
        except DoesNotExist as exc:
            raise HTTPException(
                status_code=404,
                detail="Group not found"
            ) from exc
