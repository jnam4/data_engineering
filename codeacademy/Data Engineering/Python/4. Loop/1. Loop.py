#Chapter4: Loop
#2024.12.28
#Jiyun Nam
#@codeacademy

#Why Loops?
#Can be more efficient 
# Write 10 print() statements below! 
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")
print("This can be so much easier with loops!")


#1.a For Loops-Intro
# will know how many times the loop will need to be
# for <temporary variable> in <collection>:action
# for i in ingredients:
  #print(i)

#Indentation-should be in the body
#Elegant loops-in one line

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]
sport_games = ["football", "hockey", "baseball", "cricket"]

#prints each game in the list board_games
for game in board_games:
  print(game)
#prints each sports in the list sport_games
for sports in sport_games:
  print(sports)


#1.b For Loops-Using Range
#for <temporary variable> in <list of length 6>:
#     print("Learnig Loops!")
promise = "I will finish the python loops module!"
for temp in range(5):
  print(promise)



#2.a While Loops-Intro
#perform set of instructions as long as condition is true

#Indentation-should be in the body
#Elegant loops-in one line 
#command + / => comment

# Your code below: 
print("Start While Loop from 0 to 10")
countdown=0
while countdown <= 10: #0 from 10 
  print("Current countdown"+str(countdown))
  countdown+=1
print("We have liftoff")


print("Start While Loop from 10 to 0")
countdown=10
while countdown >= 0:
  print("Current countdown"+str(countdown))
  countdown-=1
print("We have liftoff")


# Countdown 
countdown = 10
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("We have liftoff!")



#2.b While Loops-Lists
# Lists + Length mix

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
print(ingredients)

length = len(ingredients)
print(length)
index = 0 
while index < length:
  print(ingredients[index])
  index += 1

#your code below
python_topics = ["variables", "control flow", "loops", "modules", "classes"]
print(python_topics)
length = len(python_topics)
index = 0 
while index < length:
  print("I am learning about "+ str(python_topics[index]))
  index += 1



#3. Infinite Looops
# control + c - terminate the program 

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for students in students_period_A:
  students_period_B.append(students)
print(students_period_B)



#4.a Loop Control-Break
# If loop meet the requirements, does not show up after

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
print("Checking the sale list")
#Search "knit dress" and print "found it"
for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
print("End of the search")


# your code below
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    break
print("They have the dog I want!")



#4.b Loop Control-Continue
#Continue use when only want to skip the current iterartion of the loop

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
print(big_number_list)

for i in big_number_list:
  if i <= 0:
    continue
  print(i)


ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
print(ages)

for i in ages:
  if i < 21:
    continue
  print(i)



#5. Nested Loop

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
print(project_teams)
# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)

#Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
#loop through each location:
for location in sales_data:
  #loop thorugh element
  for element in location:
    scoops_sold += element
print(scoops_sold)



#6. List comprehensions-Intro
# new_list = [<expression> for <element> in <collection>]

# Original Way
numbers = [2, -1, 79, 33, -45]
doubled = []

for number in numbers:
  doubled.append(number * 2)

print(doubled)

# It can be expressed to 
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

# Your code:
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)

    
 
#7. List. Comprehensions-Conditions

# Original Way
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []

for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)

print(only_negative_doubled) 

# It can be expressed to 
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0] #conditions come first
print(negative_doubled)

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ] #conditions comes after the expressions but before fore keyword
print(doubled)

numbers = [2, -1, 79, 33, -45]
no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]


# Your code below:
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
# To ride you need to above 161 cm 
can_ride_coaster = [a for a in heights if a > 161]
print(can_ride_coaster)
