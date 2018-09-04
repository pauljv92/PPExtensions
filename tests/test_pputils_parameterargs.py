from ppextensions.pputils.utils.parameterargs import *
from IPython.core.magic_arguments import argument, magic_arguments, parse_argstring
import unittest

class TestPPUtilsParamArgs(unittest.TestCase):

    @magic_arguments()
    @argument("-test", "--test", type=str, help="test1")
    @argument("-test2", "--test2", type=str, help="test2")
    def setUp(self):
        args = "--test test --test2 testa:::testb:::testc"
        self.param_args = ParameterArgs(parse_argstring(self.setUp, args))

    def test_get_args(self):
        self.assertTrue(self.param_args.get("test") == "test")
        self.assertTrue(self.param_args.get("test2") == "testa:::testb:::testc")
        
    def test_has_args(self):
        self.assertTrue(self.param_args.hasattr("test"))
        self.assertTrue(self.param_args.hasattr("test2"))
        
    def test_get_list(self):
        return_vals = self.param_args.get_list("test2")
        self.assertTrue(isinstance(return_vals, list))
        self.assertTrue(len(return_vals) == 3)

if __name__ == '__main__':
    unittest.main()
