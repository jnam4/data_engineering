#Chapter3: Slicing
#2024.12.27
#Jiyun Nam
#@codeacademy


#1. lists[start:end+1]
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:4]

# Your code below: 
print(beginning)
#modifying
beginning = suitcase[0:2]
print(beginning) #['shirt', 'shirt']
middle = suitcase[2:4] 
print(middle) #['pants', 'pants']



#2. lists[:n], lists[-n:]
#lists[:n]-give from start to n 
#lists[-n:]-give back n from the end
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
#containing final two elements
last_two_elements=suitcase[-2:]
print(last_two_elements)
#containing all but the last three elements
slice_off_last_three=suitcase[:-3]
print(slice_off_last_three)



#3. letters.count("letter")
#count how many letters in the lists 
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
#How many students voted for Jake
jake_votes=votes.count("Jake")
print(jake_votes)



#4. list.sort(a)
#list.sort(a)-sort the list of a in alphabetical order. 
#list.sort(reverse=True)-descending order

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
print(names)

# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort() #sorted cities are "cities", not "cities.sort()"
#In Reverse Order
cities.sort(reverse=True)
print(cities)



#5. sorted()
#sorted() and .sort() are different 
#comes before a list
#generates a new list

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
# Your code below:
games_sorted = sorted(games) #generated new lists with ascending order for the games. 
print(games_sorted)
print(games)



#Review
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

#how many items are in the inventory?
inventory_len=len(inventory)
print(inventory_len)

#select first element
first=inventory[0]
print(first)
#select last element
last=inventory[-1]
print(last)

#index 2 and up to, but no including, index 6 
inventory_2_6=inventory[2:6]
print(inventory_2_6)

#select first 3 items of inventory
first_3=inventory[0:3]
print(first_3)

#'twin bed's are in 'inventory'?
twin_beds=inventory.count("twin bed")
print(twin_beds)

#remove 5th element
removed_item=inventory.pop(4)
print(removed_item)

#add new item called "19th Century Bed Frame" as the 11th element
inventory.insert(10, "19th Century Bed Frame")
print(inventory)

#sort invnetory
inventory.sort()
print(inventory)

