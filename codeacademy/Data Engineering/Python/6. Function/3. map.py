#Chapter6: map
#2024.12.29
#Jiyun Nam
#@codeacademy

# map(function, iterable, [iterable2, iterable3, ...]) 
# Use for memory efficiency, readability, functional programming


def double(x): 
    return x * 2 

numbers = [1, 2, 3, 4, 5] 
doubled_numbers = map(double, numbers) 
#return map object, which is iterator 
print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10] 


# Converting strings to integers 
str_nums = ['1', '2', '3', '4', '5'] 
int_nums = list(map(int, str_nums)) 
print(int_nums)  # Output: [1, 2, 3, 4, 5] 


# Finding the length of strings 
words = ['apple', 'banana', 'cherry'] 
word_lengths = list(map(len, words)) 
print(word_lengths)  # Output: [5, 6, 6] 

# With lambda 
numbers = [1, 2, 3, 4, 5] 
doubled = list(map(lambda x: x * 2, numbers)) 
print(doubled)  # Output: [2, 4, 6, 8, 10] 

# Alternative when
# 1. List Comprehension
# 2. Generator Expression
# 3. For Loops 

doubled = [x * 2 for x in numbers] 



#Practice 
#Sample list of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# Using map with a lambda function to get the length of each name
name_lengths = list(map(lambda x: len(x), names))

# Using map with a defined function to capitalize each name
def capitalize_name(name):
    return name.upper()

capitalized_names = list(map(capitalize_name, names))

# Print the results
print("Original names:", names)
print("Name lengths:", name_lengths)
print("Capitalized names:", capitalized_names)