from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, BigInteger, Date, TIMESTAMP, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config.settings import DATABASE

Base = declarative_base()

# Roles
class Role(Base):
    __tablename__ = "roles"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    description = Column(Text)
    users = relationship("User", back_populates="role")

# Users
class User(Base):
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
    __tablename__ = "ingredient_categories"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    description = Column(Text)
    ingredients = relationship("Ingredient", back_populates="category")

# Ingredients
class Ingredient(Base):
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
    __tablename__ = "units"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    recipe_ingredients = relationship("RecipeIngredient", back_populates="unit")
    inventories = relationship("Inventory", back_populates="unit")
    shopping_list_items = relationship("ShoppingListItem", back_populates="unit")

# Recipe Ingredients
class RecipeIngredient(Base):
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
    __tablename__ = "menus"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    plan_id = Column(BigInteger, ForeignKey("plans.id"))
    name = Column(String(255))
    plan = relationship("Plan", back_populates="menus")
    recipes = relationship("MenuRecipe", back_populates="menu")

# Menu Recipes
class MenuRecipe(Base):
    __tablename__ = "menu_recipes"
    menu_id = Column(BigInteger, ForeignKey("menus.id"), primary_key=True)
    recipe_id = Column(BigInteger, ForeignKey("recipes.id"), primary_key=True)
    menu = relationship("Menu", back_populates="recipes")
    recipe = relationship("Recipe", back_populates="menus")

# Shopping Lists
class ShoppingList(Base):
    __tablename__ = "shopping_lists"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP)
    is_completed = Column(Boolean)
    user = relationship("User", back_populates="shopping_lists")
    ingredients = relationship("ShoppingListItem", back_populates="list")

# Shopping List Items
class ShoppingListItem(Base):
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
    __tablename__ = "notifications"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    message = Column(Text)
    sent_at = Column(TIMESTAMP)
    user = relationship("User")

# Groups
class Group(Base):
    __tablename__ = "groups"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(Text)
    users = relationship("UserGroup", back_populates="group")

# Categories
class Category(Base):
    __tablename__ = "categories"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    description = Column(Text)
    recipes = relationship("RecipeCategory", back_populates="category")

# User Recipes
class UserRecipe(Base):
    __tablename__ = "user_recipes"
    user_id = Column(BigInteger, ForeignKey("users.id"), primary_key=True)
    recipe_id = Column(BigInteger, ForeignKey("recipes.id"), primary_key=True)
    is_owner = Column(Boolean)
    user = relationship("User", back_populates="recipes")
    recipe = relationship("Recipe", back_populates="users")

# Recipe Categories
class RecipeCategory(Base):
    __tablename__ = "recipe_categories"
    recipe_id = Column(BigInteger, ForeignKey("recipes.id"), primary_key=True)
    category_id = Column(BigInteger, ForeignKey("categories.id"), primary_key=True)
    recipe = relationship("Recipe", back_populates="categories")
    category = relationship("Category", back_populates="recipes")

# User Groups
class UserGroup(Base):
    __tablename__ = "user_groups"
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), primary_key=True)
    group_id = Column(BigInteger, ForeignKey("groups.id"), primary_key=True)
    user = relationship("User")
    group = relationship("Group", back_populates="users")

# Database settings
DATABASE_URL = f"mysql+pymysql://{DATABASE["user"]}:{DATABASE["password"]}@{DATABASE["host"]}:{DATABASE["port"]}/{DATABASE["name"]}"
engine = create_engine(DATABASE_URL)


# Create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)