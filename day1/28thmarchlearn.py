# starting of the 4th day of python
# i will be doing the project of codecademy all on my own
# i will first do the project in the web editor and then i will paste the final code in here


# Create calculate_insurance_cost() function below: 


# Initial variables for Maria 
age = 28
sex = 0  
bmi = 26.2
num_of_children = 3
smoker = 0  

def calculate_insurance_cost(name,age,sex,bmi,num_of_children,smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output_message = "The estimated insurance cost for "+name+" is "+ str(estimated_cost) + " dollars."
  return estimated_cost, output_message
def insurance_diff(a,b):
  diff = a - b
  print("the difference of insurance is" + str(diff))
  return diff

maria_insurance_cost = calculate_insurance_cost("maria",28,0,26.2,3,0)
omar_insurance_cost = calculate_insurance_cost("omar", 35,1,22.2,0,1)
new_insurance_cost = calculate_insurance_cost("dipak",25,1,25,0,0)
insurance_diff(maria_insurance_cost[0], omar_insurance_cost[0])


# that is the overall code i wrote in the codecademy
# first we started playing with the hard coded data and formula to get the desired output
# in the second step we defined the function and added parameters to the function
# in the third step created new variables to store the estimated insurance cost for two different people
# in the fourth step we called the function
# in the fifth step we did multiple returns from the function
# int the sixth step we created additional function to find the difference between the two people


# the catch in this process where i messed was, since i was from js background i thought it have only one return and tried to actually subtract the tuples but later i passed the first return from those 2 functions and found the estimated cost difference