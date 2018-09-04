from ppextensions.pputils.utils.configuration import *
import unittest

class TestPPUtilsConfiguration(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def test_load_config(self):
        conf = load_conf(PATH)
        self.assertTrue(isinstance(conf, dict))

    def test_conf_info(self):
        config_info = conf_info("test-engine")
        self.assertTrue(isinstance(config_info, dict))

if __name__ == '__main__':
    unittest.main()
