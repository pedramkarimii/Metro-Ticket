from admin_bank import AdminBank
from admin_metro import AdminMetro
from user_bank import UserBank
from User_metro import UserMetro
from Pickle import PickleData
from Show_money_bank import ShowMoneyInfo


def main():
    """Main function to run the admin and user interaction loop."""
    bank_admin_instance = AdminBank()
    bank_user_instance = UserBank()
    metro_admin_instance = AdminMetro()
    metro_user_instance = UserMetro()
    pickle_data = PickleData()
    show_money_info = ShowMoneyInfo()
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
                    metro_user_instance.Add_Information(name, lastname, age, phone, address, national_code)
                elif choice == "2":
                    print("**\nPlease Enter username and password**\n")
                    username = "Pedram.9060@gmail.com"  # input("Enter username: ")
                    password = "Pedram$9060"  # input("Enter password: ")
                    if metro_user_instance.check_credentials_User(username, password) == True:
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
                    if metro_admin_instance.check_credentials(username, password) == True:
                        pickle_data.pickle_metro_admin_username_password()
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
                    bank_user_instance.Add_Information_User_Bank(name, lastname, age, phone, address, national_code)

                elif choice == "2":
                    print("**\nPlease Enter username and password**\n")
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    if bank_user_instance.check_credentials_User_Bank(username, password) == True:
                        print("\n1.deposit\n2.withdraw")
                        choice = input("Enter your choice: \n")
                        if choice == "1":
                            amount_deposit = input("Enter your amount for deposit: \n")
                            bank_user_instance.deposit(amount_deposit)
                            print("Your balance:", bank_user_instance.get_balance())
                        elif choice == "2":
                            amount_withdraw = input("\nEnter your amount for withdraw: ")
                            bank_user_instance.withdraw(amount_withdraw)
                            show_money_info.show_money(username)
            elif choice == "2":
                print("**\nPlease Enter username and password**\n")
                username = input("Enter username: ")
                password = input("Enter password: ")
                if bank_admin_instance.check_credentials_Admin_Bank(username, password) == True:

                    print("Do you want to Show all account or Search?\n1.Show all account\n2.Search")
                    choice = input("Enter your choice: \n")
                    if choice == "1":
                        show_all = show_money_info.AllMoney
                        print(f"All account Info: {show_all}")
                    elif choice == "2":
                        name_account = input("Enter name account: ")
                        all_account = show_money_info.AllMoney
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
