# untill now we learnt how inner merge works and the benefits of using the inner merge however it also has some drawback as it hides the data from the table which are not in another table. 
# To overcome this problem we want to do outer join just as in sql

# lets import our beloved csvs
import pandas as pd

store_a = pd.read_csv('panda/multipletable/store_a.csv')
store_b = pd.read_csv('panda/multipletable/store_b.csv')

# lets do outer merge on them:
# to do this we use merge but with how attrbiute which would be equal to "outer"

store_a_b = pd.merge(store_a,store_b,how='outer')
print(store_a_b) #we have seen that the data which donot have the value on the given table are displayed as NaN 

