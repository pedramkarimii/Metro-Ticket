import hashlib
import re


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AdminMetro(metaclass=SingletonMeta):
    password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%#*?&]{8,}$"

    def __init__(self):
        self.passwords = set()

    def add_password_username(self, username, password):
        if not re.match(self.password_regex, password):
            raise ValueError(
                "Invalid password. It must have at least 8 characters and include at least one lowercase letter,"
                "\n one uppercase letter, one digit, and one special character @$!%*#?&.")

        hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
        if hashed_password in self.passwords:
            raise ValueError("This password is already in use. Please choose a different password.")
        elif len(username) < 4:
            raise ValueError("The username must have at least four characters.")
        elif username in self.passwords:
            raise ValueError(f"Username '{username}' already exists. Please choose a different username.")
        else:
            self.passwords.add(hashed_password)
            self.passwords.add(username)

    def check_credentials(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if username in self.passwords and hashed_password in self.passwords:
            print("Credentials are correct.")
        else:
            print("Credentials are incorrect.")


class Admin(AdminMetro):
    pass
