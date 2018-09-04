from ppextensions.pputils.utils.log import Log
import unittest

class TestPPUtilsLog(unittest.TestCase):

    def setUp(self):
        self.logger = Log("test_logger")
        
    def test_log_debug(self):
        self.assertTrue(self.logger.debug("test_debug") == None)

    def test_log_error(self):
        self.assertTrue(self.logger.error("test_error") == None)

    def test_log_info(self):
        self.assertTrue(self.logger.info("test_info") == None)

    def test_log_exception(self):
        self.assertTrue(self.logger.exception("test_exception") == None)

if __name__ == '__main__':
    unittest.main()
