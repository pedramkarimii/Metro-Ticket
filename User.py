"""This module defines the UserMetro class for managing user information in a metro system.
It inherits functionality from the AdminMetro class and includes methods for adding user
information ,passwords and usernames."""
from admin import *


class UserMetro(AdminMetro):
    """Class representing user information management in a metro system."""
    UserUsernamePassword = {}
    UserInfo = {}

    def __init__(self):
        """Initialize an instance of UserMetro and call the constructor of the parent class (AdminMetro)."""
        super().__init__()

    def Add_Information(self, name, lastname, age, phone, address, national_code):

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
          - ValueError: If any other validation fails.
          """
        try:
            self.validate_name_lastname(name, lastname)
            self.validate_age(age)
            self.validate_phone(phone)
            self.validate_national_code(national_code)

            self.UserInfo[name] = {
                "name": name, "lastname": lastname, "age": age, "national code": national_code, "phone": phone,
                "address": address
            }

            self.logger.info(f"Information added successfully - {self.UserInfo}")


        except (InvalidPhoneError, InvalidAgeError, InvalidNationalCodeError,

                NameValidationError, AddressValidationError, ValueError) as e:

            self.logger.error(f"Error adding information - {e}")

    def Add_Password_Username(self, username, password):
        """
        Add username and hashed password to the UserUsernamePassword dictionary.

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

            if username in self.UserUsernamePassword:
                raise ValueError(f"User instance already created for this username {username}.")


            elif username not in self.UserUsernamePassword:
                UUID = uuid.uuid4()
                self.UserUsernamePassword[username] = {"username": username, "password": hashed_password, "ID": UUID}
                self.logger.info(f"Added successfully - Username: {username}, Password: {hashed_password}, ID: {UUID}")
            else:
                self.logger.info(f"User {username} already exists.")
        except (WeakPasswordError, InvalidUsernameError, ValueError) as e:
            self.logger.error(f"Error adding user - {e}")


class User(UserMetro):
    pass
