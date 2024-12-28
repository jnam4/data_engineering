#Project:   Time Traveler's Toolkit
#Date:      2024.12.28
#Creator:   Jiyun Nam


from datetime import datetime as dt
from decimal import Decimal 
from random import randint
from random import choice 


def generate_time_travel_message(year, destination, cost):
  print("Pack your bags! You're traveling to Korea-"+ destination + " in the year " + str(year) + ". The cost of this trip will be $" + str(cost))


current_time = dt.now()
current_year = dt.now().year
print("Current time is " + str(current_time))
print("As well, the current year is " + str(current_year))

base_costs = Decimal(input("What is the costs per year?"))
print("So the current base costs per year is " + str(base_costs))

know_year = input("Do you know which year do you want to go? yes/no ").strip().lower()

if know_year == "yes": #Know where to go
  while True: 
   planning_year = int(input("Which year do you want to go?"))
   if planning_year >= current_year: 
    break
   else: #plannning_year < current_year should go again through loop
    print("It should be after the current year. Type it again. What is the planning year? ")
else: #Don't know where to go. Assume that we are leaving any year in 60 years, plan.
  planning_year=randint(current_year,current_year+60)
  print("Assuming that we are leaving at " + str(planning_year))
  
total_costs = base_costs + (base_costs * (planning_year - current_year))

know_destination = input("Do you know where to go? yes/no ").strip().lower()
if know_destination == "yes":
  destination = str(input("Where do you want to go as destination?"))
else:
  # Randomly select a destination from the list
  destination = choice([
    "Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Ulsan", "Suwon",
     "Changwon", "Sejong", "Gyeongju", "Jeonju", "Cheongju", "Pohang", "Jeju City",
     "Gimhae", "Andong", "Tongyeong", "Sokcho", "Yeosu", "Gunsan", "Mokpo"
    ])
generate_time_travel_message(planning_year, destination, total_costs)