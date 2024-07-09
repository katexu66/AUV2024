import unittest
import bank_account


class TestBankAccount(unittest.TestCase):
    def test_creation(self):
        bank = bank_account.bank("Kate", 123)
        self.assertEqual(bank.balance, 0)
        self.assertEqual(bank.name, "Kate")
        self.assertEqual(bank.accountNumber, 123)

    def test_withdraw(self):
        bank = bank_account.bank("Kate", 123)
        bank.deposit(150)
        bank.withdraw(100)
        self.assertEqual(bank.balance, 50)
        self.assertEqual(bank.name, "Kate")
        self.assertEqual(bank.accountNumber, 123)

    def test_deposit(self):
        bank = bank_account.bank("Kate", 123)
        bank.deposit(100)
        self.assertEqual(bank.balance, 100)
        self.assertEqual(bank.name, "Kate")
        self.assertEqual(bank.accountNumber, 123)

    def test_current_balance(self):
        bank = bank_account.bank("Kate", 123)
        self.assertEqual(bank.current_balance(), "Current balance: 0")
        bank.deposit(20)
        self.assertEqual(bank.current_balance(), "Current balance: 20")
