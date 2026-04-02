import unittest
from find_all_indices import index_all

class TestFindAllIndices(unittest.TestCase):

    def test_example_from_file(self):
        # The example provided in the source file
        example = [[[1, 2, 3], 2, [1, 3]], 2, [1, 2, 3]]
        target = 2
        expected = [[0, 0, 1], [0, 1], [1], [2, 1]]
        self.assertEqual(index_all(example, target), expected)

    def test_flat_list(self):
        data = [1, 2, 3, 2, 4, 2]
        target = 2
        expected = [[1], [3], [5]]
        self.assertEqual(index_all(data, target), expected)

    def test_target_not_found(self):
        data = [1, 3, 5, [7, 9, [11]]]
        target = 2
        expected = []
        self.assertEqual(index_all(data, target), expected)

    def test_empty_list(self):
        data = []
        target = 10
        expected = []
        self.assertEqual(index_all(data, target), expected)
        
    def test_deeply_nested_list(self):
        data = [[[[[5]]]]]
        target = 5
        expected = [[0, 0, 0, 0, 0]]
        self.assertEqual(index_all(data, target), expected)

    def test_strings(self):
        data = ["apple", "banana", ["cherry", "apple", "date"], "apple"]
        target = "apple"
        expected = [[0], [2, 1], [3]]
        self.assertEqual(index_all(data, target), expected)

    def test_mixed_types(self):
        data = [1, "two", [3, "two", 4.0], 4.0, [[1, "two"]]]
        target = "two"
        expected = [[1], [2, 1], [4, 0, 1]]
        self.assertEqual(index_all(data, target), expected)

    def test_target_is_list(self):
        data = [[1, 2], [3, 4], [1, 2], [[1, 2], 5]]
        target = [1, 2]
        # Depending on how `val == target` works, [1, 2] could be matched as a whole element.
        # However, `index_all` goes into `isinstance(val, list)` for inner elements too?
        # Let's see: `val == target` is evaluated first. If it's true, it's added.
        # But wait, in the function `elif isinstance(val, list)` only happens IF it didn't match.
        expected = [[0], [2], [3, 0]]
        self.assertEqual(index_all(data, target), expected)

if __name__ == "__main__":
    unittest.main()
