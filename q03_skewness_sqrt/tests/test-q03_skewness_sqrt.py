# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import skewness_sqrt
from inspect import getargspec

ny_housing = pd.read_csv('data/train.csv')
skewed_sqrt_val1, skewed_sqrt_val2 = skewness_sqrt(ny_housing)


class TestSkewness_sqrt(TestCase):
    def test_skewness_sqrt_args(self):

        # Input parameters tests
        args = getargspec(skewness_sqrt)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_skewness_sqrt_default(self):
        args = getargspec(skewness_sqrt)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
    def test_skewness_sqrt_GrLivArea(self):
        self.assertIsInstance(skewed_sqrt_val1, float,
                              "Expected data type for return value is `Float`, you are returning %s" % (
                                  type(skewed_sqrt_val1)))

    def test_skewness_sqrt_SalePrice(self):
        self.assertIsInstance(skewed_sqrt_val2, float,
                              "Expected data type for return value is `Float`, you are returning %s" % (
                                  type(skewed_sqrt_val2)))

        # Return value tests
    def test_skewness_sqrt_GrLivArea(self):
        self.assertAlmostEqual(skewed_sqrt_val1, 0.59364, 4, "Return value does not match expected value")

    def test_skewness_sqrt_SalePrice(self):
        self.assertAlmostEqual(skewed_sqrt_val2, 0.94218, 4, "Return value does not match expected value")

