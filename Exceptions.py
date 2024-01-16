"""
This module defines a set of custom exceptions that can be used in the admin and user management system.
These exceptions provide a way to handle specific error cases more gracefully and communicate issues to the calling code.
"""


class DuplicateUsernameError(Exception):
    """Exception raised when an attempt is made to create a user or admin with a duplicate username."""
    pass


class DuplicatePasswordError(Exception):
    """Exception raised when an attempt is made to create a user or admin with a duplicate password."""
    pass


class WeakPasswordError(Exception):
    """Exception raised when a password fails to meet the specified strength criteria during validation."""
    pass


class InvalidUsernameError(Exception):
    """Exception raised when a username does not meet the specified format during validation."""
    pass


class InvalidPhoneError(Exception):
    """Exception raised when a phone number does not meet the specified format during validation."""
    pass


class InvalidNationalCodeError(Exception):
    """Exception raised when a national code does not meet the specified format or length during validation."""
    pass


class InvalidAgeError(Exception):
    """Exception raised when an age is not within the specified range during validation."""
    pass


class AddressValidationError(Exception):
    """Custom exception for address validation errors."""
    pass


class NameValidationError(Exception):
    """Custom exception for name and lastname validation errors."""
    pass
