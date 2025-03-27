# parameters and arguments
# whenever we want a function to get a input value then we use parameters
# we use those parameters inside the paranthesis

def my_function(singleParam):
    print(f"This is a function that takes one parameter: {singleParam}")


# but how do we use these parameters
# when we want to call a function we use these parameters by passing arguments

# let's call the previous funtion
my_function("first parameter")



# codecademy tutorial
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit "+  location)
  print("/nYou can use the public subway system to get to "+ location)

generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station")


# untill now we were just using a single parameter but we can use multiple parameters while defining a functions, those parameters must be separated by comma

def my_function_with_multiple_params(param1, param2):
    print(f"This is a function that takes two parameters: {param1} and {param2}")


# and we can call this function with different arguments

my_function_with_multiple_params("first parameter", "second parameter")
