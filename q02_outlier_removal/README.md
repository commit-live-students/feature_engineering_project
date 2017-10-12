# Outliers

Second important step in Pre-processing is finding out the outliers from the dataset and either removing them from the dataset or capping them.

## Write a function `outlier_removal` that :
- Calculates the quantile values of the variables and then removes those observation which are higher than quantile values.

Hint: keep the quantile value 0.95.  

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| dataset| dataframe | compulsory |  | Dataframe with specified variables mentioned before|


#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| dataset | Pandas DataFrame | DataFrame with outlier removal implementation |
