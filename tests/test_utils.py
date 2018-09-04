from pputils.utils import utils
import unittest

class TestPPUtilsUtils(unittest.TestCase):
  
    def test_renew_kerberos_ticket(self):
        self.assertFalse(utils.renew_kerberos_ticket("fake","fake"))

    def test_load_user_config(self):
        user_config = utils.load_user_config()
        self.assertTrue(user_config != None)
        self.assertTrue(isinstance(user_config, dict))
    

if __name__ == '__main__':
    unittest.main()
