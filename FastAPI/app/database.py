"""
This module defines the models for managing users, roles, and groups in the system,
using the Peewee ORM for MySQL database interactions. It establishes relationships 
between users, roles, and groups and includes cascading delete behaviors.
"""

import os
from dotenv import load_dotenv
from peewee import Model, MySQLDatabase, AutoField, CharField, ForeignKeyField

# Load environment variables from .env file
load_dotenv()

# Initialize the MySQL database connection using environment variables
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)

class RolesModel(Model):
    """
    Represents a role in the system. Each user is associated with a role.
    
    Attributes:
        id (AutoField): Unique identifier for the role.
        name (CharField): Name of the role, maximum 50 characters.
        description (CharField): Description of the role, maximum 50 characters.
    """
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)

    class Meta:
        """
        Meta class for RoleModel to specify the database and table name.
        
        Attributes:
            database (MySQLDatabase): The database connection used for this model.
            table_name (str): The name of the table in the database.
        """

        # pylint: disable=too-few-public-methods
        database = database
        table_name = "roles"

class UserModel(Model):
    """
    Represents a user in the system.
    
    Attributes:
        id (AutoField): Unique identifier for the user.
        name (CharField): Name of the user, maximum 50 characters.
        email (CharField): Email address of the user, maximum 50 characters.
        password (CharField): Encrypted password of the user, maximum 50 characters.
        profile_photo (CharField): URL or path of the user's profile photo, maximum 50 characters.
        account_type (CharField): Type of user account, maximum 50 characters.
        role_id (ForeignKeyField): Foreign key to the RoleModel, representing the user's role.
    """
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50)
    profile_photo = CharField(max_length=50)
    account_type = CharField(max_length=50)
    role_id = ForeignKeyField(RolesModel, backref='users', on_delete='CASCADE')

    class Meta:
        """
        Meta class for UserModel to specify the database and table name.
        
        Attributes:
            database (MySQLDatabase): The database connection used for this model.
            table_name (str): The name of the table in the database.
        """

        # pylint: disable=too-few-public-methods
        database = database
        table_name = "users"

class GroupsModel(Model):
    """
    Represents a group in the system.
    
    Attributes:
        id (AutoField): Unique identifier for the group.
        description (CharField): Description of the group, maximum 50 characters.
    """
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    description = CharField(max_length=50)

    class Meta:
        """
        Meta class for GroupModule to specify the database and table name.
        
        Attributes:
            database (MySQLDatabase): The database connection used for this model.
            table_name (str): The name of the table in the database.
        """

        # pylint: disable=too-few-public-methods
        database = database
        table_name = "groups"

class UserGroupsModel(Model):
    """
    Represents the association between a user and a group.
    
    Attributes:
        id (AutoField): Unique identifier for the user-group relation.
        user_id (ForeignKeyField): Foreign key to UserModel, representing the user.
        group_id (ForeignKeyField): Foreign key to GroupModule, representing the group.
    """
    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(UserModel, backref='user_groups', on_delete='CASCADE')
    group_id = ForeignKeyField(GroupsModel, backref='user_groups', on_delete='CASCADE')

    class Meta:
        """
        Meta class for UserGroupsModel to specify the database and table name.
        
        Attributes:
            database (MySQLDatabase): The database connection used for this model.
            table_name (str): The name of the table in the database.
        """

        # pylint: disable=too-few-public-methods
        database = database
        table_name = "user_groups"
