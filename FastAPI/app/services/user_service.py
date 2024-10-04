"""
This module provides a service class for managing user-related operations,
including retrieving, creating, updating, and deleting user records from the database.
"""

from peewee import DoesNotExist, IntegrityError
from fastapi import Body, HTTPException
from models.user import User
from database import UserModel


class UserService:
    """
    Service class for handling business logic related to users.

    This class provides methods to manage user records, including operations
    such as creating, updating, retrieving, and deleting user information
    from the database.

    Methods:
        get_users()
            Retrieve a list of all users.

        get_user(user_id: int)
            Retrieve a specific user by their ID.

        create_user(user: User)
            Create a new user record.

        update_user(user_id: int, user_data: Dict[str, str])
            Update an existing user record by their ID.

        delete_user(user_id: int)
            Delete a user record by their ID.

    Raises:
        HTTPException
            If a user is not found or if there is an error during any operation.
    """

    @staticmethod
    def get_users():
        """
        Retrieve a list of all users.

        Returns:
            List[User]: A list of all user records in the database.
        """
        users = list(UserModel.select())
        return users

    @staticmethod
    def get_user(user_id: int):
        """
        Retrieve a specific user by their ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            User: The user record with the specified ID.

        Raises:
            HTTPException: 404 error if the user with the given ID is not found.
        """
        try:
            user = UserModel.get(UserModel.id == user_id)
            return user
        except DoesNotExist as exc:
            raise HTTPException(status_code=404, detail="User not found") from exc

    @staticmethod
    def create_user(user: User = Body(...)):
        """
        Create a new user record.

        Args:
            user (User): The user data to create.

        Returns:
            User: The newly created user record.
        """
        try:
            created_user = UserModel.create(
                name=user.name,
                email=user.email,
                password=user.password,
                profile_photo=user.profile_photo,
                account_type=user.account_type,
                role_id=user.role_id
            )
            return created_user
        except DoesNotExist as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        except IntegrityError as exc:
            raise HTTPException(
                status_code=500, detail="An error occurred while creating the user"
            ) from exc

    @staticmethod
    def update_user(user_id: int, user: User = Body(...)):
        """
        Update an existing user record by their ID.

        Args:
            user_id (int): The ID of the user to update.

        Returns:
            User: The updated user record.

        Raises:
            HTTPException: 404 error if the user with the given ID is not found.
        """
        try:
            u_user = UserModel.get(UserModel.id == user_id)
            u_user.name = user.name
            u_user.email = user.email
            u_user.password = user.password
            u_user.profile_photo = user.profile_photo
            u_user.account_type = user.account_type
            u_user.role_id = user.role_id
            u_user.save()
            return u_user
        except DoesNotExist as exc:
            raise HTTPException(status_code=404, detail="User not found") from exc

    @staticmethod
    def delete_user(user_id: int):
        """
        Delete a user record by their ID.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            dict: A message indicating the result of the delete operation.

        Raises:
            HTTPException: 404 error if the user with the given ID is not found.
        """
        try:
            UserModel.delete().where(UserModel.id == user_id).execute()
            return {"status": "User deleted"}
        except DoesNotExist as exc:
            raise HTTPException(status_code=404, detail="User not found") from exc
