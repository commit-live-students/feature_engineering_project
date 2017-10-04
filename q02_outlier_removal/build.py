import pandas as pd


# Data
ny_housing = pd.read_csv('../data/train.csv')
# Selecting 4 most relevant variables from the dataset fot the Cleaning and Preprocessing.
housing_data = ny_housing[['MasVnrArea', 'GrLivArea', 'LotShape', 'GarageType', 'SalePrice']]

# Solution
def outlier_removal(housing_data):
    a = housing_data[['MasVnrArea','GrLivArea','SalePrice']].quantile(0.05)
    b = housing_data[['MasVnrArea','GrLivArea','SalePrice']].quantile(0.95)
    print(a,b)
    housing_data = housing_data.drop(housing_data[(housing_data['MasVnrArea']> 460)].index)
    housing_data = housing_data.drop(housing_data[(housing_data['GrLivArea']> 2500)].index)
    housing_data = housing_data.drop(housing_data[(housing_data['SalePrice']> 326100)].index)
    housing_data[''] = range(len(housing_data))
    housing_data.set_index('', inplace=True)
    return housing_data