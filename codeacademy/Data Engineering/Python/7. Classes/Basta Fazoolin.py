#Project:   Basta Fazoolin
#Date:      2025.01.01
#Creator:   Jiyun Nam

# Commnent
# 2025.01.01
# - Need to make interactive version

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self): 
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
    total = 0 
    purchased_list = []

    
    for items in purchased_items:
      if items in self.items:
        total += self.items[items]
        purchased_list.append(f"{items}")

      else:
        print (f"Item {items} does not find in the list.")
    print(f"Total price: ${total}")
    print((f"Purcahsed items: {purchased_list}"))

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menu = menus

  def __repr__(self):
    return f"Franchise is located at {self.address}"
  
  def available_menu(self, time):
    available = []
    for menu in self.menu:
      if menu.start_time <= time <= menu.end_time:
        available.append(menu)
      # print(menu) - ex:"Brunch menu availalbe from 3pm to 6pm"
    menu_names = ", ".join(menu.name for menu in available) #Extract name by , 
    print(f"Menu available at {time}: {menu_names}")

    for menu in available:
      print(f"Availalble menu : {menu}")
      for item, price in menu.items.items():
        print(f"- {item}: ${price:.2f}")
    


    return available


class Business:
  def __init__(self, name, franchise):
    self.name = name
    self.franchise = franchise
  
  def __repr__(self):
    return f"Business Name: {self.name}"



# Instantiation-Assign variables
#menus
brunch = Menu("brunch", 
{'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 
"11am", "4pm")

early_bird = Menu("early-brid", 
{'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,},
"3pm", "6pm")

dinner = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 
"5pm", "11pm")

kids = Menu("kid", 
{'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00},
"11am", "9pm")

take_a_arepa = Menu("Take a'Arepa", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, "10am", "8pm")


#franchise location
menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
arepa_franchise = Franchise("189 Fitzgerald Avenue", [take_a_arepa]) #are_franchise sell only take_a_arepa

# print(brunch)
# print(early_bird)
# print(dinner)
# print(kids)

# print(flagship_store)
# print(new_installment)
# print(arepa_franchise)

#Check purchased items in the menu and calculate the bill 
purchased_items = ['espresso', 'caesar salad']
total_bill_for_dinner = dinner.calculate_bill(purchased_items)

purchased_items= ['drink', 
 'mushroom ravioli (vegan)']
total_bill_for_early_bird = early_bird.calculate_bill(purchased_items)

# Check available menus at the flagship store
time = "5pm"
available_menus = flagship_store.available_menu(time)

# Create the business
basta_fazoolin = Business(
    "Basta Fazoolin' with my Heart",
    [flagship_store, new_installment, arepa_franchise])

# Display the name of the business
# Check with the business
print(basta_fazoolin)
print(basta_fazoolin.franchise) # print it as list
for franchise in basta_fazoolin.franchise:
    print(franchise) # print it as seperately 

time = "12pm"
print(f"Checking available menus at {flagship_store.address} at {time}:")
flagship_store.available_menu(time)

#Check area_franchise
print(f"Menus at {arepa_franchise.address}:")
time = "2pm"
arepa_franchise.available_menu(time)

take_a_arepa.calculate_bill(['arepa pabellon', 'guayanes arepa'])

