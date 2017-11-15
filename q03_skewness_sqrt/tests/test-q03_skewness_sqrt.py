# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import skewness_sqrt
from inspect import getfullargspec


class TestSkewness_sqrt(TestCase):
    def test_skewness_sqrt(self):

        # Input parameters tests
        args = getfullargspec(skewness_sqrt).args
        args_default = getfullargspec(skewness_sqrt).defaults
        self.assertEqual(len(args), 1, "Expected arguments %d, Given %d" % (1, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

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
        self.assertAlmostEqual(skewed_sqrt_val1, 0.59364, 4, "Return value does not match expected value")
        self.assertAlmostEqual(skewed_sqrt_val2, 0.94218, 4, "Return value does not match expected value")

