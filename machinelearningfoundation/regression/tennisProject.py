import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
data = pd.read_csv('tennis_stats.csv');
df = pd.DataFrame(data)
print(data.head())
def scr(x_values,y_values):
  x_train,x_test,y_train,y_test = train_test_split(x_values,y_values,train_size = 0.80,test_size=0.20)
  lr = LinearRegression()
  lr.fit(x_train,y_train)
  y_predict = lr.predict(x_test)
  R = lr.score(x_train,y_train)
  return (R)
# let's find the features whose R value is greater than 0.8 so that we can use thos feature
for i in data.columns[2:20]:
  sc = scr(df[[i]],df[['Wins']])
  if sc > 0.8:
    print(i)
    print(sc)
print ('\n\nOutcome: Losses Models')
for i in df.columns[2:20]:
    sc = scr(df[[i]],df[['Losses']])
    if sc > 0.8:
        print (i)
        print (sc)

print ('\n\nOutcome: Winnings Models')
for i in df.columns[2:20]:
    sc = scr(df[[i]],df[['Winnings']])
    if sc > 0.8:
        print (i)
        print (sc)

print ('\n\nOutcome: Ranking Models')
for i in df.columns[2:20]:
    sc = scr(df[[i]],df[['Ranking']])
    if sc > 0.8:
        print (i)
        print (sc)
        
print ('Model: BreakPointsOpportunities, ReturnGamesPlayed')
print (scr(df[['BreakPointsOpportunities', 'ReturnGamesPlayed']], df['Winnings']))
print ('Model: BreakPointsOpportunities, ServiceGamesPlayed')
print (scr(df[['BreakPointsOpportunities', 'ServiceGamesPlayed']], df['Winnings']))
print ('Model: ReturnGamesPlayed, ServiceGamesPlayed')
print (scr(df[['ReturnGamesPlayed', 'ServiceGamesPlayed']], df['Winnings']))


print ('Model: BreakPointsOpportunities, ReturnGamesPlayed, ServiceGamesPlayed')
print (scr(df[['BreakPointsOpportunities', 'ReturnGamesPlayed', 'ServiceGamesPlayed']], df['Winnings']))
print ('finish')