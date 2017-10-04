# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
from unittest import TestCase
import pandas as pd
from q03_skewness_sqrt.build import skewness_sqrt

class TestSkewness_sqrt(TestCase):
    def test_skewness_sqrt(self):
        ny_housing = pd.read_csv('../data/train.csv')
        skewed_sqrt  = skewness_sqrt(ny_housing)
        self.assertTrue(skewed_sqrt == (0.5936439161879563, 0.9421834681211159))
