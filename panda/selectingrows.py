# in dataframe the data is 0 indexed so we access the rows of data using those indexes and this equation,
# df.iloc[index]
import pandas as pd
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

# to select the data of march, since it is in 2 index we use
march = df.iloc[2]
# we can also select the number of rows using
april_may_june = df.iloc[3:6] #this will select the row from 3 to 6 not including 6

# we can also using conditional logic to find the specific data using panda
# to find all the records of data of january 
january = df[df.month == "January"]
# find the rows whree clinic_east > 60
clinic_east_greater_than_60 = df[df.clinic_east > 60]
print(clinic_east_greater_than_60)


# we can also add as many logic as we can inside the [] as long as the logics are separated by paranthesis
# in the example below we are finding the data that are of march or april

march_april = df[(df.month == "March") | (df.month == "April")]
print(march_april)


# in the same manner we can also let the dataframe to choose the row of the data from provided list of value like this
january_february_march = df[df.month.isin(['January','February','March'])] #here it will check the data in month row and if it finds jan feb or march it will return it
print(january_february_march)


# to be able to modify the dataframe and after selecting the specific row we can reset the index using reset_index() method
df3 = df.loc[[1,3,5]]
df4 = df3.reset_index(inplace = True)

print(df4)