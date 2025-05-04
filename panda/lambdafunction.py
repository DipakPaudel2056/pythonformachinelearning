# in python using lambda we can create a function in one line like this
add_two  = lambda myInput: myInput+ 2
print(add_two(5)) #it should return 7

# this lambda function right here checks if the winput has the letter "a"
contains_a = lambda word: "a" in word
print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))