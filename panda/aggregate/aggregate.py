# sometime we want to aggregate the data in the columnd and panda has made it easy to work with using aggregate function
import pandas as pd
orders = pd.read_csv("panda/aggregate/orders.csv")
# so if we want to find the maxprice then 
maxprice = orders.price.max() #it save the maxprice from the price column in orders dataframe
print(maxprice)

# we have this list of aggregate function in pandas
    # mean	Average of all values in column
    # std	Standard deviation
    # median	Median
    # max	Maximum value in column
    # min	Minimum value in column
    # count	Number of values in column
    # nunique	Number of unique values in column
    # unique	List of unique values in column

# these are just the basic measure function that we use to calculate basic math operation in dataframe. One powerful thing we can do with the panda is with groupby function

# the syntax for the groupby function is df.groupby('column_name').column_name2.mathfunction()
# lets try to find the max of the price for each shoe type.

pricey_shoes = orders.groupby('shoe_type').price.max()
print(pricey_shoes)
