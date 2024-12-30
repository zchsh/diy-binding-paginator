import unittest

from get_folios import getFolios

class TestGetFolios(unittest.TestCase):
    # Test that a signaturePageCount not divisible by 4 returns nil
    def test_invalid_page_count(self):
        result = getFolios(5)
        self.assertEqual(result, None)

    # Assert that a signaturePageCount of 4 returns a single folio
    def test_page_count_4(self):
        result = getFolios(4)
        self.assertEqual(result, [
          [[3, 0], [1, 2]]
        ])
    
    # Assert that a signaturePageCount of 8 returns two folios
    def test_page_count_8(self):
        result = getFolios(8)
        self.assertEqual(result, [
          [[7, 0], [1, 6]],
          [[5, 2], [3, 4]]
        ])

    # Assert that a signaturePageCount of 12 returns three folios
    def test_page_count_12(self):
        result = getFolios(12)
        self.assertEqual(result, [
          [[11, 0], [1, 10]],
          [[9, 2], [3, 8]],
          [[7, 4], [5, 6]]
        ])

    # Assert that a signaturePageCount of 16 returns four folios
    def test_page_count_16(self):
        result = getFolios(16)
        self.assertEqual(result, [
          [[15, 0], [1, 14]],
          [[13, 2], [3, 12]],
          [[11, 4], [5, 10]],
          [[9, 6], [7, 8],]
        ])


if __name__ == '__main__':
    unittest.main()