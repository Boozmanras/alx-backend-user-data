#!/usr/bin/env python3
"""
Auth class to manage API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Template class for all authentication systems
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path requires authentication.
        Supports wildcard exclusions (e.g., "/api/v1/stat*")
        Args:
            path (str): URL path to be checked
            excluded_paths (List[str]): List of paths that don't require auth
        Returns:
            bool: True if path requires auth, False otherwise
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:

            if excluded_path.endswith('*'):
                prefix = excluded_path[:-1]
                if path.startswith(prefix):
                    return False
            else:
                if not excluded_path.endswith('/'):
                    excluded_path += '/'
                if path == excluded_path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request
        Args:
            request: Flask request object
        Returns:
            str: The Authorization header value or None
        """
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user from the request
        Args:
            request: Flask request object
        Returns:
            TypeVar('User'): None for now - will be implemented later
        """
        return None
