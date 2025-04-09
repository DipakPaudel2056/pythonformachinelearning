# we have multiple ways to get the data to work with 
# we get the data from the primary source where the data are already cleansed and ready to use and secondary source

# for this particular day-one of extracting data tutorial we are going to see how we get the data from the API and work with them


import requests #here we are importing requests module to call the api
import csv #to work with the csv file


r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36') #here we are getting the encrypted r response by calling the request in the given url
r_json = r.json() #converted the encrypted r to json to make it easy to work with
# //open the file
with open('commute_data.csv',mode='w',newline='') as file: #here we have opened an empty commute_data.csv file in writing mode and newline as file
  writer = csv.writer(file) #writer method on the file
  writer.writerows(r_json) #written the json to the csv file
