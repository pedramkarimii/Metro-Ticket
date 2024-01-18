from User_metro import *
from transactionProcessor import TransactionProcessor


class BankUser(UserMetroAdmin):
    UserUsernamePasswordBank = {}
    UserInfoBank = {}

    def __init__(self, balance=0, withdrawal_fee=0.5):
        super().__init__()
        self.balance = balance
        self.withdrawal_fee = withdrawal_fee
        self.transaction_processor = TransactionProcessor()

    def Add_Information_User_Bank(self, name, lastname, age, phone, address, national_code):

        """ Add user information to the UserInfoBank dictionary.

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

            self.UserInfoBank[name] = {
                "name": name, "lastname": lastname, "age": age, "national code": national_code, "phone": phone,
                "address": address
            }

            self.logger.info(f"Information added successfully - {self.UserInfoBank}")


        except (InvalidPhoneError, InvalidAgeError, InvalidNationalCodeError,

                NameValidationError, AddressValidationError, ValueError) as e:

            self.logger.error(f"Error adding information - {e}")

    def Add_Password_Username_Bank_User(self, username, password):
        """
        Add username and hashed password to the UserUsernamePasswordBank dictionary.

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

            if username in self.UserUsernamePasswordBank:
                raise ValueError(f"User instance already created for this username {username}.")


            elif username not in self.UserUsernamePasswordBank:
                UUID = uuid.uuid4()
                self.UserUsernamePasswordBank[username] = {"username": username, "password": hashed_password,
                                                           "ID": UUID}
                # self.logger.info(f"Added successfully - Username: {username}, Password: {hashed_password}, ID: {UUID}")
            else:
                self.logger.info(f"User {username} already exists.")
        except (WeakPasswordError, InvalidUsernameError, ValueError) as e:
            self.logger.error(f"Error adding user - {e}")

    def check_credentials_User_Bank(self, username, password):
        """Check if the provided credentials are correct."""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_data = self.UserUsernamePasswordBank.get(username)

        if user_data and user_data["password"] == hashed_password:
            self.logger.info("Credentials are correct.")
            print("Credentials are correct.")
            return True
        else:
            self.logger.warning("Credentials are incorrect.")
            print("Credentials are incorrect.")
            return False

    def __repr__(self):
        self.logger.info(f"Information: {self.UserUsernamePasswordBank}")
        return f"information :{self.UserUsernamePasswordBank}"

    def deposit(self, amount):
        self.transaction_processor.process_deposit(self, amount)
        self.logger.info("Information added successfully - Deposit")

    def withdraw(self, amount):
        self.transaction_processor.process_withdrawal(self, amount)
        self.logger.info("Information added successfully - Withdraw")

    def calculate_withdrawal_fee(self, amount):
        withdrawal_fee = self.withdrawal_fee
        self.logger.info(f"Information added successfully - {withdrawal_fee}")
        return withdrawal_fee

    def get_balance(self):
        self.logger.info(f"Information added successfully - {self.balance}")
        return self.balance


class UserBank(BankUser):
    pass


# add admin
input_admin = BankUser()
input_admin.Add_Password_Username_Bank_User("Pedram.9060@gmail.com", "Pedram$9060")
