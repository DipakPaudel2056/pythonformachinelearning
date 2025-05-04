# dataframe is an python object that makes manipulating the tabular data much easier
# so how we create a dataframe using panda
#1. import panda
#2. get the dictionary entries with key with column name and list as the value
#pass it to the dataframe method

import pandas as pd

df1 = pd.DataFrame({
    'name':['dipak','saksham','anurag'],
    'age':[25,26,26],
    'married':[1,0,0]
})
df1.set_index('name')
print(df1)


# there is yet another way to create a dataframe using only list 
# we do that using the column keyword to define the name of the column in this way

df2 = pd.DataFrame([[1,'dipak',25],[2,'saksham',26],[3,'anurag',26]],columns=['id','name','age'])
df2.set_index('name')
print(df2)