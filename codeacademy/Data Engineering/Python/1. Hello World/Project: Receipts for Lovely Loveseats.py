#Project:   Receipts for Lovely Loveseats
#Date:      2024.12.26
#Creator:   Jiyun Namm


#Assign values
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."""
lovely_loveseat_price = 254.00

stylish_settee_description="""Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""
stylish_settee_price=180.50

luxurioups_lamp_description="""Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."""
luxurious_lamp_price=52.15

#Sales tax 8.8%
sales_tax=0.088



#First Customer
customer_one_total=0
customer_one_itemization=""
#purchased lovely loveseat 
customer_one_total+=lovely_loveseat_price
customer_one_itemization+=lovely_loveseat_description
#also purchased luxurious lamp
customer_one_total+=luxurious_lamp_price
customer_one_itemization+=luxurioups_lamp_description

#First customer ready to check out 
customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax
print("Customer One Total:" + str(customer_one_total)) #concatenation can only for strings. Therefore put str() around strings 
print("Customer One Items:" + customer_one_itemization)

