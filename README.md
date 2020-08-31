# LinearRegression_Python
A simple linear regression model using python to predict the weight based on height of an individual.

## importing the data & liberary
```{python}
import pandas as pd
import numpy as np

df = pd.read_csv("H:/Machine Learning/linear regression/heightWeightdata.csv")
```

## let's take a look at the data
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
## let's take a look at the coefficients
```{python}
reg.coef_
```

## let's take a look at the intercept
```{python}
reg.intercept_
```

## using the linear regression formula to reconcile results
```{python}
#y = mx + b
(5.4) * (20.2182285) + (-37.776636713735584)
```
