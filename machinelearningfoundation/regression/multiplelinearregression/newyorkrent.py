import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")

df = pd.DataFrame(streeteasy)
x = df[['bedrooms','bathrooms','size_sqft','min_to_subway','floor','building_age_yrs','no_fee','has_roofdeck','has_washer_dryer','has_doorman','has_elevator','has_dishwasher','has_patio','has_gym']]
y = df[['rent']]

x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,test_size=0.2)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# since we have got the test and the train data lets run the model
mlr = LinearRegression()
mlr.fit(x_train,y_train)
y_predict = mlr.predict(x_test)
sonny_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 0]]
predict = mlr.predict(sonny_apartment)
print( predict)


# let's analyse the model using the Residual analysis for that the scikit gives us the score method which is the coefficient of determination
# this R^2 value must be more than 0.70 for the model to be called as good 
# let's find the R^2 value for the 
R2 = mlr.score(x_train,y_train)
R3 = mlr.score(x_test,y_test)
print(R2,R3)