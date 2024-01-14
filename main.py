from admin import Admin


def main():
    password_admin = Admin()
    while True:
        choice = input("Enter '1' to add username and password, '2' to check credentials, or 'q' to quit: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                password_admin.add_password_username(username, password)
                print("Username and password added successfully.")
            except ValueError as e:
                print(e)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            password_admin.check_credentials(username, password)
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
