import unittest
from sort_string import sort_string

class TestSortString(unittest.TestCase):
    def test_course_example(self):
        # Standard example cases for case-insensitive sort
        self.assertEqual(sort_string("String of words"), "of String words")
        self.assertEqual(sort_string("banana ORANGE apple"), "apple banana ORANGE")

    def test_mixed_case(self):
        self.assertEqual(sort_string("Zebra apple Boy"), "apple Boy Zebra")

    def test_all_lowercase(self):
        self.assertEqual(sort_string("dog cat bird"), "bird cat dog")

    def test_all_uppercase(self):
        self.assertEqual(sort_string("DOG CAT BIRD"), "BIRD CAT DOG")

    def test_single_word(self):
        self.assertEqual(sort_string("hello"), "hello")

    def test_empty_string(self):
        self.assertEqual(sort_string(""), "")

if __name__ == '__main__':
    unittest.main()
