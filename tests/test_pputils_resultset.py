from ppextensions.pputils.utils.resultset import ResultSet, unduplicate_field_names
import unittest
import pandas as pd

class TestPPUtilsResultSet(unittest.TestCase):

    def setUp(self):
        data = {'col1': [1,2,3,4], 'col2': [3,4,5,6], 'col3': [4,5,6,7], 'col4': [5,6,7,8]}
        cols = ['col1', 'col2', 'col3', 'col4']
        self.resultset = ResultSet(cols, data)
        
    def test_resultset_df(self):
        df = self.resultset.DataFrame()
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_dict(self):
        dictionary = self.resultset.dict()
        self.assertTrue(isinstance(dictionary, dict))
        
    def test_csv(self):
        self.assertTrue(self.resultset.csv())
        
    def test_unduplicate_field_names(self):
        cols = ['col1', 'col2', 'col3', 'col4', 'col1']
        updated_cols = unduplicate_field_names(cols)
        self.assertTrue(isinstance(updated_cols, list))

if __name__ == '__main__':
    unittest.main()
