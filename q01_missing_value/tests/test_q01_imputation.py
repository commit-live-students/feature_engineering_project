# Default Imports
from unittest import TestCase
import pandas as pd
from ..build import imputation
from inspect import getfullargspec

ny_housing = pd.read_csv('data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
imp = imputation(housing_data)

class TestImputation(TestCase):
    def test_imputation_args(self):
        # Input parameters tests
        args = getfullargspec(imputation)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))

    def test_imputation_defaults(self):
        args = getfullargspec(imputation)
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

    # Return data types
    def test_datframe_1(self):
        self.assertIsInstance(imp[0], pd.core.frame.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(imp[0])))
    def test_datframe_2(self):
        self.assertIsInstance(imp[1], pd.core.frame.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(imp[1])))
    
    # Return value tests
    def test_na_values_datframe_1(self):
        Return_val = imp[0].isnull().values.any()
        self.assertEqual(Return_val, False, "Return value contains NaN values")

    def test_na_values_datframe_2(self):
        Return_val1 = imp[1].isnull().values.any()
        self.assertEqual(Return_val1, False, "Return value contains NaN values")
