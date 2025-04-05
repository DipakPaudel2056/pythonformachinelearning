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



# slicing in python is very simple you just have to follow this 
# letters[start:end]

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]
middle = suitcase[2:4]
# Your code below: 
print(beginning)
print(middle)
# advance slicing includes using the negative index as input to select top from the beginning or the end of the list

advanced_slice = suitcase[:-2] #remove 2 from the end of the list

# count function returns the number of times the inputted argument exist in the list

numbers = [1, 2, 2, 3, 4, 4, 4, 5]

count_two = numbers.count(2) #return 2





# python sort method modifies the list and sort the list in ascending order but if we want to sort the list in descending order we can input reverse = True 

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)
# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(cities)

# advance sort method also includes sorted method that takes a list as input and return a new sorted list and it doesnot modify the original list 
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games,games_sorted)

