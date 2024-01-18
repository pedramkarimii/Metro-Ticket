from transactionProcessor import TransactionProcessor


class ShowMoney(TransactionProcessor):
    def __init__(self):
        """Call the constructor of the parent class (Bank)"""
        super().__init__()
        self.UserMoneyDeposit = []
        self.UserMoneyWithdraw = []
        self.UserMoneyFee = []
        self.UserMoneyBalance = []

        """Dictionary to store all financial information for each user."""

        self.AllMoney = {}

    """Method to display money-related information for a given user"""

    def show_money(self, name):
        deposit_info_deposit = self.MoneyInfo[1]
        self.UserMoneyDeposit.extend(["deposit", deposit_info_deposit])
        print(f"{name}: {self.UserMoneyDeposit}")
        self.UserMoneyDeposit.clear()

        withdraw_info = self.MoneyInfo[3]
        self.UserMoneyWithdraw.extend(["withdraw", withdraw_info])
        print(f"{name}: {self.UserMoneyWithdraw}")
        self.UserMoneyWithdraw.clear()

        fee_info = self.MoneyInfo[5]
        self.UserMoneyFee.extend(["fee", fee_info])
        print(f"{name}: {self.UserMoneyFee}")
        self.UserMoneyFee.clear()

        balance_info = self.MoneyInfo[7]
        self.UserMoneyBalance.extend(["balance", balance_info])
        print(f"{name}: {self.UserMoneyBalance}")
        self.AllMoney[name] = {"deposit": deposit_info_deposit[0:4], "withdraw": withdraw_info[0:4],
                               "fee": fee_info[0:4], "balance": balance_info[0:4]}
        self.UserMoneyBalance.clear()


class ShowMoneyInfo(ShowMoney):
    pass
