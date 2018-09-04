from ppextensions.ppsql.connection.hiveconnection import HiveConnection
from thriftpy.transport import TTransportException
import unittest

class TestPPSqlHiveConnection(unittest.TestCase):
    
    def test_invalid_hive_connection(self):
        with self.assertRaises(TTransportException):
            hc = HiveConnection("fake", "fake", 1234, "GSSAPI", "fake")
            self.assertTrue(hc != None)
            
if __name__ == '__main__':
    unittest.main()
