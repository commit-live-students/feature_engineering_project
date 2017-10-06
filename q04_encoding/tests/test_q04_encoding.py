# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
import pandas as pd
from q04_encoding.build import encoding

class TestEncoding(TestCase):
    def test_encoding(self):
        ny_housing = pd.read_csv('data/train.csv')
        housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]
        encoded_housing_data = encoding(housing_data)
        self.assertTrue(encoded_housing_data.shape == (1460, 11))
