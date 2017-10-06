import pandas as pd
from sklearn.preprocessing import LabelEncoder
#Calculating the Skewness and then removal of skewness using Log_transformation
ny_housing = pd.read_csv('data/train.csv')
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Solution
# Write your code here