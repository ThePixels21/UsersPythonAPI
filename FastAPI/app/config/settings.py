"""
This module defines the settings of the database.
"""

import os
from dotenv import load_dotenv

# Load variables using .env file
load_dotenv()

ENV = os.getenv("ENV", "dev")  # 'dev' will be the default value if 'ENV' is not stablished

# Database configurations for different environments
if ENV == "production":
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),
        "engine": "peewee.MySQLDatabase",
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "host": os.getenv("MYSQL_HOST"),
        "port": int(os.getenv("MYSQL_PORT")),
    }
else:
    DATABASE = {
        "name": os.getenv("MYSQL_DATABASE"),
        "engine": "peewee.MySQLDatabase",
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "host": os.getenv("MYSQL_HOST"),
        "port": int(os.getenv("MYSQL_PORT")),
    }
