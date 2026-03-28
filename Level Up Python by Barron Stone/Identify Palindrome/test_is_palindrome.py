import unittest
from is_palidrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_hello_world(self):
        self.assertFalse(is_palindrome("Hello world"))
        
    def test_salami_lasagna_hog(self):
        self.assertTrue(is_palindrome("Go hang a salami - I'm a lasagna hog"))
        
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))
        
    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        
    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        
    def test_numbers_only(self):
        # The function discards non-alphabet characters. "123" -> "" -> True
        self.assertTrue(is_palindrome("123"))
        
    def test_mixed_alphanumeric_palindrome(self):
        # "radar 1" -> "radar" -> True
        self.assertTrue(is_palindrome("radar 1"))
        
    def test_mixed_alphanumeric_non_palindrome(self):
        # "radars 1" -> "radars" -> False
        self.assertFalse(is_palindrome("radars 1"))
        
    def test_special_characters_only(self):
        # "!@#$" -> "" -> True
        self.assertTrue(is_palindrome("!@#$"))

if __name__ == '__main__':
    unittest.main()
