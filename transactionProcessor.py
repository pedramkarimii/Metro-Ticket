from Exceptions import InsufficientFundsError


class TransactionProcessor:
    MoneyInfo = []
    DepositMoney = []

    def process_deposit(self, account, amount):
        try:
            amount = float(amount)
            if amount > 0:
                account.balance += amount
                deposit_ = account.balance
                self.MoneyInfo.extend(str("deposit").split())
                self.MoneyInfo.extend(str(deposit_).split())
                self.DepositMoney.extend(str(deposit_).split())
                print(f"Deposited ${amount}. Current balance: ${account.balance}")
            else:
                print("Invalid deposit amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input for deposit. Please enter a valid numeric value.")

    def process_withdrawal(self, account, amount):
        try:
            amount = float(amount)
            if amount > 0:
                withdrawal_fee = account.calculate_withdrawal_fee(amount)
                total_withdrawal = amount + withdrawal_fee

                self.MoneyInfo.extend(str("fee").split())
                self.MoneyInfo.extend(str(withdrawal_fee).split())
                self.MoneyInfo.extend(str("withdrawal").split())
                self.MoneyInfo.extend(str(amount).split())
                deposit = float(self.DepositMoney[0])
                if total_withdrawal <= deposit:
                    deposit -= total_withdrawal
                    withdrawal_ = deposit
                    self.MoneyInfo.extend(str("Balance").split())
                    self.MoneyInfo.extend(str(withdrawal_).split())
                    print(
                        f"Withdrew ${amount} with a withdrawal fee of"
                        f" ${withdrawal_fee}. Current balance: ${account.balance}")
                else:
                    raise InsufficientFundsError("Insufficient funds.")
            else:
                print("Invalid withdrawal amount. Please enter a positive value.")
        except ValueError:
            print("Invalid input for withdrawal. Please enter a valid numeric value.")
        except InsufficientFundsError as e:
            print(f"Error: {e}")

    def __str__(self):
        pass
