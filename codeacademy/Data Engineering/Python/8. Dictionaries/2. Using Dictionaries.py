#Chapter8 : Using Dictionaries
#2025.01.02
#Jiyun Nam
#@codecademy

# 1. Get a Key
# print(listname[key value])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])



# 2. Get an Invalid Key 
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# KeyError as "energy" does not exist
# print(zodiac_elements["energy"]) 

# Add element 
zodiac_elements["energy"] = "Not a Zodiac element"
# Check the element in the dictionary 
key_to_check = "energy" #Key_to_check can always change
if key_to_check  in zodiac_elements:
  print(zodiac_elements[key_to_check])
else:
  print(f"{key_to_check} does not exist")



# 3. Safely Get a Key 
# dictionary_list.get() = search for value instead of dictionary_list[key]
# If not exist -> return None
# If want to print 0 instead of None 
# dictionary_list.get(key, 0)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

# Get the value "teraCoder", if not print 10000
tc_id = user_ids.get("teraCoder", 10000)
print(tc_id)

# Try the coe that does not exist
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)



# 4. Delete a Key
# dictionary_list.pop(key, value to instead if not exist)
# print out the key that want to delete

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

print(available_items)
# If "stamina grains" exist, add it to the health_points variable. 
# If not, add 0 to health_points 
health_points += available_items.pop("stamina grains", 0)
print("")
print(available_items)
print(health_points)

health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print("")
print(available_items)
print(health_points)



# 5. Get All Keys

# 1. To print regular list 
#  list(dictionary_list) 
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

# 2. To print dictionary view object 
#  for (name) in dictionary_list.keys():
#  or name = ditionary_list.keys()
# memory efficient 
# Grace
# Jeffrey
# Sylvia
# Pedro
# Martin
# Dina

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

for users in user_ids.keys():
  print(users) #returns only keys 

print("")
users = user_ids.keys()
print(users)  # dictionary view object
# returns dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
user_list = list(user_ids)
print(user_list) # regular list 
# returns ['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith']

lessons = num_exercises.keys()
print(lessons)




# 6. Get All Values
# dictionary_list.values()
# returns dict_values object 
# if want to print as list, list(dictionary_list.values())

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0 
for exercise in num_exercises.values():
  total_exercises += exercise 
print(total_exercises)


# 7. Get All items
# dictionary_list.items()
# returns dict_list object (key, value)
# for key, value in dictionary_list.items():

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

print("")
print(list(pct_women_in_occupation.items()))
for key, value in pct_women_in_occupation.items():
  print(f"Women make up {value} percent of {key}s")