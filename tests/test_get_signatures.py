import unittest

from get_signatures import getSignatures

class TestDetermineSignaturs(unittest.TestCase):
    # Test that when pageCount is not divisible by 4, we get None
    def test_invalid_page_count(self):
        result = getSignatures(5)
        self.assertEqual(result, None)

    # Test pageCount that should yield single signatures
    def test_page_counts_single_signatures(self):
        self.assertEqual(getSignatures(4), [4])
        self.assertEqual(getSignatures(8), [8])
        self.assertEqual(getSignatures(12), [12])
        self.assertEqual(getSignatures(16), [16])

    # Test pageCounts for a bunch of other values.
    # Maybe a bit silly, but feels fine to be exhaustive in a silly way.
    def test_page_count_20(self):
        self.assertEqual(getSignatures(20), [12, 8])
    def test_page_count_24(self):
        self.assertEqual(getSignatures(24), [12, 12])
    def test_page_count_28(self):
        self.assertEqual(getSignatures(28), [16, 12])
    def test_page_count_32(self):
        self.assertEqual(getSignatures(32), [16, 16])
    def test_page_count_36(self):
        self.assertEqual(getSignatures(36), [12, 12, 12])
    def test_page_count_40(self):
        self.assertEqual(getSignatures(40), [16, 12, 12])
    def test_page_count_44(self):
        self.assertEqual(getSignatures(44), [16, 16, 12])
    def test_page_count_48(self):
        self.assertEqual(getSignatures(48), [16, 16, 16])
    def test_page_count_52(self):
        self.assertEqual(getSignatures(52), [16, 12, 12, 12])
    def test_page_count_56(self):
        self.assertEqual(getSignatures(56), [16, 16, 12, 12])
    def test_page_count_60(self):
        self.assertEqual(getSignatures(60), [16, 16, 16, 12])
    def test_page_count_64(self):
        self.assertEqual(getSignatures(64), [16, 16, 16, 16])
    def test_page_count_72(self):
        self.assertEqual(getSignatures(72), [16, 16, 16, 12, 12])
    def test_page_count_96(self):
        self.assertEqual(getSignatures(96), [16, 16, 16, 16, 16, 16])
    def test_page_count_144(self):
        self.assertEqual(
          getSignatures(144),
          [16, 16, 16, 16, 16, 16, 16, 16, 16]
        )
    def test_page_count_200(self):
        self.assertEqual(
          getSignatures(200),
          [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 12, 12]
        )
    def test_page_count_256(self):
        self.assertEqual(
          getSignatures(256),
          [16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16]
        )
    
if __name__ == '__main__':
    unittest.main()