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


def panel_metro_user():
    while True:
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
            password = "Pedram$Karimi0020"  # input("Enter password: ")
            if metro_user_instance.check_credentials_User(username, password) == True:
                while True:
                    print("\nEnter your choice\n1.Show tickets\n2.sing out\n")
                    choice = input("Enter your choice: \n")
                    if choice == "1":
                        while True:
                            if choice == "1":
                                while True:
                                    print("\n1.show a one-way ticket\n"
                                          "2.show multi way ticket\n"
                                          "3.show a multi way ticket with an expiration date\n4.Show all\n5.sing out\n")
                                    choice = input("\nEnter your choice: ")
                                    if choice == "1":
                                        single_ticket = show_tickets_info.single_tickets
                                        print(single_ticket)
                                        print("\nEnter your choice\n1.Buy\n2.sing out\n")
                                        choice = input("Enter your choice: \n")
                                        if choice == "1":
                                            print("\nEnter your choice\n1.Purchase from bank account\n"
                                                  "2.Create a bank account\n3.sing out\n")
                                            choice = input("Enter your choice: \n")
                                            if choice == "1":
                                                print("\n**Please Enter username and password**\n")
                                                username = input("Enter username: ")
                                                password = input("Enter password: ")
                                                if bank_user_instance.check_credentials_User_Bank(username,
                                                                                                  password) == True:
                                                    input_tkicket = input("Enter origin for Single Trip Ticket: ")
                                                    for ticket in single_ticket:
                                                        if input_tkicket == ticket:
                                                            price_ticket = show_tickets_info.show_price(input_tkicket)
                                                            amount_withdraw = price_ticket
                                                            bank_user_instance.withdraw(amount_withdraw)
                                                            show_money_info.show_money(username)
                                                            search_bank = show_money_info.UserMoneyBalance
                                                            buy = int(search_bank[1]) - price_ticket
                                                            print(f"Your purchase was successful and Your account "
                                                                  f"balance {buy}")
                                                        else:
                                                            cowsay.tux("Invalid choice. Please Enter "
                                                                       "name origin ticket")


                                            elif choice == "2":
                                                name = input("Enter your name: ")
                                                lastname = input("Enter your lastname: ")
                                                age = input("Enter your age: ")
                                                national_code = input("Enter your national code: ")
                                                phone = input("Enter your phone: ")
                                                address = input("Enter your address: ")
                                                bank_user_instance.Add_Information_User_Bank(name, lastname, age, phone,
                                                                                             address, national_code)
                                            elif choice == "3":
                                                print("exit in panel Buy one-way ticket\n")
                                                break
                                            else:
                                                cowsay.tux("Invalid choice. Please Enter your "
                                                           "1.Buy 2.sing out")
                                        elif choice == "2":
                                            print("exit in panel Buy one-way ticket\n")
                                            break
                                        else:
                                            cowsay.tux("Invalid choice. Please Enter your "
                                                       "1.Buy 2.sing out")
                                    elif choice == "2":
                                        multi_ticket = show_tickets_info.multi_stop_tickets
                                        print(multi_ticket)
                                        print("\nEnter your choice\n1.Buy\n2.sing out\n")
                                        choice = input("Enter your choice: \n")
                                        if choice == "1":
                                            print("\nEnter your choice\n1.Purchase from bank account\n"
                                                  "2.Create a bank account\n3.sing out\n")
                                            choice = input("Enter your choice: \n")
                                            if choice == "1":
                                                print("\n**Please Enter username and password**\n")
                                                username = input("Enter username: ")
                                                password = input("Enter password: ")
                                                if bank_user_instance.check_credentials_User_Bank(username,
                                                                                                  password) == True:

                                                    input_tkicket = input("Enter origin for Single Trip Ticket: ")
                                                    for ticket in multi_ticket:
                                                        if input_tkicket == ticket:
                                                            price_ticket = show_tickets_info.show_price(input_tkicket)
                                                            amount_withdraw = price_ticket
                                                            bank_user_instance.withdraw(amount_withdraw)
                                                            show_money_info.show_money(username)
                                                            search_bank = show_money_info.UserMoneyBalance
                                                            buy = int(search_bank[1]) - price_ticket
                                                            print(f"Your purchase was successful and Your account "
                                                                  f"balance {buy}")
                                                        else:
                                                            cowsay.tux("Invalid choice. Please Enter "
                                                                       "name origin ticket")
                                        elif choice == "2":
                                            print("exit in panel Buy multi way ticket\n")
                                            break
                                        else:
                                            cowsay.tux("Invalid choice. Please Enter your "
                                                       "1.Buy 2.sing out")

                                    elif choice == "3":
                                        flexible_ticket = show_tickets_info.flexible_tickets
                                        print(flexible_ticket)
                                        print("\nEnter your choice\n1.Buy\n2.sing out\n")
                                        choice = input("Enter your choice: \n")
                                        if choice == "1":
                                            print("\nEnter your choice\n1.Purchase from bank account\n"
                                                  "2.Create a bank account\n3.sing out\n")
                                            choice = input("Enter your choice: \n")
                                            if choice == "1":
                                                print("\n**Please Enter username and password**\n")
                                                username = input("Enter username: ")
                                                password = input("Enter password: ")
                                                if bank_user_instance.check_credentials_User_Bank(username,
                                                                                                  password) == True:
                                                    input_tkicket = input("Enter origin for Single Trip Ticket: ")
                                                    for ticket in flexible_ticket:
                                                        if input_tkicket == ticket:
                                                            price_ticket = show_tickets_info.show_price(input_tkicket)
                                                            amount_withdraw = price_ticket
                                                            bank_user_instance.withdraw(amount_withdraw)
                                                            show_money_info.show_money(username)
                                                            search_bank = show_money_info.UserMoneyBalance
                                                            buy = int(search_bank[1]) - price_ticket
                                                            print(f"Your purchase was successful and Your account "
                                                                  f"balance {buy}")
                                                        else:
                                                            cowsay.tux("Invalid choice. Please Enter "
                                                                       "name origin ticket")
                                        elif choice == "2":
                                            print("exit in panel Buy multi way ticket "
                                                  "with an expiration date\n")
                                            break
                                        else:
                                            cowsay.tux("Invalid choice. Please Enter your "
                                                       "1.Buy 2.sing out")
                                    elif choice == "4":
                                        single_ticket = show_tickets_info.single_tickets
                                        multi_ticket = show_tickets_info.multi_stop_tickets
                                        flexible_ticket = show_tickets_info.flexible_tickets
                                        print(f'\nsingle ticket:\n{single_ticket}\nmulti ticket:\n'
                                              f'{multi_ticket}\nflexible ticket:\n{flexible_ticket}\n')
                                    elif choice == "5":
                                        print("exit in panel Show ticket\n")
                                        break
                                    else:
                                        cowsay.tux("Invalid choice. Please Enter your "
                                                   "choice 1.show a one-way ticket "
                                                   "2.show multi-way ticket 3.show a multi-way"
                                                   " ticket with an expiration date"
                                                   " 4.Show all 5.sing out")
                            elif choice == "2":
                                print("exit in panel User\n")
                                break
                            else:
                                cowsay.tux("Invalid choice. Please Enter your choice"
                                           "1.Show tickets 2.sing out")
                    elif choice == "2":
                        print("exit in panel User\n")
                        break
                    else:
                        cowsay.tux("Invalid choice. Please Enter your choice 1.Show tickets"
                                   " or sing out")
        elif choice == "3":
            print("exit in panel User\n")
            break
        else:
            cowsay.tux("\nInvalid choice. Please Enter your choice login or sing up or sing out.\n")


