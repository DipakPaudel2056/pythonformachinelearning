# here in this project we will use the scikit linearregression model to predict the honey production in the future year 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://content.codecademy.com/programs/data-science-path/linear_regression/honeyproduction.csv")
# grouping the data by year and getting their mean
prod_per_year = df.groupby(df['year'])['totalprod'].mean().reset_index()
# reshapping the data to fit for the scikit
X = prod_per_year['year'].values.reshape(-1,1)
y = prod_per_year['totalprod']
# created scatter plot
plt.scatter(X,y)
# made linear regression model using LinearRegression from Scikit
regr = LinearRegression()
# fit the X and y Value
regr.fit(X,y)
print([regr.coef_,regr.intercept_])
# predicted Y value for the given X value
y_predict = regr.predict(X)
# shown the straight line which has less average loss
plt.plot(X,y_predict)
plt.show()
# greated number from 2013 to 2050
nums = np.array(range(2013,2050))
X_future = nums.reshape(-1,1)
# getting the production prediction using the previous regr model
future_predict = regr.predict(X_future)
plt.plot(X_future,future_predict)
plt.show()
