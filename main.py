from admin import Admin
from User import User
from Bank_Account import BankCreatAccount


def main():
    """Main function to run the admin and user interaction loop."""
    admin_instance = Admin()
    user_instance = User()
    account_bank = BankCreatAccount()
    while True:
        print("\nEnter a number Options")
        print("Metro or Bank?\n1.Metro\n2.Bank Account")

        choice = input("Enter your choice or exit Enter a number 4: ")
        if choice == "1":
            print("\n**Welcome to the Metro**\nEnter a number Options")
            print("\nYou are an admin or user?\n1.User\n2.Admin")
            choice = input("Enter your choice or exit Enter a number 4: ")
            if choice == "1":
                print("\nEnter your choice\n1.sing up\n2.login\n3.sing out")
                choice = input("Enter your choice: \n")
                if choice == "1":
                    name = input("Enter your name: ")
                    lastname = input("Enter your lastname: ")
                    age = input("Enter your age: ")
                    national_code = input("Enter your national code: ")
                    phone = input("Enter your phone: ")
                    address = input("Enter your address: ")
                    user_instance.Add_Information(name, lastname, age, phone, address, national_code)
                elif choice == "2":
                    print("**\nPlease Enter username and password**\n")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    if user_instance.check_credentials_User(username, password) == True:
                        pass
                elif choice == "3":
                    print("exit in panel User\n")
                    break
                else:
                    print("\nInvalid choice. Please Enter your choice login or sing up or sing out.\n")

            elif choice == "2":
                print("\nEnter your choice\n1.login\n2.sing out")
                choice = input("Enter your choice: \n")
                if choice == "1":
                    print("**\nPlease Enter username and password**\n")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    if admin_instance.check_credentials(username, password) == True:
                        pass
                elif choice == "2":
                    print("exit in panel Admin\n")
                    break
                else:
                    print("\nInvalid choice. Please Enter your choice login or sing up or sing out.\n")

        elif choice == "2":
            print("\n**Welcome to the Bank**\nEnter a number Options")
            print("\nYou are an admin or user?\n1.User\n2.Admin")
            choice = input("\nEnter your choice: ")
            if choice == "1":
                print("Do you want to create an account or login?\n1.create an account\n2.Login\n")
                choice = input("Enter your choice:")
                if choice == "1":
                    name = input("Enter your name: ")
                    lastname = input("Enter your lastname: ")
                    age = input("Enter your age: ")
                    national_code = input("Enter your national code: ")
                    phone = input("Enter your phone: ")
                    address = input("Enter your address: ")
                    account_bank.Add_Information_User_Bank(name, lastname, age, phone, address, national_code)

                elif choice == "2":
                    print("**\nPlease Enter username and password**\n")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    if account_bank.check_credentials_User_Bank(username, password) == True:
                        print("\n1.deposit\n2.withdraw")
                        choice = input("Enter your choice: \n")
                        if choice == "1":
                            amount_deposit = input("Enter your amount for deposit: \n")
                            account_bank.deposit(amount_deposit)
                            print("Your balance:", account_bank.get_balance())
                        elif choice == "2":
                            amount_withdraw = input("\nEnter your amount for withdraw: ")
                            account_bank.withdraw(amount_withdraw)
                            account_bank.show_money(username)
            elif choice == "2":
                print("**\nPlease Enter username and password**\n")
                username = input("Enter username: ")
                password = input("Enter password: ")
                if account_bank.check_credentials_Admin_Bank(username, password) == True:

                    print("Do you want to Show all account or Search?\n1.Show all account\n2.Search")
                    choice = input("Enter your choice: \n")
                    if choice == "1":
                        show_all = account_bank.AllMoney
                        print(f"All account Info: {show_all}")
                    elif choice == "2":
                        name_account = input("Enter name account: ")
                        all_account = account_bank.AllMoney
                        search = all_account.keys(name_account)
                        print(search)
                else:
                    print("Credentials are incorrect.")
        elif choice == "4":
            break

        else:
            print("\nInvalid choice. Please Enter your choice amin or user or exit Enter number 4.\n")


if __name__ == '__main__':
    main()
