# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import skewness_sqrt
from inspect import getargspec


class TestSkewness_sqrt(TestCase):
    def test_skewness_sqrt(self):

        # Input parameters tests
        args = getargspec(skewness_sqrt)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
        ny_housing = pd.read_csv('data/train.csv')
        skewed_sqrt_val1, skewed_sqrt_val2 = skewness_sqrt(ny_housing)
        self.assertIsInstance(skewed_sqrt_val1, float,
                              "Expected data type for return value is `Float`, you are returning %s" % (
                                  type(skewed_sqrt_val1)))
        self.assertIsInstance(skewed_sqrt_val2, float,
                              "Expected data type for return value is `Float`, you are returning %s" % (
                                  type(skewed_sqrt_val2)))

        # Return value tests
        self.assertEqual(skewed_sqrt_val1, 0.59364, "Return value does not match expected value")
        self.assertEqual(skewed_sqrt_val2, 0.94218, "Return value does not match expected value")

