import unittest

from password.tools import StrengthMeter

WEAK = [
    "AAAAAA",
    "aaaaaa",
    "123456"
]

STRONG = [
    "@d8l*7kUH5VtIt@V41v5NairbceFGgnOA#KN",
    "@d8l*7kUH5VtIt@V41v5NairbceFGgnOA#KN!?523"
]


class ValidStrengthMeterTestCase(unittest.TestCase):
    def test_weak_password(self):
        for pw in WEAK:
            result = StrengthMeter(pw).strength
            self.assertEqual(result, 'Weak password')

    def test_medium_password(self):
        result = StrengthMeter('Tester12').strength
        self.assertEqual(result, 'Medium password')

    def test_strong_password(self):
        for pw in STRONG:
            result = StrengthMeter(pw).strength
            self.assertEqual(result, 'Strong password')
