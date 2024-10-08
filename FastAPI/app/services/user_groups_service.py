"""
This module provides a service class for managing user-group-related operations,
including retrieving, creating, updating, and deleting user-group association records.
"""

from peewee import DoesNotExist, IntegrityError
from fastapi import Body, HTTPException
from models.user_groups import UserGroups
from database import UserGroupsModel


class UserGroupsService:
    """
    Service class for handling business logic related to user-group associations.

    This class provides methods to manage user-group records, including operations
    such as creating, updating, retrieving, and deleting user-group association information
    from the database.

    Methods:
        get_user_groups()
            Retrieve a list of all user-group associations.

        get_user_group(user_id: int, group_id: int)
            Retrieve a specific user-group association by user and group IDs.

        create_user_group(user_group: UserGroups)
            Create a new user-group association.

        delete_user_group(user_id: int, group_id: int)
            Delete a user-group association by user and group IDs.
    """

    @staticmethod
    def get_user_groups():
        """
        Retrieve a list of all user-group associations.

        Returns:
            List[UserGroups]: A list of all user-group records in the database.
        """
        user_groups = list(UserGroupsModel.select())
        return user_groups

    @staticmethod
    def get_user_group(user_group_id: int):
        """
        Retrieve a specific user-group association by user and group IDs.

        Args:
            user_id (int): The ID of the user.
            group_id (int): The ID of the group.

        Returns:
            UserGroups: The user-group record with the specified IDs.

        Raises:
            HTTPException: 404 error if the user-group association is not found.
        """
        try:
            user_group = UserGroupsModel.get((UserGroupsModel.id == user_group_id))
            return user_group
        except DoesNotExist as exc:
            raise HTTPException(
                status_code=404,
                detail="User-group association not found"
            ) from exc

    @staticmethod
    def create_user_group(user_group: UserGroups = Body(...)):
        """
        Create a new user-group association.

        Args:
            user_group (UserGroups): The user-group data to create.

        Returns:
            UserGroups: The newly created user-group association.
        """
        try:
            created_user_group = UserGroupsModel.create(
                user_id=user_group.user_id,
                group_id=user_group.group_id
            )
            return created_user_group
        except IntegrityError as exc:
            raise HTTPException(
                status_code=500,
                detail="An error occurred while creating the user-group association"
            ) from exc

    @staticmethod
    def update_user_group(user_group_id:int, user_group: UserGroups =  Body(...)):
        """
        Update an existing user group with new user and group information.

        Args:
            user_group_id (int): The ID of the user group to update.
            user_group (UserGroups,optional): A body parameter containing the new user and group. 

        Returns:
            UserGroupsModel: The updated user group object.
        """
        try:
            u_group = UserGroupsModel.get(UserGroupsModel.id == user_group_id)
            u_group.user_id = user_group.user_id
            u_group.group_id = user_group.group_id
            u_group.save()
            return u_group
        except DoesNotExist as exc:
            raise HTTPException(status_code=404, detail="User group not found") from exc

    @staticmethod
    def delete_user_group(user_group_id:int):
        """
        Delete a user-group association by user and group IDs.

        Args:
            user_id (int): The ID of the user.
            group_id (int): The ID of the group.

        Returns:
            dict: A message indicating the result of the delete operation.

        Raises:
            HTTPException: 404 error if the user-group association is not found.
        """
        try:
            UserGroupsModel.delete().where((UserGroupsModel.id == user_group_id)).execute()
            return {"status": "User-group association deleted"}
        except DoesNotExist as exc:
            raise HTTPException(
                status_code=404,
                detail="User-group association not found"
            ) from exc
