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
        
        
# till now we have only dealt with the csv files separated by comma but we also have other kinds of csv file where the delimiter are different
import csv
with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv,delimiter='@') #here the delimiter is @ 
  isbn_list = []
  for row in books_reader:
    isbn_list.append(row['ISBN'])

print(isbn_list)