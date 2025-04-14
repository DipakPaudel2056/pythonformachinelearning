# here in this lecture we created a dictionary and populated the dictionary
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"]=12
animals_in_zoo["dinosaurs"]=0
print(animals_in_zoo)

# like list comprehension we also have the dict comprehension in dictionary here we create a set of dictionary by zipping two different list
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

zipped_songs = zip(songs,playcounts)
plays = {key: value for key,value in zipped_songs}
print(plays)


zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# checking if the energy is in the zodiac_elements, 
# this will prevent it from getting name error
if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])

zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"])



# this approach is not sustainable so we have the .get() method to find if the value exist and if the value is not exist than we can also set the value 
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder")
print(tc_id)
# printing the tc_id which is the key that exist in the dictionary

stack_id = user_ids.get("superStackSmash",100000) #setting the value as 1000000 if the key provided doesnot exist in the dictionary
print(stack_id)


# popping up the value from the dictionary is very easy
# we use the .pop method to remove the key value pair from the dictionary and in return we get the value of that key and if we donot have the value than we can get the default value by passing on the other argument in the pop method
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
ans = available_items.pop("stamina grains") #it returns the value of stamina grains which is 15
health_points += ans

power_value = available_items.pop("power stew")
health_points += power_value
health_points += available_items.pop("mystic bread",0) #it is checking if the mystic bread is in dictionary and pass the default value of 0 if mystic bread is not in the dictionary
print(available_items,health_points)

# sometime if we want to get the access to all the keys of the dictionaries we can use .keys method
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)