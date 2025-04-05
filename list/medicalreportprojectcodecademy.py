names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla") # append new name
insurance_costs.append(8320.0) #append new insurance cost

medical_records = list(zip(insurance_costs,names)) #this method zip two different list elemen to create a 2d list
print(medical_records)

num_medical_records = len(medical_records) #counting the number of records
print("There are " + str(num_medical_records) + " medical records.")



first_medical_record = medical_records[0] 
print(first_medical_record)

medical_records.sort() #sorting the element by insurance cost
print("Sorted medical records \n", medical_records )
cheapest_three = medical_records[:3] #finding first 3
print("cheapest three medical records \n",cheapest_three)
expensive_three = medical_records[-3:] #finding last 3
print("expensive three medical records \n",expensive_three)


occurances_paul = names.count("Paul") #counting the occurance of the paul
print("There are " + str(occurances_paul) + " individuals with the name Paul in our medical records.")