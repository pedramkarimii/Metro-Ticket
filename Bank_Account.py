from User import *
from Exceptions import InsufficientFundsError


class TransactionProcessor:
    MoneyInfo = []
    DepositMoney = []

    def process_deposit(self, account, amount):
        try:
            amount = float(amount)
            if amount > 0:
                account.balance += amount
                deposit_ = account.balance
                self.MoneyInfo.extend(str("deposit").split())
                self.MoneyInfo.extend(str(deposit_).split())
                self.DepositMoney.extend(str(deposit_).split())
                print(f"Deposited ${amount}. Current balance: ${account.balance}")
            else:
                print("Invalid deposit amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input for deposit. Please enter a valid numeric value.")

    def process_withdrawal(self, account, amount):
        try:
            amount = float(amount)
            if amount > 0:
                withdrawal_fee = account.calculate_withdrawal_fee(amount)
                total_withdrawal = amount + withdrawal_fee

                self.MoneyInfo.extend(str("fee").split())
                self.MoneyInfo.extend(str(withdrawal_fee).split())
                self.MoneyInfo.extend(str("withdrawal").split())
                self.MoneyInfo.extend(str(amount).split())
                deposit = float(self.DepositMoney[0])
                if total_withdrawal <= deposit:
                    deposit -= total_withdrawal
                    withdrawal_ = deposit
                    self.MoneyInfo.extend(str("Balance").split())
                    self.MoneyInfo.extend(str(withdrawal_).split())
                    print(
                        f"Withdrew ${amount} with a withdrawal fee of ${withdrawal_fee}. Current balance: ${account.balance}")
                else:
                    raise InsufficientFundsError("Insufficient funds.")
            else:
                print("Invalid withdrawal amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input for withdrawal. Please enter a valid numeric value.")
        except InsufficientFundsError as e:
            print(f"Error: {e}")

    def __str__(self):
        pass


class BankUser(UserMetro):
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


# add admin
input_admin = BankUser()
input_admin.Add_Password_Username_Bank_User("Pedram.9060@gmail.com", "Pedram$9060")


class BankAdmin(BankUser):
    AdminUsernamePasswordBank = {}

    def __init__(self):
        super().__init__()

    def Add_Password_Username_Bank_Admin(self, username, password):
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

            if username in self.AdminUsernamePasswordBank:
                raise ValueError(f"User instance already created for this username {username}.")


            elif username not in self.AdminUsernamePasswordBank:
                UUID = uuid.uuid4()
                self.AdminUsernamePasswordBank[username] = {"username": username, "password": hashed_password,
                                                            "ID": UUID}
                # self.logger.info(f"Added successfully - Username: {username}, Password: {hashed_password}, ID: {UUID}")
            else:
                self.logger.info(f"User {username} already exists.")
        except (WeakPasswordError, InvalidUsernameError, ValueError) as e:
            self.logger.error(f"Error adding user - {e}")

    def check_credentials_Admin_Bank(self, username, password):
        """Check if the provided credentials are correct."""
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_data = self.AdminUsernamePasswordBank.get(username)

        if user_data and user_data["password"] == hashed_password:
            self.logger.info("Credentials are correct.")
            print("Credentials are correct.")
            return True
        else:
            self.logger.warning("Credentials are incorrect.")
            print("Credentials are incorrect.")
            return False

    def __repr__(self):
        self.logger.info(f"Information: {self.AdminUsernamePasswordBank}")
        return f"information :{self.AdminUsernamePasswordBank}"


# add admin
input_admin = BankAdmin()
input_admin.Add_Password_Username_Bank_Admin("Pedram.9060@gmail.com", "Pedram$9060")


class BankAccount(BankAdmin, TransactionProcessor):
    pass


class ShowMoney(BankAccount):
    def __init__(self):
        """Call the constructor of the parent class (Bank)"""
        super().__init__()
        self.UserMoneyDeposit = []
        self.UserMoneyWithdraw = []
        self.UserMoneyFee = []
        self.UserMoneyBalance = []

        """Dictionary to store all financial information for each user."""

        self.AllMoney = {}

    """Method to display money-related information for a given user"""

    def show_money(self, name):
        deposit_info_deposit = self.MoneyInfo[1]
        self.UserMoneyDeposit.extend(["deposit", deposit_info_deposit])
        print(f"{name}: {self.UserMoneyDeposit}")
        self.UserMoneyDeposit.clear()

        withdraw_info = self.MoneyInfo[3]
        self.UserMoneyWithdraw.extend(["withdraw", withdraw_info])
        print(f"{name}: {self.UserMoneyWithdraw}")
        self.UserMoneyWithdraw.clear()

        fee_info = self.MoneyInfo[5]
        self.UserMoneyFee.extend(["fee", fee_info])
        print(f"{name}: {self.UserMoneyFee}")
        self.UserMoneyFee.clear()

        balance_info = self.MoneyInfo[7]
        self.UserMoneyBalance.extend(["balance", balance_info])
        print(f"{name}: {self.UserMoneyBalance}")
        self.AllMoney[name] = {"deposit": deposit_info_deposit[0:4], "withdraw": withdraw_info[0:4],
                               "fee": fee_info[0:4], "balance": balance_info[0:4]}
        self.UserMoneyBalance.clear()


class BankCreatAccount(ShowMoney):
    pass
