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
print(results)
