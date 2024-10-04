"""
This module defines the API routes for user management.

Routes provided:
- GET /users: Retrieve a list of all users.
- GET /users/{user_id}: Retrieve a specific user by ID.
- POST /users: Create a new user record.
- PUT /users/{user_id}: Update an existing user record by ID.
- DELETE /users/{user_id}: Delete a user record by ID.
"""

from fastapi import APIRouter, Body
from models.user import User
from services.user_service import UserService

user_route = APIRouter()

@user_route.get("/")
def get_users():
    """
    Retrieve a list of all users.

    Returns:
        List[User]: A list of all user records in the database.
    """
    return UserService.get_users()

@user_route.get("/{user_id}")
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
    return UserService.get_user(user_id)

@user_route.post("/")
def create_user(user: User = Body(...)):
    """
    Create a new user record.

    Args:
        user (User): The user data to create.

    Returns:
        User: The newly created user record.
    """
    return UserService.create_user(user)

@user_route.put("/{user_id}")
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
    return UserService.update_user(user_id, user)

@user_route.delete("/{user_id}")
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
    return UserService.delete_user(user_id)
