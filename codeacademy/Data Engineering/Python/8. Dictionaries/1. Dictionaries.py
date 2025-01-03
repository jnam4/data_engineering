#Chapter8 : Dictionaries
#2025.01.01
#Jiyun Nam
#@codecademy


# 1. Introduction 
# dictionary : unordered set of {[key:value], [key:value], ...}

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}
print(sensors)

# Make a Dictionary
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print(translations)



# 2. Empty Dictionary
my_empty_dictionary = {}

# 3. Add A Key
# dictionary[key] = value

animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)



# 4. Add Multiple Keys
# use dicitonary.update() method 

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
#add multiple keys
user_ids.update({"theLooper" : 138475, "stringQueen":85739})
print(user_ids)



# 5. Overwrite Values 

menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)

oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
# Add the key "Supporting Actress" and set value to "Violas Davis"
oscar_winners["Supporting Actress"] = "Viola Davis"
# Change 
oscar_winners["Best Picture"] = "Moonlight"



# 6. Dict Comprehensnions 
# zipped_list = zip(list1, list2)
# Create a dictionary using a dict comprehension 
# dict_comprehension = {key:value for key, valaue in zipped_list}

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

print(drinks_to_caffeine)