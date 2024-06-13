import unittest
from unittest.mock import patch
from main import ImageProcessor  # Adjust the import based on your actual class structure

class TestImageProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()  

    @patch('main.QMessageBox')  # Mock QMessageBox to avoid GUI interaction during tests
    def test_submit_no_images(self, mock_msgbox):
        """
        Test that the submit function behaves correctly when no images have been added.
        """
        # Assuming 'addedimages' is a list attribute of ImageProcessor. Adjust if necessary.
        self.processor.addedimages = []  # Ensure no images are added

        with patch('builtins.print') as mocked_print:  
            self.processor.submit()
            mocked_print.assert_called_with('Please add image') 
        mock_msgbox.question.assert_called_once()


if __name__ == '__main__':
    unittest.main()