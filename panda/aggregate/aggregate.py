# sometime we want to aggregate the data in the columnd and panda has made it easy to work with using aggregate function
import pandas as pd
import numpy as np
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

# if we examine the data at this point the return or print is the dataseries not a dataframe. in this case it will be really hard to work with the resultant output so we want to convert it to dataframe for further calculation to do so we use reset_index function

pricey_shoes_df = pricey_shoes.reset_index()

# lets see another example her we want to count how many of the specific shoe type are there
shoe_count = orders.groupby('shoe_type').id.count().reset_index()
#at this point the column name is id instead we want count to do so
shoe_count = shoe_count.rename(columns={'id':'count'})
print(shoe_count)


# so far we have only use some basic aggregate function but to calculate more complex logic we can make use of lambda function like this
orders = pd.read_csv('orders.csv')
percentile = lambda x : np.percentile(x,25)
cheap_shoes = orders.groupby('shoe_color').price.apply(percentile,axis=1).reset_index()


# groupby doesnot only work with one column we can pass the name of the columns as list in the groupby function as well.
shoe_counts = orders.groupby(['shoe_type','shoe_color'])['id'].count().reset_index().rename(columns={"id":"count"}) #it group according to shoe_type and shoe_color and on the basis of id it count the occurance
print(shoe_counts)

