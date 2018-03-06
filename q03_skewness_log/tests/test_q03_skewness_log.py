# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import skewness_log
from inspect import getfullargspec

ny_housing = pd.read_csv('data/train.csv')
skewed_val1, skewed_val2 = skewness_log(ny_housing)

class TestSkewness_log(TestCase):
    def test_skewness_log_args(self):

        # Input parameters tests
        args = getfullargspec(skewness_log)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_skewness_log_default(self):
        args = getfullargspec(skewness_log)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types 
    def test_check_returnGrLivArea_float(self):        
        self.assertIsInstance(skewed_val1, float,
                              "Expected data type for return value is `Float`, you are returning %s" % (
                                  type(skewed_val1)))
    def test_check_returnSalePrice_float(self):
        self.assertIsInstance(skewed_val2, float,
                              "Expected data type for return value is `Float`, you are returning %s" % (
                                  type(skewed_val2)))

        # Return value tests
    def test_values_GrLivArea(self):
        self.assertAlmostEqual(skewed_val1, -0.00698, 4, "Return value does not match expected value")

    def test_values_SalePrice(self):
        self.assertAlmostEqual(skewed_val2, 0.12121, 4, "Return value does not match expected value")
