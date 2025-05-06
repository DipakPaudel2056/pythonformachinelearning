# we have many different way to modify the column data or to add new columns
# lets get the csv to dataframe
import pandas as pd
df = pd.read_csv('panda\modifying\employees.csv')
# so tell me what you want to do
# create new column lastname with the help of lambda function that check the name column and return just the lastname


# lambda function to get the lastname from given name
get_last_name = lambda name:name.split(' ')[-1]
# now we want to use this function with the apply method we learnt earlier
df['lastname'] = df.name.apply(get_last_name) #here we are prepping the name column for the lambda function
# it must have new column lastname with the lastname of the employee
#print(df) 



total_earned = lambda row: (row.hourly_wage * 40) + ((row.hourly_wage * 1.5) * (row.hours_worked - 40)) \
	if row.hours_worked > 40 \
  else row.hourly_wage * row.hours_worked
  
df['total_earned'] = df.apply(total_earned, axis = 1)



# sometime we want to modify the name of the column itself it is very simple with the .columns attribute in the dataframe itself and we instantiate the list in order with new name and it will do the job
df.columns = ["ID","Employee Name","Wage","Hours","Last Name","Amount"]
print(df)
