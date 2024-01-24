import cowsay
from admin_bank import AdminBank
from admin_metro import AdminMetro
from user_bank import UserBank
from User_metro import UserMetro
from Pickle import PickleData
from Show_money_bank import ShowMoneyInfo
from ticket_metro import *

bank_admin_instance = AdminBank()
bank_user_instance = UserBank()
metro_admin_instance = AdminMetro()
metro_user_instance = UserMetro()
pickle_data = PickleData()
show_money_info = ShowMoneyInfo()
show_tickets_info = ShowTickets()


def panel_bank_user():
    while True:

        print("Do you want to create an account or login?\n"
              "1.create an account\n2.Login\n3.sing out\n")
        choice = input("Enter your choice:")
        if choice == "1":
            name = "pedram"  # input("Enter your name: ")
            lastname = "karimi"  # input("Enter your lastname: ")
            age = 27  # input("Enter your age: ")
            national_code = "1234512345"  # input("Enter your national code: ")
            phone = "09128355747"  # input("Enter your phone: ")
            address = "tehran ckjkdjsc kdsjk"  # input("Enter your address: ")
            bank_user_instance.Add_Information_User_Bank(name, lastname, age, phone, address, national_code)
            username = "Pedram.9060@gmail.com"  # input("Enter username: ")
            password = "Pedram$Karimi0020"
            bank_user_instance.add_password_username(username,password)
        elif choice == "2":
            print("\n**Please Enter username and password**\n")
            username = "Pedram.9060@gmail.com"   # input("Enter username: ")
            password =  "Pedram$Karimi0020"# input("Enter password: ")
            if bank_user_instance.check_credentials_User_Bank(username, password) == True:
                while True:
                    print("\n1.deposit\n2.withdraw\n3.Exit\n")
                    choice = input("Enter your choice: \n")
                    if choice == "1":
                        amount_deposit = 100 # input("Enter your amount for deposit: \n")
                        bank_user_instance.deposit(amount_deposit)
                        print("Your balance:", bank_user_instance.get_balance())
                    elif choice == "2":
                        amount_withdraw = input("\nEnter your amount for withdraw: ")
                        bank_user_instance.withdraw(amount_withdraw)
                        show_money_info.show_money(username)
                    elif choice == "3":
                        print("exit in panel User Bank\n")
                        break
                    else:
                        cowsay.tux("\nInvalid choice. Please Enter your choice 1.deposit 2.withdraw"
                                   " 3.exit in panel User Bank\n")

        elif choice == "3":
            print("exit in panel User Bank\n")
            break
        else:
            cowsay.tux("\nInvalid choice. Please Enter your choice "
                       "1.create an account 2.Login 3.sing out\n")
panel_bank_user()
def panel_bank_login():
    while True:
        print("**\nPlease Enter username and password**\n")
        username = "Pedram.9060@gmail.com" # input("Enter username: ")
        password = "Pedram$9060" #input("Enter password: ")
        if bank_admin_instance.check_credentials_Admin_Bank(username, password) == True:
            while True:
                print("Do you want to Show all account or Search?\n1.Show all account\n"
                      "2.Search\n3.sing out\n")
                choice = input("Enter your choice: \n")
                if choice == "1":
                    show_all = show_money_info.AllMoney
                    print(f"All account Info: {show_all}")
                elif choice == "2":
                    name_account = "Pedram.9060@gmail.com"#input("Enter name account: ")
                    all_account = show_money_info.AllMoney
                    search = all_account.values( )

                    a = show_money_info.UserMoneyBalance
                    print(f"Your baaaalance", a[1])
                    print(search)
                elif choice == "3":
                    print("exit in panel Admin Bank\n")
                    break
                else:
                    cowsay.tux("\nInvalid choice. Please Enter your choice "
                               "1.Show all account 2.Search 3.sing out\n")
        else:
            cowsay.tux("\nCredentials are incorrect.\n")
panel_bank_login()