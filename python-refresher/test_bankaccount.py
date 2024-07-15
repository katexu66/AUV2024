import unittest
import bank_account


class TestBankAccount(unittest.TestCase):
    def setUp(self): # set up runs before every test
        self.bank = bank_account.bank("Kate", 123) # self makes it exist in stack memory (as opposed to heap)
   
    def test_creation(self):
        self.assertEqual(self.bank.balance, 0)
        self.assertEqual(self.bank.name, "Kate")
        self.assertEqual(self.bank.accountNumber, 123)

    def test_withdraw(self):
        self.bank.deposit(150)
        self.bank.withdraw(100)
        self.assertEqual(self.bank.balance, 50)
        self.assertEqual(self.bank.name, "Kate")
        self.assertEqual(self.bank.accountNumber, 123)
        self.assertEqual(self.bank.withdraw(-50), "Cannot withdraw negative amount from bank account.")
        self.assertEqual(self.bank.withdraw(55), "Cannot withdraw more than your current balance.")

    def test_deposit(self):
        self.bank.deposit(100)
        self.assertEqual(self.bank.balance, 100)
        self.assertEqual(self.bank.name, "Kate")
        self.assertEqual(self.bank.accountNumber, 123)
        self.assertEqual(self.bank.deposit(-50), "Cannot deposit negative amount from bank account.")

    def test_current_balance(self):
        self.assertEqual(self.bank.current_balance(), "Current balance: 0")
        self.bank.deposit(20)
        self.assertEqual(self.bank.current_balance(), "Current balance: 20")
