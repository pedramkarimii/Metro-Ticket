"""
This script provides a command-line interface for interacting with the admin and user functionalities
of the metro system. It creates instances of the Admin and User classes, allowing users to sign up,
log in, and log out. The script runs in a loop until the user decides to exit.
"""
from admin import Admin
from User import User


def main():
    """Main function to run the admin and user interaction loop."""
    admin_instance = Admin()
    user_instance = User()
    while True:
        print("\nOptions:")
        print("you are admin or user?")
        choice = input("Enter your choice or exit Enter number 4: ")

        if choice == "user":
            choice = input("Enter your choice login or sing up or sing out: ")
            if choice == "sing up":
                name = input("Enter your name: ")
                lastname = input("Enter your lastname: ")
                age = input("Enter your age: ")
                national_code = input("Enter your national code: ")
                phone = input("Enter your phone: ")
                address = input("Enter your address: ")
                username = input("Enter admin username: ")
                password = input("Enter admin password: ")
                user_instance.Add_Information(name, lastname, age, phone, address, national_code)
                user_instance.Add_Password_Username(username, password)
            elif choice == "login":
                username = input("Enter admin username: ")
                password = input("Enter admin password: ")
                user_instance.check_credentials(username, password)
            elif choice == "sing out":
                break
            else:
                print("Invalid choice. Please Enter your choice login or sing up or sing out ")

        elif choice == "admin":
            choice = input("Enter your choice login or sing up or sing out: ")
            if choice == "sing up":
                name = input("Enter your name: ")
                lastname = input("Enter your lastname: ")
                age = input("Enter your age: ")
                national_code = input("Enter your national code: ")
                phone = input("Enter your phone: ")
                address = input("Enter your address: ")
                username = input("Enter admin username: ")
                password = input("Enter admin password: ")
                admin_instance.add_information(name, lastname, age, phone, address, national_code)
                admin_instance.add_password_username(username, password)
            elif choice == "login":
                username = input("Enter admin username: ")
                password = input("Enter admin password: ")
                admin_instance.check_credentials(username, password)

            elif choice == "sing out":
                break
            else:
                print("Invalid choice. Please Enter your choice login or sing up or sing out ")
        elif choice == "4":
            break

        else:
            print("Invalid choice. Please Enter your choice amin or user or exit Enter number 4.")


if __name__ == '__main__':
    main()
