# i have good understanding of the for and while loops in python so i
# didnot document it here however in python i found one syntax or the term called list comprehension


# List comprehension is a compact way to create lists using another list 
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade+10 for grade in grades] # here i have created new list using the grades list and adding extran 10 in every element
print(scaled_grades)


# another good use case of the list comprehension is we can use list comprehension with the conditional statement as well

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157] #list of the heights of the people
can_ride_coaster = [height for height in heights if height > 161 ] # list comprehension to check if the height is greater than 161
print(can_ride_coaster)


# mini project from codecademy

single_digits= [] #creating a single digits empty list
for i in range(10):
  single_digits.append(i) #using a normal for loop i populated an empty list
squares = []
for element in single_digits:
  print(element)
  squares.append(element ** 2) # populated the squares list with the square value

print(squares)
cubes = [cube**3 for cube in single_digits ]
print(cubes)