# Task 2: Outliers

**Second important step in Pre-processing is finding out the outliers from the dataset and either removing them from the dataset or capping them.**

**Create a function `outlier_removal` which calculates the quantile values of the variables and then removes those observation which are higher than quatile values.**

**Output of function should show the quantile values.**

- Hint: keep the quantile value 0.95.  

**Parameter is given to you.**

#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| dataset| dataframe | compulsory |  | making changes into dataset |


#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| dataset | Pandas DataFrame | DataFrame with change in observations |
