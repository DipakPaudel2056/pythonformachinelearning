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


# example from codecademy tutorial
# Write your code below: 
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price

  

  return trip_total

# Step 5: call your function
calculate_expenses(200,100,100,5)

# codecademy practice
def trip_planner(first_destination,second_destination,final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + 
  " then "+
  second_destination+
  ", and lastly "
  + final_destination
)
trip_planner("Denmark","France","Germany")
trip_planner(first_destination = "Iceland",final_destination="Germany",second_destination="India")
trip_planner("Brooklyn","Queens")

# we have also used 3 different ways of passing arguments to the function

# now we are going to discuss userdefined functions and Builtin functions
# there are some functions already built in with the python called builtin function i have provided the list of some of the functions here

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = 0
max_price= max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)
min_price= min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)
rounded_price = round(tshirt_price,1)
print(rounded_price)

# scope
# the variables defined within the function only can be accessed and modified within the function it is called scope of the function
# but if there are any variables defined outside of the function it can be accessed outside of the function anywhere in the file

# returns

def add_numbers(a, b):
  return a + b

result = add_numbers(5, 10)
print(result)


current_budget = 3500.75
shirt_expense = 9
def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))
def deduct_expense(budget,expense):
  return budget - expense
new_budget_after_shirt = deduct_expense(current_budget,shirt_expense)

print_remaining_budget(current_budget)
print_remaining_budget(new_budget_after_shirt)


# codecademyu function final tutorial
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 "+ name)

trip_planner_welcome("Dipak")

def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate =  estimated_time_rounded(3.4)

def destination_setup(origin,destination,estimated_time,mode_of_transport="Car"):
  print("Your trip starts off in "+ origin)
  print("And you are traveling to "+destination)
  print("You will be traveling by "+mode_of_transport)
  print("It will take approximately " + str(estimate) + " hours")

destination_setup("kap","melb",estimate)

# tomorrow we will be doing a medical project with functions

