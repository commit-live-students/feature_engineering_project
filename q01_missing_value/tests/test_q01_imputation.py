# Default Imports
<<<<<<< HEAD
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
=======
>>>>>>> ead7dd0dda06169bc83a097d0598bc2875ec7ae6
from unittest import TestCase
import pandas as pd
from ..build import imputation
from inspect import getargspec


class TestImputation(TestCase):
    def test_imputation(self):
<<<<<<< HEAD
=======
        # Input parameters tests
        args = getargspec(imputation)
        self.assertEqual(len(args[0]), 1, "Expected arguments %d, Given %d" % (1, len(args[0])))
        self.assertEqual(args[3], None, "Expected default values do not match given default values")

        # Return data types
>>>>>>> ead7dd0dda06169bc83a097d0598bc2875ec7ae6
        ny_housing = pd.read_csv('data/train.csv')
        # Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
        housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
        imp, imp1 = imputation(housing_data)

        self.assertIsInstance(imp, pd.core.frame.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(imp)))
        self.assertIsInstance(imp1, pd.core.frame.DataFrame,
                              "Expected data type for return value is `pandas DataFrame`, you are returning %s" % (
                                  type(imp1)))

        # Return value tests
        Return_val = imp.isnull().values.any()
        Return_val1 = imp1.isnull().values.any()

        self.assertEqual(Return_val, False, "Return value contains NaN values")
        self.assertEqual(Return_val1, False, "Return value contains NaN values")
