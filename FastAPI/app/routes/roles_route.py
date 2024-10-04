"""
roles_route.py

Este módulo define las rutas para gestionar roles en la API.
Incluye funciones para obtener, crear, actualizar y eliminar roles.
"""

from fastapi import APIRouter, Body
from models.roles import Roles
from services.roles_service import RolesService

roles_route = APIRouter()

@roles_route.get("/")
def get_roles():
    """
    Retrieve a list of all roles.

    Returns:
        List[Roles]: A list of all role records in the database.
    """
    return RolesService.get_roles()

@roles_route.get("/{role_id}")
def get_role(role_id: int):
    """
    Retrieve a specific role by their ID.

    Args:
        role_id (int): The ID of the role to retrieve.

    Returns:
        Roles: The role record with the specified ID.

    Raises:
        HTTPException: 404 error if the role with the given ID is not found.
    """
    return RolesService.get_role(role_id)

@roles_route.post("/")
def create_role(role: Roles = Body(...)):
    """
    Create a new role record.

    Args:
        role (Roles): The role data to create.

    Returns:
        Roles: The newly created role record.
    """
    return RolesService.create_role(role)

@roles_route.put("/{role_id}")
def update_role(role_id: int, role: Roles = Body(...)):
    """
    Update an existing role record by their ID.

    Args:
        role_id (int): The ID of the role to update.

    Returns:
        Roles: The updated role record.

    Raises:
        HTTPException: 404 error if the role with the given ID is not found.
    """
    return RolesService.update_role(role_id, role)

@roles_route.delete("/{role_id}")
def delete_role(role_id: int):
    """
    Delete a role record by their ID.

    Args:
        role_id (int): The ID of the role to delete.

    Returns:
        dict: A message indicating the result of the delete operation.

    Raises:
        HTTPException: 404 error if the role with the given ID is not found.
    """
    return RolesService.delete_role(role_id)
