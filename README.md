# LinearRegression_Python
A simple linear regression model using python to predict the weight based on height of an individual.

## importing the data & liberary
```{python}
import pandas as pd
import numpy as np

df = pd.read_csv("H:/Machine Learning/linear regression/heightWeightdata.csv")
df

reg = linear_model.LinearRegression( )
reg.fit(df[['Height']],df.Weight)

reg.predict([[5.4]])
```
