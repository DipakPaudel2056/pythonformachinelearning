import pandas as pd
# to be able to read the data from csv we need read_csv method from pd class
orders = pd.read_csv('shoefly.csv')
# to be able to get all the list of the emails
emails = orders['email']
# getting the row for the first_name Frances and last_name Palmer
frances_palmer = orders[(orders.first_name == "Frances") & (orders.last_name == "Palmer")]
# getting the shoetype clogs, boots, ballet flats
comfy_shoes = orders[orders.shoe_type.isin(['clogs','boots','ballet flats'])]