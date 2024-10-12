"""
This module defines the models for the complete database in the system,
using the SQLAlchemy ORM for MySQL database interactions.
"""

from sqlalchemy import (Column, Integer, String, Text, ForeignKey,
                        Boolean, BigInteger, Date, TIMESTAMP, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config.settings import DATABASE

Base = declarative_base()

# Roles
class Role(Base):
    """
        Role class representing user roles in the system.

        Attributes:
            id (BigInteger): Primary key for the role.
            name (String): Name of the role.
            description (Text): Description of the role.
            users (relationship): Relationship to the User model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "roles"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    description = Column(Text)
    users = relationship("User", back_populates="role")

# Users
class User(Base):
    """
        User class representing users in the system.

        Attributes:
            id (BigInteger): Primary key for the user.
            name (String): Name of the user.
            email (String): Email of the user.
            password (String): Encrypted password.
            profile_photo (String): Profile photo URL.
            account_type (String): Type of account (e.g., admin, regular).
            role_id (BigInteger): Foreign key to Role model.
            role (relationship): Relationship to the Role model.
            recipes (relationship): Relationship to the UserRecipe model.
            inventories (relationship): Relationship to the Inventory model.
            plans (relationship): Relationship to the Plan model.
            shopping_lists (relationship): Relationship to the ShoppingList model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    email = Column(String(255), unique=True)
    password = Column(String(255))
    profile_photo = Column(String(255))
    account_type = Column(String(255))
    role_id = Column(BigInteger, ForeignKey("roles.id"))
    role = relationship("Role", back_populates="users")
    recipes = relationship("UserRecipe", back_populates="user")
    inventories = relationship("Inventory", back_populates="user")
    plans = relationship("Plan", back_populates="user")
    shopping_lists = relationship("ShoppingList", back_populates="user")

# Recipes
class Recipe(Base):
    """
        Recipe class representing a recipe in the system.

        Attributes:
            id (BigInteger): Primary key for the recipe.
            name (String): Name of the recipe.
            description (Text): Detailed description of the recipe.
            instructions (Text): Step-by-step cooking instructions.
            difficulty (String): Difficulty level (e.g., easy, medium, hard).
            preparation_time (Integer): Preparation time in minutes.
            is_public (Boolean): Indicates if the recipe is publicly visible.
            categories (relationship): Relationship to RecipeCategory model.
            ingredients (relationship): Relationship to RecipeIngredient model.
            menus (relationship): Relationship to MenuRecipe model.
            users (relationship): Relationship to UserRecipe model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "recipes"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(Text)
    instructions = Column(Text)
    difficulty = Column(String(50))
    preparation_time = Column(Integer)
    is_public = Column(Boolean)
    categories = relationship("RecipeCategory", back_populates="recipe")
    ingredients = relationship("RecipeIngredient", back_populates="recipe")
    menus = relationship("MenuRecipe", back_populates="recipe")
    users = relationship("UserRecipe", back_populates="recipe")

# Ingredient Categories
class IngredientCategory(Base):
    """
        IngredientCategory class representing categories for ingredients.

        Attributes:
            id (BigInteger): Primary key for the ingredient category.
            name (String): Name of the category.
            description (Text): Description of the category.
            ingredients (relationship): Relationship to the Ingredient model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "ingredient_categories"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    description = Column(Text)
    ingredients = relationship("Ingredient", back_populates="category")

# Ingredients
class Ingredient(Base):
    """
        Ingredient class representing an ingredient in the system.

        Attributes:
            id (BigInteger): Primary key for the ingredient.
            name (String): Name of the ingredient.
            category_id (BigInteger): Foreign key to the IngredientCategory model.
            category (relationship): Relationship to the IngredientCategory model.
            recipe_ingredients (relationship): Relationship to RecipeIngredient model.
            inventories (relationship): Relationship to Inventory model.
            shopping_list_items (relationship): Relationship to ShoppingListItem model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "ingredients"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    category_id = Column(BigInteger, ForeignKey("ingredient_categories.id"))
    category = relationship("IngredientCategory", back_populates="ingredients")
    recipe_ingredients = relationship("RecipeIngredient", back_populates="ingredient")
    inventories = relationship("Inventory", back_populates="ingredient")
    shopping_list_items = relationship("ShoppingListItem", back_populates="ingredient")

# Units
class Unit(Base):
    """
        Unit class representing units of measurement.

        Attributes:
            id (BigInteger): Primary key for the unit.
            name (String): Name of the unit (e.g., gram, liter).
            recipe_ingredients (relationship): Relationship to RecipeIngredient model.
            inventories (relationship): Relationship to Inventory model.
            shopping_list_items (relationship): Relationship to ShoppingListItem model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "units"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    recipe_ingredients = relationship("RecipeIngredient", back_populates="unit")
    inventories = relationship("Inventory", back_populates="unit")
    shopping_list_items = relationship("ShoppingListItem", back_populates="unit")

# Recipe Ingredients
class RecipeIngredient(Base):
    """
        RecipeIngredient class representing the association between recipes and ingredients.

        Attributes:
            recipe_id (BigInteger): Foreign key to the Recipe model.
            ingredient_id (BigInteger): Foreign key to the Ingredient model.
            quantity (String): Amount of the ingredient required.
            unit_id (BigInteger): Foreign key to the Unit model.
            recipe (relationship): Relationship to the Recipe model.
            ingredient (relationship): Relationship to the Ingredient model.
            unit (relationship): Relationship to the Unit model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "recipe_ingredients"
    recipe_id = Column(BigInteger, ForeignKey("recipes.id"), primary_key=True)
    ingredient_id = Column(BigInteger, ForeignKey("ingredients.id"), primary_key=True)
    quantity = Column(String(50))
    unit_id = Column(BigInteger, ForeignKey("units.id"))
    recipe = relationship("Recipe", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="recipe_ingredients")
    unit = relationship("Unit", back_populates="recipe_ingredients")

# Inventories
class Inventory(Base):
    """
        Inventory class representing the user's inventory of ingredients.

        Attributes:
            id (BigInteger): Primary key for the inventory.
            user_id (BigInteger): Foreign key to the User model.
            ingredient_id (BigInteger): Foreign key to the Ingredient model.
            quantity (String): Amount of the ingredient in inventory.
            unit_id (BigInteger): Foreign key to the Unit model.
            expiration_date (Date): Expiration date of the ingredient.
            user (relationship): Relationship to the User model.
            ingredient (relationship): Relationship to the Ingredient model.
            unit (relationship): Relationship to the Unit model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "inventories"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    ingredient_id = Column(BigInteger, ForeignKey("ingredients.id"))
    quantity = Column(String(50))
    unit_id = Column(BigInteger, ForeignKey("units.id"))
    expiration_date = Column(Date)
    user = relationship("User", back_populates="inventories")
    ingredient = relationship("Ingredient", back_populates="inventories")
    unit = relationship("Unit", back_populates="inventories")

# Plans
class Plan(Base):
    """
            Plan class representing a user's plan within the system.

            Attributes:
                id (BigInteger): Primary key for the plan.
                user_id (BigInteger): Foreign key to the User model.
                start_date (Date): The start date of the plan.
                end_date (Date): The end date of the plan.
                plan_type (String): The type of plan (e.g., weekly, monthly).
                user (relationship): Relationship to the User model.
                menus (relationship): Relationship to the Menu model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "plans"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    plan_type = Column(String(50))
    user = relationship("User", back_populates="plans")
    menus = relationship("Menu", back_populates="plan")

# Menus
class Menu(Base):
    """
            Menu class representing a menu within a plan.

            Attributes:
                id (BigInteger): Primary key for the menu.
                plan_id (BigInteger): Foreign key to the Plan model.
                name (String): Name of the menu.
                plan (relationship): Relationship to the Plan model.
                recipes (relationship): Relationship to the MenuRecipe model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "menus"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    plan_id = Column(BigInteger, ForeignKey("plans.id"))
    name = Column(String(255))
    plan = relationship("Plan", back_populates="menus")
    recipes = relationship("MenuRecipe", back_populates="menu")

# Menu Recipes
class MenuRecipe(Base):
    """
            MenuRecipe class representing the association between menus and recipes.

            Attributes:
                menu_id (BigInteger): Foreign key to the Menu model.
                recipe_id (BigInteger): Foreign key to the Recipe model.
                menu (relationship): Relationship to the Menu model.
                recipe (relationship): Relationship to the Recipe model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "menu_recipes"
    menu_id = Column(BigInteger, ForeignKey("menus.id"), primary_key=True)
    recipe_id = Column(BigInteger, ForeignKey("recipes.id"), primary_key=True)
    menu = relationship("Menu", back_populates="recipes")
    recipe = relationship("Recipe", back_populates="menus")

# Shopping Lists
class ShoppingList(Base):
    """
            ShoppingList class representing a shopping list created by a user.

            Attributes:
                id (BigInteger): Primary key for the shopping list.
                user_id (BigInteger): Foreign key to the User model.
                created_at (TIMESTAMP): Timestamp of when the list was created.
                is_completed (Boolean): Indicates if the shopping list has been completed.
                user (relationship): Relationship to the User model.
                ingredients (relationship): Relationship to the ShoppingListItem model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "shopping_lists"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP)
    is_completed = Column(Boolean)
    user = relationship("User", back_populates="shopping_lists")
    ingredients = relationship("ShoppingListItem", back_populates="list")

