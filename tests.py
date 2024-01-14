import unittest
import logging
from admin import *
from io import StringIO
import sys
import hashlib

logging.basicConfig(filename='test_log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(console_handler)


class TestAdminMetro(unittest.TestCase):

    def setUp(self):
        self.admin = AdminMetro()

    def test_singleton_instance(self):
        admin1 = AdminMetro()
        admin2 = AdminMetro()
        self.assertIs(admin1, admin2)
        logging.info("Test: Singleton instance - Passed")

    def test_add_valid_password_username(self):
        self.admin.add_password_username("user1", "Password123@")
        self.assertIn("user1", self.admin.passwords)
        self.assertIn(hashlib.sha256("Password123@".encode("utf-8")).hexdigest(), self.admin.passwords)
        logging.info("Test: Add valid password and username - Passed")

    def test_add_invalid_password(self):
        with self.assertRaises(ValueError):
            self.admin.add_password_username("user2", "invalidpassword")
        logging.info("Test: Add invalid password - Passed")

    def test_add_existing_username(self):
        self.admin.add_password_username("user3", "ValidPassword123@")
        with self.assertRaises(ValueError):
            self.admin.add_password_username("user3", "AnotherPassword456#")
        logging.info("Test: Add existing username - Passed")

    def test_check_valid_credentials(self):
        self.admin.add_password_username("user4", "ValidPassword789*")
        with captured_output() as (out, err):
            self.admin.check_credentials("user4", "ValidPassword789*")
        self.assertEqual(out.getvalue().strip(), "Credentials are correct.")
        logging.info("Test: Check valid credentials - Passed")

    def test_check_invalid_credentials(self):
        with captured_output() as (out, err):
            self.admin.check_credentials("nonexistent_user", "InvalidPassword123@")
        self.assertEqual(out.getvalue().strip(), "Credentials are incorrect.")
        logging.info("Test: Check invalid credentials - Passed")


class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.admin = Admin()

    def test_inherits_from_admin_metro(self):
        self.assertIsInstance(self.admin, AdminMetro)
        logging.info("Test: Inherits from AdminMetro - Passed")


class captured_output:
    def __enter__(self):
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        return sys.stdout, sys.stderr

    def __exit__(self, *args):
        sys.stdout = self.old_stdout
        sys.stderr = self.old_stderr


if __name__ == '__main__':
    unittest.main()
