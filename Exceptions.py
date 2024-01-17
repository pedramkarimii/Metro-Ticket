"""
This module defines a set of custom exceptions that can be used in the admin and user management system.
These exceptions provide a way to handle specific error cases more gracefully and communicate issues to the calling code.
"""


class MainException(Exception):
    pass


class DuplicateUsernameError(MainException):
    """Exception raised when an attempt is made to create a user or admin with a duplicate username."""
    pass


class DuplicatePasswordError(MainException):
    """Exception raised when an attempt is made to create a user or admin with a duplicate password."""
    pass


class WeakPasswordError(MainException):
    """Exception raised when a password fails to meet the specified strength criteria during validation."""
    pass


class InvalidUsernameError(MainException):
    """Exception raised when a username does not meet the specified format during validation."""
    pass


class InvalidPhoneError(MainException):
    """Exception raised when a phone number does not meet the specified format during validation."""
    pass


class InvalidNationalCodeError(MainException):
    """Exception raised when a national code does not meet the specified format or length during validation."""
    pass


class InvalidAgeError(MainException):
    """Exception raised when an age is not within the specified range during validation."""
    pass


class AddressValidationError(MainException):
    """Custom exception for address validation errors."""
    pass


class NameValidationError(Exception):
    """Custom exception for name and lastname validation errors."""
    pass


class InsufficientFundsError(Exception):
    pass
