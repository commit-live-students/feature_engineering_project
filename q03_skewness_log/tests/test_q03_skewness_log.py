# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import skewness_log
from inspect import getargspec


class TestSkewness_log(TestCase):
    def test_skewness_log(self):

        # Input parameters tests
        args = getargspec(skewness_log)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

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
        self.assertEqual(skewed_val1, -0.00698, "Return value does not match expected value")
        self.assertEqual(skewed_val2, 0.12121, "Return value does not match expected value")
