"""
This module defines the AdminMetro class for managing metro system administration.
It includes methods for validating passwords, usernames, phone numbers, national codes,
names, and lastnames, as well as adding user information and checking credentials.
"""
import hashlib
import re
import uuid
from Exceptions import *
from Logger import *


class AdminMetro(Logger):
    """Class representing the administration of a metro system."""
    AdminUsernamePassword = {}
    AdminInfo = {}
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%#*?&]{8,}$"
    user_regex = r"^[a-zA-Z0-9._]+@[a-z.]+\.[a-z]{2,}$"
    mobile_regex = r"09(1[0-9]|3[0-9]|2[0-9]|0[1-9]|9[0-9])[0-9]{7}$"
    nationalcode = r"^\d{2}[0-9]{8}$"

    def __init__(self):
        super().__init__()

    def validate_password_strength(self, password):
        """Validate the strength of the given password."""
        if not re.match(self.password_regex, password):
            raise WeakPasswordError(
                "Invalid password. It must have at least 8 characters and include at least one lowercase letter,"
                "\n one uppercase letter, one digit, and one special character @$!%*#?&.")

    def validate_username_strength(self, username):
        """Validate the format of the given username."""
        if not re.match(self.user_regex, username):
            raise InvalidUsernameError("Invalid username format.")

    def validate_phone(self, phone):
        """Validate the format of the given phone number."""
        try:
            if not re.match(self.mobile_regex, phone):
                raise InvalidPhoneError("Invalid phone number format.")
        except re.error as e:
            raise InvalidPhoneError(f"Error in phone number validation: {e}")

    def validate_national_code(self, national_code):
        """Validate the format of the given national code."""
        if not re.match(self.nationalcode, national_code):
            raise InvalidNationalCodeError("The number must be 10 digits")

    def validate_name_lastname(self, name, lastname):
        """Validate the length and alphabetic nature of the given name and lastname."""
        if len(name) <= 3 or len(lastname) <= 3:
            raise NameValidationError("Name and Lastname must be at least 4 characters long.")

        if not name.isalpha() and not lastname.isalpha():
            raise NameValidationError("Name and Lastname must contain only alphabetic characters.")

    def validate_address(self, address):
        """Validate the content and length of the given address."""
        if len(address) < 3:
            raise AddressValidationError("Address must be at least 3 characters long.")

        if not all(char.isalpha() and char.isdigit() and char.isspace() for char in address):
            raise AddressValidationError("Address must contain only words and numbers.")

    def validate_age(self, age):
        """Validate the age to be between 18 and 60."""
        try:
            age = int(age)
            if not (18 <= age <= 60):
                raise InvalidAgeError("Invalid age. Age must be between 18 and 60.")
        except ValueError:
            raise InvalidAgeError("Invalid age. Age must be int and between 18 and 60.")

    def add_information(self, name, lastname, age, phone, address, national_code):

        """ Add user information to the UserInfo dictionary.

          Parameters:
          - name (str): User's first name.
          - lastname (str): User's last name.
          - age (int): User's age.
          - phone (str): User's phone number.
          - address (str): User's address.
          - national_code (str): User's national code.

          Raises:
          - InvalidPhoneError: If the phone number is in an invalid format.
          - InvalidAgeError: If the age is not between 18 and 60.
          - InvalidNationalCodeError: If the national code is invalid.
          - InvalidUsernameError: If the username is in an invalid format.
          - ValueError: If any other validation fails."""

        try:
            self.validate_name_lastname(name, lastname)
            self.validate_age(age)
            self.validate_phone(phone)
            self.validate_address(address)
            self.validate_national_code(national_code)

            self.AdminInfo[name] = {
                "name": name, "lastname": lastname, "age": age, "national code": national_code, "phone": phone,
                "address": address
            }
            self.logger.info(f"Information added successfully - {self.AdminInfo}")

        except (InvalidPhoneError, InvalidAgeError, InvalidNationalCodeError,
                NameValidationError, AddressValidationError, ValueError) as e:
            self.logger.error(f"Error adding information - {e}")

    def add_password_username(self, username, password):
        """
        Add username and hashed password to the AdminUsernamePassword dictionary.

        Parameters:
        - username (str): User's username.
        - password (str): User's password.

        Raises:
        - WeakPasswordError: If the password is weak.
        - InvalidUsernameError: If the username is in an invalid format.
        - ValueError: If the username already exists or any other validation fails.
        """
        try:
            self.validate_password_strength(password)
            self.validate_username_strength(username)
            hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

            if username in self.AdminUsernamePassword:
                raise ValueError(f"User instance already created for this username {username}.")

            elif len(self.AdminUsernamePassword) < 1:
                UUID = uuid.uuid4()
                self.AdminUsernamePassword[username] = {"username": username, "password": hashed_password, "ID": UUID}
                # self.logger.info(f"Added successfully - Username: {username}, Password: {hashed_password}, ID: {UUID}")
            else:
                self.logger.info("User already exists.")
        except (WeakPasswordError, InvalidUsernameError, ValueError) as e:
            self.logger.error(f"Error adding user - {e}")

    def check_credentials(self, username, password):
        """Check if the provided credentials are correct."""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_data = self.AdminUsernamePassword.get(username)

        if user_data and user_data["password"] == hashed_password:
            self.logger.info("Credentials are correct.")
            print("Credentials are correct.")
            return True
        else:
            self.logger.warning("Credentials are incorrect.")
            print("Credentials are incorrect.")
            return False

    def __str__(self):
        self.logger.info(f"Information: {self.AdminUsernamePassword}")
        return f"information :{self.AdminUsernamePassword}"


class Admin(AdminMetro):
    pass


# add admin
input_admin = Admin()
input_admin.add_password_username("Pedram.9060@gmail.com", "Pedram$9060")

