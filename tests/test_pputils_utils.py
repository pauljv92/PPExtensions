from ppextensions.pputils.utils import utils
import pandas as pd
import unittest

class TestPPUtilsUtils(unittest.TestCase):
    
    def setUp(self):
        self.test_df = utils.csv_to_df({}, {"csv":"test_files/test.csv"})

    def test_renew_kerberos_ticket_negative(self):
        self.assertFalse(utils.renew_kerberos_ticket("fake","fake"))

    def test_renew_kerberos_ticket_positive(self):
        self.assertTrue(utils.renew_kerberos_ticket("pp_batch_opts_admin","~/PPExtensions/tests/test_files/.pp_batch_opts_admin.keytab"))
        
    def test_parse_run_str(self):
        self.assertTrue(utils.parse_run_str("%%info"))
        self.assertTrue(utils.parse_run_str("test_call_value=123"))

    def test_csv_to_df_and_back(self):
        df = utils.csv_to_df({}, {"csv":"test_files/test.csv"})
        self.assertTrue(isinstance(df, pd.DataFrame))
        args = {"dataframe":"df"}
        csv_file = utils.df_to_csv({"df":df}, args)
        self.assertTrue(csv_file != None)

    def test_substitute_params(self):
        substitute_cell = utils.substitute_params("test_cell_value = {}", {"test":"test"})
        self.assertTrue(substitute_cell != None)

    
if __name__ == '__main__':
    unittest.main()
