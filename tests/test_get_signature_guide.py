import unittest

from get_signature_guide import getSignatureGuide

class TestGetSignatureGuide(unittest.TestCase):
    # Test that a pageCount not divisible by 4 returns nil
    def test_invalid_page_count(self):
        result = getSignatureGuide(5)
        self.assertEqual(result, None)

    # Assert that a pageCount of 4 returns a single folio
    def test_page_count_4(self):
        result = getSignatureGuide(4)
        self.assertEqual(result, [
          [[1, 2], [3, 0]]
        ])
    
    # Assert that a pageCount of 8 returns two folios
    def test_page_count_8(self):
        result = getSignatureGuide(8)
        self.assertEqual(result, [
          [[1, 6], [7, 0]],
          [[3, 4], [5, 2]]
        ])

    # Assert that a pageCount of 12 returns three folios
    def test_page_count_12(self):
        result = getSignatureGuide(12)
        self.assertEqual(result, [
          [[1, 10], [11, 0]],
          [[3, 8], [9, 2]],
          [[5, 6], [7, 4]]
        ])

    # Assert that a pageCount of 16 returns four folios
    def test_page_count_16(self):
        result = getSignatureGuide(16)
        self.assertEqual(result, [
          [[1, 14], [15, 0]],
          [[3, 12], [13, 2]],
          [[5, 10], [11, 4]],
          [[7, 8], [9, 6]]
        ])


if __name__ == '__main__':
    unittest.main()