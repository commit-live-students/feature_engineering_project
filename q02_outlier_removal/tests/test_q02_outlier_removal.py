# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import outlier_removal
from inspect import getfullargspec


class TestOutlier_removal(TestCase):
    def test_outlier_removal(self):
        # Input parameters tests
		
        args = getfullargspec(calculate_statistics).args
        args_default = getfullargspec(calculate_statistics).defaults
        self.assertEqual(len(args), 1, "Expected arguments %d, Given %d" % (1, len(args)))
        self.assertEqual(args_default, None, "Expected default values do not match given default values")

        # Return data types
        ny_housing = pd.read_csv('data/train.csv')
        housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
        without_out = outlier_removal(housing_data)
        self.assertIsInstance(without_out, pd.core.frame.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(without_out)))

        # Return value tests
        self.assertEqual(without_out.shape, (1302, 5), "Return value shape does not match expected value")