# Shopping List Items
class ShoppingListItem(Base):
    """
            ShoppingListItem class representing items within a shopping list.

            Attributes:
                list_id (BigInteger): Foreign key to the ShoppingList model.
                ingredient_id (BigInteger): Foreign key to the Ingredient model.
                quantity (String): Quantity of the ingredient required.
                unit_id (BigInteger): Foreign key to the Unit model.
                status (String): Status of the item (e.g., pending, purchased).
                list (relationship): Relationship to the ShoppingList model.
                ingredient (relationship): Relationship to the Ingredient model.
                unit (relationship): Relationship to the Unit model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "shopping_list_items"
    list_id = Column(BigInteger, ForeignKey("shopping_lists.id"), primary_key=True)
    ingredient_id = Column(BigInteger, ForeignKey("ingredients.id"), primary_key=True)
    quantity = Column(String(50))
    unit_id = Column(BigInteger, ForeignKey("units.id"))
    status = Column(String(50))
    list = relationship("ShoppingList", back_populates="ingredients")
    ingredient = relationship("Ingredient", back_populates="shopping_list_items")
    unit = relationship("Unit", back_populates="shopping_list_items")

# Notifications
class Notification(Base):
    """
            Notification class representing a user notification.

            Attributes:
                id (BigInteger): Primary key for the notification.
                user_id (BigInteger): Foreign key to the User model.
                message (Text): The notification message.
                sent_at (TIMESTAMP): Timestamp of when the notification was sent.
                user (relationship): Relationship to the User model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "notifications"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    message = Column(Text)
    sent_at = Column(TIMESTAMP)
    user = relationship("User")

