# Default Imports
<<<<<<< HEAD
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
=======
>>>>>>> ead7dd0dda06169bc83a097d0598bc2875ec7ae6
from unittest import TestCase
import pandas as pd
from ..build import skewness_log
from inspect import getargspec


class TestSkewness_log(TestCase):
    def test_skewness_log(self):
<<<<<<< HEAD
        ny_housing = pd.read_csv('data/train.csv')
        skewed  = skewness_log(ny_housing)
=======
>>>>>>> ead7dd0dda06169bc83a097d0598bc2875ec7ae6

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
        self.assertEqual(skewed_val1, -0.006987993304655894, "Return value does not match expected value")
        self.assertEqual(skewed_val2, 0.1212103673013655, "Return value does not match expected value")
