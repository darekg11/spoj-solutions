import unittest
import main

class GCD_Tests(unittest.TestCase):
    def test_gcd_for_15_9(self):
        self.assertEqual(main.greatest_common_divisor(15, 9), 3)
    def test_gcd_for_120_4(self):
        self.assertEqual(main.greatest_common_divisor(120, 4), 4)
    def test_gcd_for_121_21(self):
        self.assertEqual(main.greatest_common_divisor(121, 21), 1)

class LCM_Tests(unittest.TestCase):
    def test_lcm_12_15(self):
        self.assertEqual(main.least_common_multiple(12, 15), 60)
    def test_lcm_11_22(self):
        self.assertEqual(main.least_common_multiple(11, 22), 22)


if __name__ == '__main__':
    unittest.main()