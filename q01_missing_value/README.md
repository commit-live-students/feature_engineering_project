# The Missing Values

The very first step in Pre-processing is finding out the missing values from the variables and imputing those observations form the other observations.
We can do imputations of many kind.
- Kindly refer to theoretical part. 

We have selected the four variables from the dataset along with SalePrice with which we would be working 
which are as followings:
- MasVnrArea
- GrLivArea
- LotShape
- GarageType

## Write a function `imputation` that:
- Finds out Variables which contain missing values in their observations.
- Imputes the missing value(s) with one among the several missing value imputation
techniques.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| dataset| dataframe | compulsory |  | dataframe containing the above variables |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|Imputed dataframe column|dataframe|dataframe column with numerical values with implementation of missing value imputation|
|Imputed dataframe column|dataframe|dataframe column with categorical values with implementation of missing value imputation|

 Hint:
  - For numerical variable use mean of observations to fill the missing values
  - For Categorical variable use observation which is highly occured in variable.
  
Let's get started !
