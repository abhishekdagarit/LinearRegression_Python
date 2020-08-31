#importing the data & liberary
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("H:/Machine Learning/linear regression/heightWeightdata.csv")
df

reg = linear_model.LinearRegression( )
reg.fit(df[['Height']],df.Weight)

reg.predict([[5.4]])
