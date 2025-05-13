# in data analysis we often have to play with lots of different tables 
# and panda come with this function which helps us to merge different table just as in SQL to do the analysis
#let's look how innermerge work in panda

# we import panda and the files we are working with
import pandas as pd

sales = pd.read_csv('panda/multipletable/sales.csv')
targets = pd.read_csv('panda/multipletable/targets.csv')
men_women = pd.read_csv('panda/multipletable/men_women.csv')

# lets do inner merge in this two table
sales_targets = pd.merge(sales,targets)
# lets find the month where the sales is more than the target
sales_vs_targets = sales_targets[sales_targets.revenue > sales_targets.target]

# now is time to do more complicated stuff
# since we can merge multiple tables together we can actually chain the merge method
all_results = sales.merge(targets).merge(men_women)
# now the assignment is find a month where the revenue > target and women > men
results = all_results[(all_results.revenue > all_results.target) & (all_results.women > all_results.men)]



# sometimes the column name is not similar in both tables, in our case the product_id in orders table is actually referrring to id in product table. Which actually make sense however if we just merge them than it will cause an error 
# to fix this error we must change the column name and we change the column name using .rename function
orders = pd.read_csv('panda/multipletable/orders.csv')
products = pd.read_csv('panda/multipletable/products.csv')
orders_products = pd.merge(orders,products.rename(columns={'id':'product_id'}))

# untill now the column were by default merging on the basis of id column however we want to change that using 2 parameters left_on and right_on, left_on equals to the column name where we want to connect and right_on means the second column name which we want to merge to the first table. if we provide only these 2 parameters by default panda will create x_id and y_id columns name which we must change. To do this another parameter to merge function is suffixes where we pass an list of suffixes in place of x and y 

#so if we want to merge this two column with more control this is what we are supposed to do
orders_products = pd.merge(orders,products,left_on='product_id',right_on='id',suffixes=['_orders','_products'])
print(orders_products)


# we have yet another functionality while working with multiple tables called concatenate which works only if the columns name and the columns number are same in both table 

# the syntax is :
# concatenated_df = pandas.concat([df1,df2])