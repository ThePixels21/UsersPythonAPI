from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from config.settings import DATABASE

Base = declarative_base()

class Roles(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    description = Column(String(100))
    users = relationship("User", back_populates="role")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100))
    password = Column(String(50))
    profile_photo = Column(String(50))
    account_type = Column(String(50))
    role_id = Column(Integer, ForeignKey("roles.id"))
    role = relationship("Roles", back_populates="users")

# Database settings
DATABASE_URL = f"mysql+pymysql://{DATABASE["user"]}:{DATABASE["password"]}@{DATABASE["host"]}:{DATABASE["port"]}/{DATABASE["name"]}"
engine = create_engine(DATABASE_URL)


# Create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)