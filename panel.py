import cowsay

from panel_bank import panel_bank_user
from panel_bank import panel_bank_login
from panel_metro import panel_metro_user
from panel_metro import panel_metro_admin


def main():
    """Main function to run the admin and user interaction loop."""
    cowsay.trex("Welcome to my project")
    while True:
        print("\nEnter a number Options")
        print("Metro or Bank?\n1.Metro\n2.Bank Account\n3.Exit")

        choice = input("Enter your choice or exit Enter a number 4: ")
        if choice == "1":
            print("\n**Welcome to the Metro**\nEnter a number Options")
            print("\nYou are an admin or user?\n1.User\n2.Admin\n3. sing out")
            choice = input("Enter your choice or exit Enter a number 4: ")
            if choice == "1":
                panel_metro_user()

            elif choice == "2":
                panel_metro_admin()
            elif choice == "3":
                print("exit in panel metro\n")
                break
            else:
                cowsay.tux("\nInvalid choice. Please Enter your choice 1.User 2.Admin 3.sing out.\n")
        elif choice == "2":
            print("\n**Welcome to the Bank**\nEnter a number Options")
            print("\nYou are an admin or user?\n1.User\n2.Admin\n3.sing out")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                panel_bank_user()
            elif choice == "2":
                panel_bank_login()
            elif choice == "3":
                print("exit in panel bank\n")
                break
            else:
                cowsay.tux("\nInvalid choice. Please Enter your choice 1.User 2.Admin 3.sing out.\n")
        elif choice == "3":
            break
        else:
            cowsay.tux("\nInvalid choice. Please Enter your choice 1.Metro 2.Bank Account 3.Exit Enter\n")
