# in this session i will try to cover the basic of list operation and list data type in python.
# i have a feeling that i am taking a bit more time in this because i already have a experience of programming in javascript

# list is same as arrays in javascript

# in javascript the list must have same data type but in python we can have different data types in a list

name_list = ['alina', 'alish', 'anamika', 4, 5]
# this is valid list in python

# list method
# append() and remove()
# append is used to append a new item to the end of the list
name_list.append(6)

# remove() is used to remove an item from the list
name_list.remove(6)

# to be able toa add multiple items in the list we can perform the list concatination approach using + 

    # example
new_list = name_list + [7, 8, 9]
print(new_list)



# accessing the items  in the list
# same as js it is also indexed and starts at 0
# we access the item in the same way as in js and we also use negative indexing to access the item from the last but the catch is the last element is -1 not -0😁😁

print(name_list[0])
print(name_list[-1])

# modifying the list
# the basic approach to modify the list item is to find the index of the item and reassign the value of that index like this

name_list[1] = 'alisha'
print(name_list)

order_list = ["Celery","Orange Juice","Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)


# not only one dimension we can have list as an element in the list of the element
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64],["Vik",68]]
ages=[["Aaron",15],["Dhruti",16]]

# accessing this list element is same as accessing the item in the 1d list using square bracket notation

print(heights[0][0]) #prints "jenny"
print(ages[1][1]) #prints 16

# modifying the 2d list 
#Your code below:
incoming_class = [
  ["Kenny","American",9],
  ["Tanya","Ukrainian",9],
  ["Madison","Indian",7]
]
incoming_class[2][2] = 8
incoming_class[-3][-3] = "Ken"
print(incoming_class)


# final project from codecademy list intro session
# Your code below: 
first_names = ["Ainsley","Ben","Chani","Depak"]
preferred_size = ["Small","Large","Medium"]
preferred_size.append("Medium")
print(preferred_size)

customer_data = [
  ["Ainsley","Small",True],
  ["Ben","Large",False],
  ["Chani","Medium",True],
  ["Depak","Medium",False]
]
print(customer_data)
customer_data[2][2] = False
customer_data[1].remove(False)
customer_data_final = customer_data + [["Amit","Large",True],["Karim","X-Large",False]]
print(customer_data_final)


# zipfunction
# in python there is a built function if we want to combine 2 different list to create a 2d list it is called zipfunction
# zip function takes 2 parameters and returns the zip object and we can easily change the zip object to the list using list function 
# here is the example
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
names_and_dogs_names = zip(owners,dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)