#!/usr/bin/env python3
"""
This module provides functions for securely hashing passwords
and verifying them using bcrypt.
"""

import bcrypt
from typing import bytes


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with a randomly-generated salt.
    Args:
        password (str): The plain text password to hash.
    Returns:
        bytes: The salted, hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Verify if the provided plain-text password matches the hashed password.
    Args:
        hashed_password (bytes): The hashed password to verify against.
        password (str): The plain-text password to check.
    Returns:
        bool: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
