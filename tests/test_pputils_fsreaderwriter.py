from ppextensions.pputils.utils.filesystemreader import FileSystemReaderWriter
import unittest

class TestPPUtilsFileSystemReaderWriter(unittest.TestCase):

    def setUp(self):
        # In current implementation we will have two RM Objects
        # One with invalid RM Url & One with Valid one
        self.fsreadwriter = FileSystemReaderWriter("~")
        
    def test_ensure_path_exists(self):
        self.assertTrue(self.fsreadwriter.ensure_path_exists() == None)

    def test_ensure_file_exists(self):
        self.assertTrue(self.fsreadwriter.ensure_file_exists() == None)

if __name__ == '__main__':
    unittest.main()
