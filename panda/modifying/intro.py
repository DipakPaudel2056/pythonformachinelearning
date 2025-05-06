# sometime we have to add column in the data frame and a naive way to do is same as list declaration
import pandas as pd

df = pd.DataFrame([
  [1, '3 inch screw', 0.5, 0.75],
  [2, '2 inch nail', 0.10, 0.25],
  [3, 'hammer', 3.00, 5.50],
  [4, 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)
# Add columns here
# here we have manually added a new column with manually typing the data
df['Sold in Bulk?'] = ['Yes','Yes','No','No']
# also if there is just one value to be populated in one column then we can also do this
df['is taxed?'] = 'Yes'
print(df)