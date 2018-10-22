# Data Encoding
Now is the right time to encode the categorical variable.
So far we have worked on the Numerical dataset performing outlier removal and Skewness treatment.
Now, we will work on Categorical Variables.

## Write a function `encoding` that:
- Which deals with the two categorical variable.
- Encodes `LotShape` using Label Encoder and saves it in a new column called `LotShape_Label`. Also creates dummies for column `GarageType`
  
### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| dataset| dataframe | compulsory |  | making changes into dataset |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|dataset|Pandas DataFrame|DataFrame with implementation of encoding|
