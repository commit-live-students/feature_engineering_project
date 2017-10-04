# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
from unittest import TestCase
import pandas as pd
from q02_outlier_removal.build import outlier_removal

class TestOutlier_removal(TestCase):
    def test_outlier_removal(self):
        # Data
        ny_housing = pd.read_csv('../data/train.csv')
        # Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
        housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
        out_shape = outlier_removal(housing_data).shape
        self.assertTrue(out_shape == (1305, 5))
