# a introduction was made to me by giving the example of the decisions we take since the time we wake up
# learnt about the comparison operator
#  == is the equal operator and the != is a not equal operator
# before starting the control flow it make us clear about the boolean data type

# we spent a brief time to explain and understand the boolean expression and the values
# now i am interested in the if statement

# if statement is used to make decisions based on boolean expressions
# in python the syntax looks like this:
#     if condition:
#         # code block to execute if the condition is true
#     else:
#         # code block to execute if the condition is false

# Enter a user name here, make sure to make it a string
user_name =  "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I knwo it is you, Dave! Go away!")


# here we are just using conditional operator == and != 
# but to get the boolean expression or the values we have relational operators too
# some relational operators are < , >, <=, >=,
# and we also have boolean operators or and not 

# the project code after completing the lesson was like this
def analyze_smoker(smoker_status):
    if smoker_status == 0:
      print("to lower your cost, you should consider quitting smoking")
    else:
      print("Smoking is not an issue for you.")
# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)
dipak_insurance_cost = estimate_insurance_cost("dipak",25,1,0,0)