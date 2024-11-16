#!/usr/bin/env python3
"""
BasicAuth module for API authentication
"""
from api.v1.auth.auth import Auth
from typing import TypeVar


class BasicAuth(Auth):
    """
    Basic Authentication class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Authentication

        Args:
            authorization_header (str): The Authorization header value

        Returns:
            str: The Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """
        Decodes a Base64 string

        Args:
            base64_authorization_header (str): Base64 string to decode

        Returns:
            str: Decoded value as UTF8 string or None if invalid
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            import base64
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user credentials from decoded Base64 header

        Args:
            decoded_base64_authorization_header (str): Decoded Base64 string

        Returns:
            tuple: (user_email, user_password) or (None, None) if invalid
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        credentials = decoded_base64_authorization_header.split(':', 1)
        return (credentials[0], credentials[1])

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on email and password

        Args:
            user_email (str): user's email
            user_pwd (str): user's password

        Returns:
            User: User instance or None if invalid credentials
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            from models.user import User
            users = User.search({'email': user_email})

            if not users:
                return None

            user = users[0]
            if not user.is_valid_password(user_pwd):
                return None

            return user

        except Exception:
            return None
