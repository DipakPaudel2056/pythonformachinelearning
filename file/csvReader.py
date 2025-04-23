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
# import csv
# with open('books.csv') as books_csv:
#   books_reader = csv.DictReader(books_csv,delimiter='@') #here the delimiter is @ 
#   isbn_list = []
#   for row in books_reader:
#     isbn_list.append(row['ISBN'])

# print(isbn_list)


# as we can read the csv file in the dictionary format we can also write the list into the csv format 
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open('file\logger.csv','w') as logger_csv: #we opened the logger csv file as logger_csv in writing mode
   log_writer = csv.DictWriter(logger_csv,fieldnames=fields) #we used dictwriter method to writeinto the csv file and keyword argument fieldnames is set to fields list
   log_writer.writeheader() #we have used writeheader to create a header of the csv file using the previous step
   for row in access_log : #loop throught the log and wriiten the row in th row
    log_writer.writerow(row)
