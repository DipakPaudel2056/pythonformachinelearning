# as we read the text and the csv file we can also read the json file
# here is the quick syntax of the json reading syntax

# import json #for csv we import csv module in the same way I upload the json module to work with the json module
# with open('message.json') as message_json: 
#   message = json.load(message_json) #json.load() method to be able to read the json data into object
#   print(message['text'])

# writing the json file
# we can also convert the dictionaries into json using dump function
# here is the quick snick pick 

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]
import json
with open('file\data.json','w') as data_json:
  json.dump(data_payload,data_json)
  
  