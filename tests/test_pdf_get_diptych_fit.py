import unittest

from pdf_get_diptych_fit import pdfGetDiptychFit

class TestPdfGetDiptychFit(unittest.TestCase):
    # Test that a larger page doesn't fit within a smaller target area.
    def test_page_too_large(self):
        pageSize = {"width": 100, "height": 100}
        targetArea = {"width": 50, "height": 50}
        result = pdfGetDiptychFit(pageSize, targetArea)
        self.assertEqual(result, [None, None, None, None])

    # Test that a page fits exactly within an area double the size
    def test_page_just_right(self):        
        pageSize = {"width": 50, "height": 100}
        targetArea = {"width": 100, "height": 100}
        result = pdfGetDiptychFit(pageSize, targetArea)
        self.assertEqual(result, [0, 0, 50, 0])

    # Test that a page fits exactly within an area double the size
    def test_small_page_centered(self):        
        pageSize = {"width": 60, "height": 40}
        targetArea = {"width": 200, "height": 100}
        result = pdfGetDiptychFit(pageSize, targetArea)
        self.assertEqual(result, [40, 30, 100, 30])
    
    # Test that a page fits exactly within an area double the size
    def test_small_page_centered_with_spacing(self):        
        pageSize = {"width": 60, "height": 40}
        targetArea = {"width": 200, "height": 100}
        spacing = 10
        result = pdfGetDiptychFit(pageSize, targetArea, spacing)
        self.assertEqual(result, [35, 30, 105, 30])

if __name__ == '__main__':
    unittest.main()