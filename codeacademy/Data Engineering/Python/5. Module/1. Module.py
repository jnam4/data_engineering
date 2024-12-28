#Chapter5: Module
#2024.12.28
#Jiyun Nam
#@codeacademy

# Allow us to package code into files or sets-called "modules"
# from <module_name> import <object_name>

# 1. Intro
# Import datetime from datetime below:
from datetime import datetime
current_time = datetime.now()
print(current_time)





# 2. Random 
# random.choice() - takes a list as an argument and returns a nmber from list 
# random.randit() - takes two numbers a s arguments and generates random number between two numbers

# Import random below:
# import the random library 
import random

# Create random_list below:
random_list = []
for i in range(101):
  random_list.append(random.randint(1,100))
print(random_list)
  
# Print randomer_number below:
randomer_number = random.choice(random_list)
print(randomer_number)





#3. Namespaces 
# from <module_name> import <object_name> as <name you pick>
# random.sample(list, k) - takes a list(range)and randomly selects k items from it
#new_list = random.sample(list, k)

from matplotlib import pyplot as plt
import random

#for example:
nums = [1, 2, 3, 4, 5]
sample_nums = random.sample(nums, 3)
print(sample_nums) # 2, 5, 1


# Add your code below:
numbers_a = range(1,13) #1 to 12
numbers_b = random.sample(numbers_a, 12)
print(numbers_b)

#plot these numbers
plt.plot(numbers_b)
plt.show()





#4. Decimals 
from decimal import Decimal 

# Fix the floating point math below:
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)





#5. Python Files and Scope
# Scope apples to varaiables, classes, files
# Files are modules - access thorugh 'import'

#libary.py 에는
# Add your always_three() function below:
def always_three():
  return 3

# Import library below:
#from library import always_three
# Call your function below:
print(always_three())




