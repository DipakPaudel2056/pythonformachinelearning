import pandas as pd

user_visits = pd.read_csv('panda/aggregate/miniproject/visits.csv') #just converting the csv file into panda dataframe
click_source = user_visits.groupby('utm_source').id.count().reset_index() #grouping the data according to the utm_source

click_source_by_month = user_visits.groupby(['utm_source','month'])['id'].count().reset_index().rename(columns={"id":"count"}) #grouping the dataframe  by utm_source and the month
click_source_by_month_pivot = click_source_by_month.pivot(index="utm_source",columns="month",values="count").reset_index() #creating pivot table from previously grouped data
print(click_source_by_month_pivot)