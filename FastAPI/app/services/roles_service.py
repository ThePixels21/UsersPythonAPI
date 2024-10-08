"""
This module provides a service class for managing role-related operations,
including retrieving, creating, updating, and deleting role records from the database.
"""

from peewee import DoesNotExist, IntegrityError
from fastapi import Body, HTTPException
from models.roles import Roles
from database import RolesModel


class RolesService:
    """
    Service class for handling business logic related to roles.

    This class provides methods to manage role records, including operations
    such as creating, updating, retrieving, and deleting role information
    from the database.

    Methods:
        get_roles()
            Retrieve a list of all roles.

        get_role(role_id: int)
            Retrieve a specific role by its ID.

        create_role(role: Roles)
            Create a new role record.

        update_role(role_id: int, role_data: Dict[str, str])
            Update an existing role record by its ID.

        delete_role(role_id: int)
            Delete a role record by its ID.
    """

    @staticmethod
    def get_roles():
        """
        Retrieve a list of all roles.

        Returns:
            List[Roles]: A list of all role records in the database.
        """
        roles = list(RolesModel.select())
        return roles

    @staticmethod
    def get_role(role_id: int):
        """
        Retrieve a specific role by its ID.

        Args:
            role_id (int): The ID of the role to retrieve.

        Returns:
            Roles: The role record with the specified ID.

        Raises:
            HTTPException: 404 error if the role with the given ID is not found.
        """
        try:
            role = RolesModel.get(RolesModel.id == role_id)
            return role
        except DoesNotExist as exc:
            raise HTTPException(status_code=404, detail="Role not found") from exc

    @staticmethod
    def create_role(role: Roles = Body(...)):
        """
        Create a new role record.

        Args:
            role (Roles): The role data to create.

        Returns:
            Roles: The newly created role record.
        """
        try:
            created_role = RolesModel.create(
                name=role.name,
                description=role.description
            )
            return created_role
        except IntegrityError as exc:
            raise HTTPException(
                status_code=500, detail="An error occurred while creating the role"
            ) from exc

    @staticmethod
    def update_role(role_id: int, role: Roles = Body(...)):
        """
        Update an existing role record by its ID.

        Args:
            role_id (int): The ID of the role to update.

        Returns:
            Roles: The updated role record.

        Raises:
            HTTPException: 404 error if the role with the given ID is not found.
        """
        try:
            u_role = RolesModel.get(RolesModel.id == role_id)
            u_role.name = role.name
            u_role.description = role.description
            u_role.save()
            return u_role
        except DoesNotExist as exc:
            raise HTTPException(status_code=404, detail="Role not found") from exc

    @staticmethod
    def delete_role(role_id: int):
        """
        Delete a role record by its ID.

        Args:
            role_id (int): The ID of the role to delete.

        Returns:
            dict: A message indicating the result of the delete operation.

        Raises:
            HTTPException: 404 error if the role with the given ID is not found.
        """
        try:
            RolesModel.delete().where(RolesModel.id == role_id).execute()
            return {"status": "Role deleted"}
        except DoesNotExist as exc:
            raise HTTPException(status_code=404, detail="Role not found") from exc
