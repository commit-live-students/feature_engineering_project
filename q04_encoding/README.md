# Data Encoding
Now is the right time to encode the categorical variable.
So far we have worked on the Numerical dataset performing outlier removal and Skewness treatment.
Now, we will work on Categorical Variables.

## Write a function `encoding` that:
- Which deals with the two categorical variable.
- Encodes one categorical variable using Label Encoder and another one as binary coding which gives 0 and 1. 
  
### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| dataset| dataframe | compulsory |  | making changes into dataset |


### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|dataset|Pandas DataFrame|DataFrame with implementation of encoding|