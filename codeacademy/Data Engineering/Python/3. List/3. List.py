#Chapter3: List
#2024.12.27
#Jiyun Nam
#@codeacademy


#1. List
#Collecton of data in sequential order #[a,b,c,d] 
#Able to contain any type 
#empty => []

heights = [61, 70, 67, 64, 65]
broken_heights = [65, 71, 59, 62]



#2. List Methods 
#list_name.method()
#example_list.append() => add element 
#example_list.remove() => remove element 
#.remove() method removes the first matching element in a list.

example_list = [1, 2, 3, 4]
#Using Append => add the element 
example_list.append(5)
print(example_list)
#Using Remove => remove the element 
example_list.remove(5)
print(example_list)



#3. Growing List: Append 
#Take only one element at the time 
orders = ["daisies", "periwinkle"]
print(orders)

#received new order
orders.append("tulips")
#another new order
orders.append("roses")
print(orders)




#4. Growing List: Plus(+) 
#Plus(+) can be used between lists 
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
#new orders
new_orders = ["lilac", "iris"]

orders_combined= orders + new_orders 
broken_prices = [5, 3, 4, 5, 4] + [4]

#check
print(orders_combined)
print(broken_prices)



#5.a Accessing List Elements:Positive Index
#list_name[number of elements-1]
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four=employees[3]
#print(employees[8]) 
#Bring indexerror - element does not exists



#5.b Accessing List elements:Negative Index
#list_name[-1] => count in the another way
shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
#check
print(index5_element)
print(last_element)



#6. Modifiying List Elements:
#name_list[element number] = "Texts"
garden_waitlist=["Jiho", "Adam", "Sonny", "Alisha"]
#Replace Adam with Calla
garden_waitlist[1]="Calla"
print(garden_waitlist)
#Replace Alisha with Alex using negative index
garden_waitlist[-1]="Alex"
print(garden_waitlist)



#7. Shrinking a List:Remove
#name_list.remove()

order_list=["Celery","Orange Juice","Orange","Flatbread"]
print(order_list)
#Remove flatbread
order_list.remove("Flatbread")
print(order_list)

new_store_order_list=["Orange","Apple","Mango","Broccoli","Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
#new_store_order_list.remove("Onions") => ValueError



#8. 2D Lists (Two dimensional)
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
ages=[["Aaron", 15], ["Dhruti", 16]]



#9. Accessing 2D Lists
class_name_test = [["Jenny", 90],["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)
#Sam
sams_score = class_name_test[2][1]
print(sams_score)
#Ellie (negative index)
ellies_score = class_name_test[-1][-1]
print(ellies_score)



#10. Modifying 2D Lists
incoming_class=[["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
#Madision move to the 8th grade
incoming_class[2][2]=8
print(incoming_class)
#Kenny called by his nickname "Ken". Modifying with negative index
incoming_class[-3][-3]="Ken"
print(incoming_class)



#Review
#Create & Modifying
first_names=["Ainsley", "Ben", "Chani", "Depak"]
preferred_size=["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)
#2D
customer_data=[["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)

#Chani:Shipping preference to False
customer_data[2][2]=False
#Ben:Remove shipping options
customer_data[1].remove(False)
#New customer 
new_data = [["Amit", "Large", True], ["Karim", "X-Large", False]]
customer_data_final = customer_data + new_data
print(customer_data_final)