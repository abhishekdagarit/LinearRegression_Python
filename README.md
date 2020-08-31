# LinearRegression_Python
A simple linear regression model using python to predict the weight based on height of an individual.

## importing the data & liberary
```{python}
import pandas as pd
import numpy as np

df = pd.read_csv("H:/Machine Learning/linear regression/heightWeightdata.csv")
```

## Let's take a look at the data
```{python}
df
```

## applying the linear regression model
```{python}
reg = linear_model.LinearRegression( )
reg.fit(df[['Height']],df.Weight)
```

## checking the prediction
```{python}
reg.predict([[5.4]])
```
