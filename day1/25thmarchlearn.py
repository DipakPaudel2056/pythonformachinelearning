# day2 of learning python
#  today i did the first project of the codecademy and it was about the medical report and calculate the insurance price and the change in the price of the insurance based off of the 
# various variables 
# the code below is the final solution i did the first project of the codecademy

# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128*sex + 370*bmi+425*num_of_children + 24000*smoker - 12500
print("This person's insurance cost is " + str(insurance_cost) +  " dollars.")

age += 4
# Age Factor
new_insurance_cost = 250 * age - 128*sex + 370*bmi+425*num_of_children + 24000*smoker - 12500
print("This person's insurance cost is " + str(new_insurance_cost) +  " dollars.")
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("the change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost)+" dollars.")
age -= 4
# BMI Factor
bmi += 3.1
new_insurance_cost = 250 * age - 128*sex + 370*bmi+425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated insurance cost after increasing BMI by 3.1 is " + str(change_in_insurance_cost) + " dollars")
bmi -= 3.1
# Male vs. Female Factor
sex = 1
new_insurance_cost = 250 * age - 128*sex + 370*bmi+425*num_of_children + 24000*smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print("The change in estimated cost for being male instead of female is" + str(change_in_insurance_cost) + "dollars.")

# Extra Practice
# this practice is same as changing the variable value for other 2 variables 
