from ppextensions.ppsql.connection.csvconnection import CSVConnection
import unittest

class TestPPSqlCSVConnection(unittest.TestCase):

    def setUp(self):
        self.csvconn = CSVConnection()

    def test_csv_query(self):
        self.assertTrue(self.csvconn.execute("select * from test_files/test.csv") != None)

if __name__ == '__main__':
    unittest.main()
