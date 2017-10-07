## Task 1: The Missing Values

**The very first step in Pre-processing is finding out the missing values from the variables and imputing those observations form the other observations.**

**We can do imputations of many kind.**
- Kindly refer to theoretical part. 

**Create function `imputation` which performs above explained task as together as one.**

**Finding out Variables which contain missing values in their observation**

- Write down your solution by Defining the Function which finds out missing values in variables.

**Now after finding out the variables with missing value, next job of this task is to impute those missing values**


- Hint:
    - For numerical variable use mean of observations to fill the missing values
    - For Categorical variable use obseervation which is highly occured in variable.
    


**Parameter is given to you.**
  
#### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- | 
| dataset| dataframe | compulsory |  | making changes into dataset |


#### Returns:

| Return | dtype | description |
| --- | --- | --- | 
|dataset|Pandas DataFrame|DataFrame with change in observations|