"""
Main module for FastAPI application setup.

This module sets up the FastAPI application, manages the database connection
lifecycle, and includes routes.
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse
from helpers.api_key_auth import get_api_key
from database import database as connection
from routes.user_route import user_route
from routes.roles_route import roles_route
from routes.groups_route import groups_route
from routes.user_groups_route import user_groups_route

@asynccontextmanager
async def manage_lifespan(_app: FastAPI):
    """
    Manage the lifespan of the FastAPI application.

    Ensures the database connection is opened and closed properly.
    """
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        if not connection.is_closed():
            connection.close()

app = FastAPI(
    title="Microservicio de gestión de ususarios",
    version="2.0",
    contact={
        "name": "SANTIAGO QUINTERO RINCÓN, JOHAN SEBASTIAN GRISALES MONTOYA"
        +",JUAN FELIPE FRANCO TAMAYO",
        "url-Santiago": "https://github.com/ThePixels21",
        "url-Sebastian": "https://github.com/heysebas",
        "url-Felipe": "https://github.com/pipe0427",
        "email-santiago": "santiqrdev@gmail.com",
        "email-Sebastian": "",
        "email-Felipe": "pipe04271@gmail.com"
    },
    lifespan=manage_lifespan
)

@app.get("/")
async def read_root():
    """
    Redirect the root path to the API documentation.

    Returns a redirection response to the documentation page.
    """
    return RedirectResponse(url="/docs")

app.include_router(roles_route,
                   prefix="/routes",
                   tags=["Routes"],
                   dependencies=[Depends(get_api_key)])
app.include_router(user_route,
                   prefix="/users",
                   tags=["Users"],
                   dependencies=[Depends(get_api_key)])
app.include_router(groups_route,
                   prefix="/groups",
                   tags=["Groups"],
                   dependencies=[Depends(get_api_key)])
app.include_router(user_groups_route,
                   prefix="/user_groups",
                   tags=["UserGroups"],
                   dependencies=[Depends(get_api_key)])
