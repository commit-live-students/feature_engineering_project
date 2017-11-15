# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import skewness_log
from inspect import getfullargspec


class TestSkewness_log(TestCase):
    def test_skewness_log(self):

        # Input parameters tests
        args = getfullargspec(skewness_log).args
        args_default = getfullargspec(skewness_log).defaults
        self.assertEqual(len(args), 1, "Expected arguments %d, Given %d" % (1, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return data types
        ny_housing = pd.read_csv('data/train.csv')
        skewed_val1, skewed_val2 = skewness_log(ny_housing)
        self.assertIsInstance(skewed_val1, float,
                              "Expected data type for return value is `Float`, you are returning %s" % (
                                  type(skewed_val1)))
        self.assertIsInstance(skewed_val2, float,
                              "Expected data type for return value is `Float`, you are returning %s" % (
                                  type(skewed_val2)))

        # Return value tests
        self.assertAlmostEqual(skewed_val1, -0.00698, 4, "Return value does not match expected value")
        self.assertAlmostEqual(skewed_val2, 0.12121, 4, "Return value does not match expected value")
