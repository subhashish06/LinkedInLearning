import unittest
from prime_factors import find_prime_factors


class TestPrimeFactors(unittest.TestCase):
    def test_negative_number(self):
        """Test negative integers return the error message."""
        self.assertEqual(find_prime_factors(-5), "Enter only positive integers")

    def test_zero(self):
        """Test zero returns the error message."""
        self.assertEqual(find_prime_factors(0), "Enter only positive integers")

    def test_one(self):
        """Test 1 returns the specific corner case result [1]."""
        self.assertEqual(find_prime_factors(1), {1})

    def test_prime_number(self):
        """Test prime numbers return a set containing only themselves."""
        self.assertEqual(find_prime_factors(2), {2})
        self.assertEqual(find_prime_factors(3), {3})
        self.assertEqual(find_prime_factors(97), {97})

    def test_composite_number_duplicate_factors(self):
        """Test composite numbers with duplicate prime factors return a set of unique factors."""
        # 4 = 2 * 2
        self.assertEqual(find_prime_factors(4), {2})
        # 27 = 3 * 3 * 3
        self.assertEqual(find_prime_factors(27), {3})

    def test_composite_number_distinct_factors(self):
        """Test composite numbers with multiple distinct prime factors."""
        # 6 = 2 * 3
        self.assertEqual(find_prime_factors(6), {2, 3})
        # 60 = 2 * 2 * 3 * 5
        self.assertEqual(find_prime_factors(60), {2, 3, 5})
        # 210 = 2 * 3 * 5 * 7
        self.assertEqual(find_prime_factors(210), {2, 3, 5, 7})

    def test_large_composite(self):
        """Test larger composite numbers."""
        # 9409 = 97 * 97
        self.assertEqual(find_prime_factors(9409), {97})

if __name__ == '__main__':
    unittest.main()
