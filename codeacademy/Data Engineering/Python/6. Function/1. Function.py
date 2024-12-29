#Chapter6: Function
#2024.12.28
#Jiyun Nam
#@codeacademy



#1. Defining a Function 
# def function_name():
#     # functions tasks 

def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")



#2. Calling a Function 
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

# Call your function here:
directions_to_timesSq()



#3. Whitespace & Execution Flow

print("Checking the weather for you!")
def weather_check():
  print("Looks great outside! Enjoy your trip.")
  print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()



#4. Parameters & Arguments
# Parameter-name defined in the parenthesis of the function and can be used in the body 
# def trip_welcome(parameter):
#     print("a"+parameter) 

# Argument-data passed in when we call the function, which is then assigned to the parameter name
# trip_welcome("empire state_building")
# No argument: function()


# Your code below:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location) #Parameter-location

generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station") #Arguments-"Central Park" "GCS"


#5. Multiple Parameters
# Write your code below: 
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  return trip_total

# Call your function
print(calculate_expenses(200, 100, 100, 5))



#6. Types of Arguments
# Positional arguments-arguments that can be called by their positions in the function definition
# Keyword arguments-arguments that can be called by their name
# Default arguments-arguments that are given default values 

# Write your code below:
# give the final_destination parameter a default value
# final_destination would print out eventhough we didn't print it out 

def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First we will stop in "
  + first_destination + ", then "
  + second_destination + ", and lastly "
  + final_destination)


trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")

#Keyword argument
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")

#Positional argument
trip_planner("Brooklyn", "Queens")



#7. Built-in VS User Defined Functions 

tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
# Built-in function
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)

rounded_price = round(tshirt_price,1)
print(rounded_price)



#8. Variable Access
# variables should be define in the firsthand, before writing in the body 

# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"

def print_count_locations():
  print(favorite_locations)
  print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations() 



#9. Returns
# Store values 
current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 

def deduct_expense(budget, expense):
  return budget - expense 

shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)
print(new_budget_after_shirt)

print_remaining_budget(new_budget_after_shirt)



#10. Multiple Returns 

def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1)
print(most_popular2)
print(most_popular3)