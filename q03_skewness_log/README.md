# Task 3: Skewness

**The third most important step in Pre-processing is performing skewness removal from the dataset.**

**These steps transforms the dataset statistically close to Gaussian dataset, so that the largest set of tools are available to  use on the dataset.**

**For this task we will be using the raw(original data) data. Can you guess why?**

**Reason behind this is when do we remove outlier from the data then skewness also shifts. So if distribution is left skewed, then after outlier removal it will shift to right side.** 


## Skewness

**Create a two different function for `skewness` which calculates the skewness values and then removes the skewness from the data using Log transformation and Square-root transformation.**

**Name the function as `skewness`.**

- Compare the result of skewness from both the transformation.
- This function should create new variables in the dataset which contains the transformed values.  

**Parameter is given to you.**
    
#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| data| dataframe | compulsory |  | making changes into dataset |


#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
| data | Pandas DataFrame | DataFrame with change in observations |


