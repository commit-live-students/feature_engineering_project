# Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
from unittest import TestCase
import pandas as pd
import numpy as np
from q03_skewness_log.build import skewness_log

class TestSkewness_log(TestCase):
    def test_skewness_log(self):
        ny_housing = pd.read_csv('../data/train.csv')
        skewed  = skewness_log(ny_housing)

        self.assertTrue(skewed == (-0.006987993304655894, 0.1212103673013655))
