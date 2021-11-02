import unittest
from Account import Account, WithdrawalResult

class AccountTests(unittest.TestCase):
    def test_withdrawal_with_too_much_amount_returns_error(self):
        target = Account("12345")
        belopp = target.getSaldo()
        result = target.withdraw(100)
        self.assertEqual(WithdrawalResult.NotEnoughSaldo, result)
        self.assertEqual(belopp, target.getSaldo())

if __name__ == "__main__":
    unittest.main()