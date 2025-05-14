import pandas as pd

# Read in the census dataframe
census = pd.read_csv('panda/EDA/census_data.csv', index_col=0)
census['birth_year'] = census['birth_year'].replace(['missing'],1967) #we have replaced the missing value with 1967
census['birth_year'] = census['birth_year'].astype('int') #we have converted the type of the birth year
average = census['birth_year'].mean() #calculating the mean of the birth_year
census['higher_tax'] = pd.Categorical(census['higher_tax'],['strongly disagree','disagree','neutral','agree','strongly agree'],ordered=True) #here we are categorising the higher tax in order so that it is easier to sort later
census['higher_tax'] = census['higher_tax'].cat.codes #label encoding higher_tax column
census = pd.get_dummies(census,columns=['marital_status']) #onehat encoding in the marital status to be able to use in model later
print(census.head()) #finally seeing the result