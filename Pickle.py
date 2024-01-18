import pickle
from Logger import Logger


class PickleInfo(Logger):
    """class that pickles information."""

    def __init__(self):
        super().__init__()

    def pickle_metro_admin_username_password(self, filename="admin_metro_UsernamePassword.pkl"):
        """Pickles AdminUsernamePassword dictionaries to a file."""
        try:
            if self.AdminUsernamePassword:
                with open(filename, "wb") as file:
                    pickle.dump(self.AdminUsernamePassword, file)
                    self.logger.info("Data pickled successfully.")
            else:
                return "Data was not pickled successfully!!!!!!!!!"
        except Exception as e:
            self.logger.error(f"Error pickling data - {e}")

    def unpickle_metro_admin_username_password(self, filename="admin_metro_UsernamePassword.pkl"):
        """Unpickle AdminUsernamePassword and AdminInfo dictionaries from a file."""
        try:
            with open(filename, "rb") as file:
                self.AdminUsernamePassword = pickle.load(file)
                print(self.AdminUsernamePassword)
                self.logger.info("Data unpickled successfully.")
        except Exception as e:
            self.logger.error(f"Error unpickling data - {e}")

    def pickle_metro_admin_info(self, filename="admin_metro_info.pkl"):
        """Pickles AdminInfo dictionaries to a file."""
        try:
            if self.AdminInfo:
                with open(filename, "wb") as file:
                    pickle.dump(self.AdminInfo, file)
                    self.logger.info("Data pickled successfully.")
            else:
                return "Data was not pickled successfully!!!!!!!!!"
        except Exception as e:
            self.logger.error(f"Error pickling data - {e}")

    def unpickle_metro_admin_info(self, filename="admin_metro_info.pkl"):
        """unpickle AdminInfo dictionaries from a file."""
        try:
            with open(filename, "rb") as file:
                self.AdminInfo = pickle.load(file)
                print(self.AdminInfo)
                self.logger.info("Data unpickled successfully.")
        except Exception as e:
            self.logger.error(f"Error unpickling data - {e}")

    def pickle_metro_user_username_password(self, filename="user_metro_UsernamePassword.pkl"):
        """Pickles UserUsernamePassword dictionaries to a file."""
        try:
            if self.UserUsernamePassword:
                with open(filename, "wb") as file:
                    pickle.dump(self.UserUsernamePassword, file)
                    self.logger.info("Data pickled successfully.")
            else:
                return "Data was not pickled successfully!!!!!!!!!"
        except Exception as e:
            self.logger.error(f"Error pickling data - {e}")

    def unpickle_metro_user_username_password(self, filename="user_metro_UsernamePassword.pkl"):
        """unpickle UserUsernamePassword dictionaries from a file."""
        try:
            with open(filename, "rb") as file:
                self.UserUsernamePassword = pickle.load(file)
                print(self.UserUsernamePassword)
                self.logger.info("Data unpickled successfully.")
        except Exception as e:
            self.logger.error(f"Error unpickling data - {e}")

    def pickle_metro_user_info(self, filename="user_metro_info.pkl"):
        """Pickles UserInfo dictionaries to a file."""
        try:
            if self.UserInfo:
                with open(filename, "wb") as file:
                    pickle.dump(self.UserInfo, file)
                    self.logger.info("Data pickled successfully.")
            else:
                return "Data was not pickled successfully!!!!!!!!!"
        except Exception as e:
            self.logger.error(f"Error pickling data - {e}")

    def unpickle_metro_user_info(self, filename="user_metro_info.pkl"):
        """unpickle UserInfo dictionaries from a file."""
        try:
            with open(filename, "rb") as file:
                self.UserInfo = pickle.load(file)
                print(self.UserInfo)
                self.logger.info("Data unpickled successfully.")
        except Exception as e:
            self.logger.error(f"Error unpickling data - {e}")

    def pickle_bank_admin_username_password(self, filename="admin_bank_UsernamePassword.pkl"):
        """Pickles AdminUsernamePassword dictionaries to a file."""
        try:
            if self.AdminUsernamePasswordBank:
                with open(filename, "wb") as file:
                    pickle.dump(self.AdminUsernamePasswordBank, file)
                    self.logger.info("Data pickled successfully.")
            else:
                return "Data was not pickled successfully!!!!!!!!!"
        except Exception as e:
            self.logger.error(f"Error pickling data - {e}")

    def unpickle_bank_admin_username_password(self, filename="admin_bank_UsernamePassword.pkl"):
        """Unpickle AdminUsernamePassword and AdminInfo dictionaries from a file."""
        try:
            with open(filename, "rb") as file:
                self.AdminUsernamePasswordBank = pickle.load(file)
                print(self.AdminUsernamePasswordBank)
                self.logger.info("Data unpickled successfully.")
        except Exception as e:
            self.logger.error(f"Error unpickling data - {e}")

    def pickle_bank_admin_info(self, filename="admin_bank_info.pkl"):
        """Pickles AdminInfoBank dictionaries to a file."""
        try:
            if self.AdminInfoBank:
                with open(filename, "wb") as file:
                    pickle.dump(self.AdminInfoBank, file)
                    self.logger.info("Data pickled successfully.")
            else:
                return "Data was not pickled successfully!!!!!!!!!"
        except Exception as e:
            self.logger.error(f"Error pickling data - {e}")

    def unpickle_bank_admin_info(self, filename="admin_bank_info.pkl"):
        """unpickle AdminInfoBank dictionaries from a file."""
        try:
            with open(filename, "rb") as file:
                self.AdminInfoBank = pickle.load(file)
                print(self.AdminInfoBank)
                self.logger.info("Data unpickled successfully.")
        except Exception as e:
            self.logger.error(f"Error unpickling data - {e}")

    def pickle_bank_user_username_password(self, filename="user_bank_UsernamePassword.pkl"):
        """Pickles UserUsernamePasswordBank dictionaries to a file."""
        try:
            if self.UserUsernamePasswordBank:
                with open(filename, "wb") as file:
                    pickle.dump(self.UserUsernamePasswordBank, file)
                    self.logger.info("Data pickled successfully.")
            else:
                return "Data was not pickled successfully!!!!!!!!!"
        except Exception as e:
            self.logger.error(f"Error pickling data - {e}")

    def unpickle_bank_user_username_password(self, filename="user_bank_UsernamePassword.pkl"):
        """Unpickle UserUsernamePasswordBank and AdminInfo dictionaries from a file."""
        try:
            with open(filename, "rb") as file:
                self.UserUsernamePasswordBank = pickle.load(file)
                print(self.UserUsernamePasswordBank)
                self.logger.info("Data unpickled successfully.")
        except Exception as e:
            self.logger.error(f"Error unpickling data - {e}")

    def pickle_bank_user_info(self, filename="bank_metro_info.pkl"):
        """Pickles UserInfoBank dictionaries to a file."""
        try:
            if self.UserInfoBank:
                with open(filename, "wb") as file:
                    pickle.dump(self.UserInfoBank, file)
                    self.logger.info("Data pickled successfully.")
            else:
                return "Data was not pickled successfully!!!!!!!!!"
        except Exception as e:
            self.logger.error(f"Error pickling data - {e}")

    def unpickle_bank_user_info(self, filename="bank_metro_info.pkl"):
        """unpickle UserInfoBank dictionaries from a file."""
        try:
            with open(filename, "rb") as file:
                self.UserInfoBank = pickle.load(file)
                print(self.UserInfoBank)
                self.logger.info("Data unpickled successfully.")
        except Exception as e:
            self.logger.error(f"Error unpickling data - {e}")


class PickleData(PickleInfo):
    pass
