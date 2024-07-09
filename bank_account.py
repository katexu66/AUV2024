"""
The account should have a balance, a name and an account number.
The account should have a method to withdraw money.
The account should have a method to deposit money.
The account should have a method to print the current balance.
"""


class bank:
    def __init__(self, name, accountNumber):
        self.balance = 0
        self.name = name
        self.accountNumber = accountNumber

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return

    def deposit(self, amount):
        self.balance = self.balance + amount
        return

    def current_balance(self):
        print("Current balance: " + str(self.balance))
        return "Current balance: " + str(self.balance)
