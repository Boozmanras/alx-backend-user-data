#!/usr/bin/env python3
"""
User model module for SQLAlchemy database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    User class for database table 'users'
    Attributes:
        id (int): Primary key
        email (str): User's email address
        hashed_password (str): Hashed password
        session_id (str): Session identifier
        reset_token (str): Password reset token
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
