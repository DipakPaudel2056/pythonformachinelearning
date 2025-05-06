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
print(march)