def panel_metro_admin():
    # elif choice == "2":
    while True:
        print("\nEnter your choice\n1.login\n2.sing out\n")
        choice = input("Enter your choice: \n")
        if choice == "1":
            print("**\nPlease Enter username and password**\n")
            username = "Pedram.9060@gmail.com"  # input("Enter username: ")
            password = "Pedram$Karimi0020"  # input("Enter password: ")
            if metro_admin_instance.check_credentials(username, password) == True:
                pickle_data.pickle_metro_admin_username_password()
                while True:
                    print("\nEnter your choice\n1.Create ticket\n2.Show ticket\n"
                          "3.exit in panel Metro ticket")
                    choice = input("Enter your choice: \n")
                    if choice == "1":
                        while True:
                            print(
                                "\nEnter your choice\n1.Create a one-way ticket\n"
                                "2.Create multi-way ticket\n"
                                "3.Create a multi-way ticket with an expiration date\n4.sing out\n")
                            choice = input("Enter your choice: \n")
                            if choice == "1":
                                price = input("Enter price for Single Trip Ticket: ")
                                origin = input("Enter origin for Single Trip Ticket: ")
                                destination = input("Enter destination for Single Trip Ticket: ")
                                date = datetime.now().strftime('%Y-%m-%d')

                                try:
                                    price = float(price)
                                except ValueError as e:
                                    raise TicketError(f"Invalid input: {e}")
                                attributes = TicketAttributes(price=price, origin=origin,
                                                              destination=destination,
                                                              expiration_date='2026-10-10')
                                try:
                                    single_ticket = SingleTripTicket(attributes=attributes)
                                except TicketError as e:
                                    print(f"Error creating Single Trip Ticket: {e}")
                                else:
                                    print(f"Single Trip Ticket - {single_ticket}")
                                show_tickets_info.show_single_trip_ticket(price, origin, destination, date)
                            elif choice == "2":
                                price = input("Enter price for Multi-Stop Ticket: ")
                                origin = input("Enter origin for Multi-Stop Ticket: ")
                                destination = input("Enter destination for Multi-Stop Ticket: ")
                                date = datetime.now().strftime('%Y-%m-%d')
                                multi_ticket_attributes = TicketAttributes(price=price, origin=origin,
                                                                           destination=destination,
                                                                           expiration_date='2026-10-10')

                                try:
                                    multi_ticket_attributes.price = float(multi_ticket_attributes.price)
                                except ValueError as e:
                                    raise TicketError(f"Invalid input: {e}")

                                try:
                                    multi_ticket = MultiStopTicket(attributes=multi_ticket_attributes)
                                except TicketError as e:
                                    print(f"Error creating Multi-Stop Ticket: {e}")
                                else:
                                    print(f"Multi-Stop Ticket - {multi_ticket}")
                                show_tickets_info.show_multi_stop_ticket(price, origin, destination, date)
                            elif choice == "3":
                                price = input("Enter price for Flexible Ticket: ")
                                origin = input("Enter origin for Flexible Ticket: ")
                                destination = input("Enter destination for Flexible Ticket: ")
                                date = datetime.now().strftime('%Y-%m-%d')
                                expiration_date_input = input(
                                    "Enter expiration date for Flexible Ticket (YYYY-MM-DD): ")
                                flexible_ticket_attributes = TicketAttributes(price=price, origin=origin,
                                                                              destination=destination,
                                                                              expiration_date=expiration_date_input)

                                try:
                                    flexible_ticket_attributes.price = float(
                                        flexible_ticket_attributes.price)
                                except ValueError as e:
                                    raise TicketError(f"Invalid input: {e}")

                                # Set the expiration_date directly
                                flexible_ticket_attributes.expiration_date = datetime.strptime(
                                    expiration_date_input,
                                    "%Y-%m-%d").strftime(
                                    '%Y-%m-%d %H:00:00')

                                try:
                                    flexible_ticket = FlexibleTicket(attributes=flexible_ticket_attributes)
                                except TicketError as e:
                                    print(f"Error creating Flexible Ticket: {e}")
                                else:
                                    print(f"Flexible Ticket - {flexible_ticket}")
                                show_tickets_info.show_flexible_ticket(price, origin, destination, date,
                                                                       expiration_date_input)
                            elif choice == "4":
                                print("exit in panel Create tickets\n")
                                break
                            else:
                                cowsay.tux("\nInvalid choice. Please Enter your choice 1.Create a one-way ticket "
                                           "2.Create multi-way ticket "
                                           "3.Create a multi-way ticket with an expiration date 4.sing out\n")
                    elif choice == "2":
                        while True:
                            print("\n1.show a one-way ticket\n"
                                  "2.show multi-way ticket\n"
                                  "3.show a multi-way ticket with an expiration date\n4.Show all\n5.sing out\n")
                            choice = input("\nEnter your choice: ")
                            if choice == "1":
                                single_ticket = show_tickets_info.single_tickets
                                print(single_ticket)
                            elif choice == "2":
                                multi_ticket = show_tickets_info.multi_stop_tickets
                                print(multi_ticket)
                            elif choice == "3":
                                flexible_ticket = show_tickets_info.flexible_tickets
                                print(flexible_ticket)
                            elif choice == "4":
                                single_ticket = show_tickets_info.single_tickets
                                multi_ticket = show_tickets_info.multi_stop_tickets
                                flexible_ticket = show_tickets_info.flexible_tickets
                                print(f'\nsingle ticket:\n{single_ticket}\nmulti ticket:\n'
                                      f'{multi_ticket}\nflexible ticket:\n{flexible_ticket}\n')
                            elif choice == "5":
                                print("exit in panel Show ticket\n")
                                break
                            else:
                                cowsay.tux("\nInvalid choice. Please Enter your choice 1.show a one-way ticket "
                                           "2.show multi-way ticket "
                                           "3.show a multi-way ticket with an "
                                           "expiration date 4.Show all 5.sing out\n")
                    elif choice == "3":
                        print("exit in panel Metro ticket\n")
                        break
                    else:
                        cowsay.tux("\nInvalid choice. Please Enter your choice Creat ticket or "
                                   "Show ticket  or exit in panel Metro ticket.\n")
        elif choice == "2":
            print("exit in panel Admin\n")
            break
        else:
            cowsay.tux("\nInvalid choice. Please Enter your choice login or sing up or sing out.\n")
