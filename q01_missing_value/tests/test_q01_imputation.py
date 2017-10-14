# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
import pandas as pd
from q01_missing_value.build import imputation

class TestImputation(TestCase):
    def test_imputation(self):
        ny_housing = pd.read_csv('data/train.csv')
        # Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
        housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
        imp = imputation(housing_data)
        type(imp)
        self.assertTrue(type(imp) == tuple)