# Groups
class Group(Base):
    """
            Group class representing user groups within the system.

            Attributes:
                id (BigInteger): Primary key for the group.
                name (String): Name of the group.
                description (Text): Description of the group.
                users (relationship): Relationship to the UserGroup model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "groups"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(Text)
    users = relationship("UserGroup", back_populates="group")

# Categories
class Category(Base):
    """
            Category class representing recipe categories.

            Attributes:
                id (BigInteger): Primary key for the category.
                name (String): Name of the category.
                description (Text): Description of the category.
                recipes (relationship): Relationship to the RecipeCategory model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "categories"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    description = Column(Text)
    recipes = relationship("RecipeCategory", back_populates="category")

# User Recipes
class UserRecipe(Base):
    """
            UserRecipe class representing the association between users and recipes.

            Attributes:
                user_id (BigInteger): Foreign key to the User model.
                recipe_id (BigInteger): Foreign key to the Recipe model.
                is_owner (Boolean): Indicates if the user is the owner of the recipe.
                user (relationship): Relationship to the User model.
                recipe (relationship): Relationship to the Recipe model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "user_recipes"
    user_id = Column(BigInteger, ForeignKey("users.id"), primary_key=True)
    recipe_id = Column(BigInteger, ForeignKey("recipes.id"), primary_key=True)
    is_owner = Column(Boolean)
    user = relationship("User", back_populates="recipes")
    recipe = relationship("Recipe", back_populates="users")

# Recipe Categories
class RecipeCategory(Base):
    """
            RecipeCategory class representing the association between recipes and categories.

            Attributes:
                recipe_id (BigInteger): Foreign key to the Recipe model.
                category_id (BigInteger): Foreign key to the Category model.
                recipe (relationship): Relationship to the Recipe model.
                category (relationship): Relationship to the Category model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "recipe_categories"
    recipe_id = Column(BigInteger, ForeignKey("recipes.id"), primary_key=True)
    category_id = Column(BigInteger, ForeignKey("categories.id"), primary_key=True)
    recipe = relationship("Recipe", back_populates="categories")
    category = relationship("Category", back_populates="recipes")

# User Groups
class UserGroup(Base):
    """
            UserGroup class representing the association between users and groups.

            Attributes:
                id (BigInteger): Primary key for the user group association.
                user_id (BigInteger): Foreign key to the User model.
                group_id (BigInteger): Foreign key to the Group model.
                user (relationship): Relationship to the User model.
                group (relationship): Relationship to the Group model.
    """
    # pylint: disable=too-few-public-methods
    __tablename__ = "user_groups"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), primary_key=True)
    group_id = Column(BigInteger, ForeignKey("groups.id"), primary_key=True)
    user = relationship("User")
    group = relationship("Group", back_populates="users")

# Database settings
DATABASE_URL = (f"mysql+pymysql://{DATABASE['user']}:{DATABASE['password']}@"
                f"{DATABASE['host']}:{DATABASE['port']}/{DATABASE['name']}")
engine = create_engine(DATABASE_URL)


# Create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
