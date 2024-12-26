import unittest

from offset_page_numbers import offsetPageNumbers

class TestOffsetPageNumbers(unittest.TestCase):
    # Test that an empty guide returns unchanged
    def test_empty_guide(self):
        result = offsetPageNumbers([[[], []]], 1)
        self.assertEqual(result, [[[], []]])
    
    # Test that offset zero returns the guide unchanged
    def test_zero_offset(self):
        result = offsetPageNumbers([[[1, 2], [3, 0]]], 0)
        self.assertEqual(result, [[[1, 2], [3, 0]]])

    # Test that a positive offset functions as expected
    def test_positive_offset(self):
        result = offsetPageNumbers([
          [[1, 10], [11, 0]],
          [[3, 8], [9, 2]],
          [[5, 6], [7, 4]]
        ], 10)
        self.assertEqual(result, [
          [[11, 20], [21, 10]],
          [[13, 18], [19, 12]],
          [[15, 16], [17, 14]]
        ])

    # Test that a negative offset functions as expected
    def test_negative_offset(self):
        result = offsetPageNumbers([[[2, 3], [4, 1]]], -1)
        self.assertEqual(result, [[[1, 2], [3, 0]]])

if __name__ == '__main__':
    unittest.main()