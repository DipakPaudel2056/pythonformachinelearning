# till now we have read and update text file but we are dealing with csv file in this Module
# csv are the comma separated value

# to work with csv we import a module called csv
# this module gives us the method called csvDictReader which converts the csv data into the dictionary

import csv
import os
print(os.getcwd())
with open('file\csvfile.csv') as temp_csv_file:
    # to be able to read a csv file
    csvDict = csv.DictReader(temp_csv_file)
    for row in csvDict:
        print(row)