# dataframe allows us to select a column or multiple columns from the given dataframe to be able to do that we have 2 ways
# create a dataframe from the list or the dictionaries or read the csv file and convert that into a data frame
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
clinic_north_south = df[['clinic_north','clinic_south']]
print(clinic_north_south)
print(type(clinic_north_south))