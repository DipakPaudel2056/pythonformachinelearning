# insert method
# insert method in python takes 2 arguments, arg1 for the index where to insert and arg2 for the element to be inserted and it mutates the original list 
new_list = ['apple','ball','cat']
# inserting a new element at front means at index 0

new_list.insert(0, 'dog')

# pop method
# pop method like in other programming languages ui sused to remove the element, in addition to remove the element from the last index, if we provide the optional argument as the index then we can pop the element from the provided index

new_list.pop(1) #remove the element from index 1
new_list.pop() #remove the last element



# range method in python takes 1 argument to determine the last number when we want to create a range of numbers it starts from 0 and ends to the provided input
# the range function however create an object and we want to convert that object to the list in this way
list1 = range(10)
print(list(list1))

# another part of the range is if we provide 2 input than it starts at the first input and ends untill the last input
# what if we have 3 inputs? than it starts at first untill it reaches the second while skipping the third input number of elements in between

range_five_three = range(5, 15, 3) #range to create a list of num from 5 untill 15 skipping 3 items between 5 # [5, 8, 11, 14]
range_diff_five = range(0,40,5) # [0, 5, 10, 15, 20, 25, 30, 35]

# len function 
# len function in python is used to find the length of the list or the object it takes the list as input and output integer value

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

big_range = range(2, 3000, 100)
big_range_length = len(big_range)

# Your code below: 
long_list_len = len(long_list)
print(big_range_length)


