#Chapter6: lambda
#2024.12.28
#Jiyun Nam
#@codeacademy

# Regular function 
def square(x): 
    return x ** 2 
  
# Lambda function 
square_lambda = lambda x: x ** 2 
# lambda [arguments]: [expression] 

# Mostly used as arguments to higher-order-functions such as map(), filter(), sorted()
# Higher-order-functions: can accept other functions, such as lambda functions, as arguments

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a lambda function to filter out odd numbers
# filer()-use when make a list that meet the conditions through lambda 
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Use a lambda function to square each number
# map()-use when make a list that apply by lambda 
squares = list(map(lambda x: x ** 2, numbers))

# Print the results
print("Original numbers:", numbers)
print("Even numbers:", evens)
print("Squared numbers:", squares)

# Try creating your own lambda function!
# Uncomment and modify the line below:
# your_result = list(map(lambda x: # Your lambda function here, numbers))
# print("Your result:", your_result)