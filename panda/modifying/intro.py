# sometime we have to add column in the data frame and a naive way to do is same as list declaration
import pandas as pd

df = pd.DataFrame([
  [1,'Anurag', '3 inch screw', 0.5, 0.75],
  [2,'Saksham', '2 inch nail', 0.10, 0.25],
  [3,'Saurav', 'hammer', 3.00, 5.50],
  [4,'Aaryan', 'screwdriver', 2.50, 3.00]
],
  columns=['Product ID','Name', 'Description', 'Cost to Manufacture', 'Price']
)
# Add columns here
# here we have manually added a new column with manually typing the data
df['Sold in Bulk?'] = ['Yes','Yes','No','No']
# also if there is just one value to be populated in one column then we can also do this
df['is taxed?'] = 'Yes'
# we can also perform the operation in between the values of the column and create new column in this way
df['margin'] = df['Price'] - df['Cost to Manufacture']
# we can also make the use of apply function to make the change in the column
df['Lowercase Name'] = df.Name.apply(str.lower) 
print(df)