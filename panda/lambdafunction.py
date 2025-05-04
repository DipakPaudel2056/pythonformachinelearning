# in python using lambda we can create a function in one line like this
add_two  = lambda myInput: myInput+ 2
print(add_two(5)) #it should return 7

# this lambda function right here checks if the winput has the letter "a"
contains_a = lambda word: "a" in word
print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))


#this lambda function long_string 
long_string = lambda str:len(str) > 12

print(long_string("short"))
print(long_string("photosynthesis"))

#this lambda function check if the string ends in character a 
ends_in_a = lambda str:str[-1] == "a"

print(ends_in_a("data"))
print(ends_in_a("aardvark"))

# we can also add if clause in the lamba function in this way
#lambda function with if clause looks like this:
double_or_zero = lambda num: num * 2 if num > 10 else 0
print(double_or_zero(15))
print(double_or_zero(5))

# one trick with the python is we can find if the num is multiple of the given number n by using %n 
# lambda to find if the number is multiple of 3
multiple_three = lambda num:True if num%3 else False