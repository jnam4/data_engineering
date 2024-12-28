#Project:   Carly's Clippers
#Date:      2024.12.28
#Creator:   Jiyun Nam

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# want to market her low prices

# 1. Average price of cut
total_price = 0
for i in prices:
  total_price += i
print(total_price)

average_price = total_price / len(hairstyles)
print("Average Haircut Price: "+ str(average_price))

# The owner want to cut all pries by 5 
new_prices = []
for i in prices:
  new_prices.append(i-5)
print(new_prices)


# 2. Revenue
total_revenue = 0
revenue=[]
for i in range(0,len(hairstyles)):
  revenue.append(prices[i] * last_week[i])
  for i in revenue:
    total_revenue += i
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / len(hairstyles)
print(average_daily_revenue)

#Marketing under 30 
print(new_prices)
cuts_under_30=[]
for i in range(len(new_prices)): #
  if new_prices[i] < 30:
    cuts_under_30.append(hairstyles[i])
print(cuts_under_30)
    
