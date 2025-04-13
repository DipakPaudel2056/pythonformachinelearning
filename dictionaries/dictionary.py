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