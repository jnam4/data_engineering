#Project:   Gradebook
#Date:      2024.12.27
#Creator:   Jiyun Nam

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]


#how many times $2 occurs? 
num_two_dollar_slices=prices.count(2)

#length of the toppings 
num_pizzas=len(toppings)
print("We sell "+str(num_pizzas)+" different kinds of pizza!")


#two dimensional list
#not yet learned loop
pizza_and_prices=[[2, "pepperoni"], [6, "pineapple"], [1,"cheeses"], [3,"sausage"], [2,"anchovies"], [7, "anchovies"], [2, "mushrooms"]]

#sort increasing price in ascending order
pizza_and_prices.sort()
print(pizza_and_prices)

cheapest_pizza=pizza_and_prices[0]
priciest_pizza=pizza_and_prices[-1]

#The man takes the most expensive pieces
pizza_and_prices.pop()
print(pizza_and_prices)

#Since no longer an "anchovies" pizza, you want to add a new topping called "peppers"
pizza_and_prices.insert(0, [2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

#store 3 lowest cost pizzas
three_cheapest=pizza_and_prices[0:3]
print(three_cheapest)