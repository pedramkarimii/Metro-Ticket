# Metro-Ticket 

## Overview
The Metro-Ticket project is a Python-based console application designed to manage both bank accounts and metro ticketing systems. The application allows users to create and manage bank accounts, deposit and withdraw funds, and purchase metro tickets using their bank balance. It also provides an admin panel for managing user accounts and tickets.

## Features

### Bank Account Management
- **User Panel**:
  - Create a new bank account.
  - Login to an existing bank account.
  - Deposit funds into the account.
  - Withdraw funds from the account.
  - View account balance.

- **Admin Panel**:
  - Login as an admin.
  - View all user accounts.
  - Search for a specific user account by username.

### Metro Ticket Management
- **User Panel**:
  - Sign up for a metro account.
  - Login to an existing metro account.
  - View available tickets (single trip, multi-stop, flexible tickets).
  - Purchase tickets using bank account funds.

- **Admin Panel**:
  - Login as an admin.
  - Create new tickets (single trip, multi-stop, flexible tickets).
  - View all available tickets.

## Project Structure

### Modules
- **admin_bank.py**: Contains `AdminBank` class for managing bank admin functionalities.
- **admin_metro.py**: Contains `AdminMetro` class for managing metro admin functionalities.
- **user_bank.py**: Contains `UserBank` class for managing user bank functionalities.
- **user_metro.py**: Contains `UserMetro` class for managing user metro functionalities.
- **pickle.py**: Contains `PickleData` class for handling data serialization.
- **show_money_bank.py**: Contains `ShowMoneyInfo` class for displaying bank account information.
- **ticket_metro.py**: Contains classes and functions for managing metro tickets.

### Panels
- **panel_bank.py**:
  - `panel_bank_user()`: User interface for bank account management.
  - `panel_bank_login()`: Admin interface for bank account management.

- **panel_metro.py**:
  - `panel_metro_user()`: User interface for metro ticket management.
  - `panel_metro_admin()`: Admin interface for metro ticket management.

### Main Program
- **main.py**: Main entry point for the application, providing the main menu and navigating to different panels.

## Usage

### Running the Application
To run the application, execute the `main.py` file:

```
python main.py
```
## Main Menu
### Upon running the application, you will be greeted with the main menu:

```
Welcome to my project

Enter a number Options
Metro or Bank?
1. Metro
2. Bank Account
3. Exit
```

## Metro Panel
### If you select the Metro option, you will be asked whether you are a user or an admin:

```
Welcome to the Metro
Enter a number Options

You are an admin or user?
1. User
2. Admin
3. sing out
```
### User
- **Sign Up**: Register a new metro account.
- **Login**: Access an existing metro account.
- **Show Tickets**: View available tickets.
- **Buy Tickets**: Purchase tickets using a bank account.

### Admin
- **Create Tickets**: Create new tickets (single trip, multi-stop, flexible).
- **Show Tickets**: View all available tickets.


## Bank Account Panel
###  If you select the Bank Account option, you will be asked whether you are a user or an admin:

```Welcome to the Bank
Enter a number Options

You are an admin or user?
1. User
2. Admin
3. sing out
```
### User Panel (Bank)
- **Create Account**: Register a new bank account.
- **Login**: Access an existing bank account.
- **Deposit**: Add funds to the account.
- **Withdraw**: Remove funds from the account.
- **View Balance**: Check the current balance.

### Admin Panel (Bank)
- **View All Accounts**: Display information for all user accounts.
- **Search Account**: Search for a specific user account.


## Exiting the Application
### To exit the application, select the "Exit" option from the main menu.
## Dependencies :
 - cowsay: Used for displaying messages with ASCII art.
 - datetime: Used for handling date and time in ticket creation.
### Install the dependencies using pip:
```
pip install cowsay
```
## Error Handling
###  The application includes basic error handling to manage invalid inputs and other exceptions. If an error occurs, a message will be displayed, and the user will be prompted to try again.
## Conclusion
### The Metro-Ticket project is a simple yet comprehensive application for managing bank accounts and metro ticketing systems. It provides both user and admin interfaces for a seamless experience. This project can be further extended with additional features and improved error handling as needed.

