from ppextensions.pputils.utils.yarnapi import ResourceManager
import unittest
import requests

class TestPPUtilsYarnAPI(unittest.TestCase):
    
    def setUp(self):
        # In current implementation we will have two RM Objects
        # One with invalid RM Url & One with Valid one
        self.invalid_rm = ResourceManager("http://invalidrm.paypalinc.com")
        
    def test_invalid_rm_cluster_app(self):
        with self.assertRaises(requests.exceptions.ConnectionError):
            self.invalid_rm.cluster_application("fake_app")

    def test_invalid_rm_cluster_metrics(self):
        with self.assertRaises(requests.exceptions.ConnectionError):
            self.invalid_rm.cluster_metrics()

if __name__ == '__main__':
    unittest.main()
