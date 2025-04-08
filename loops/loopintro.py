# i have good understanding of the for and while loops in python so i
# didnot document it here however in python i found one syntax or the term called list comprehension


# List comprehension is a compact way to create lists using another list 
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade+10 for grade in grades] # here i have created new list using the grades list and adding extran 10 in every element
print(scaled_grades)