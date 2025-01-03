#Chapter9 : String
#2025.01.02
#Jiyun Nam
#@codecademy

# 1. String 
# 'single quotes' "double quotes"
favorite_word = "jiyun"
print(favorite_word)



# 2. list 
# String can be thoguht as a list of characters 
my_name = "jiyun"
first_initial = my_name[0]
print(first_initial)


# 3. Cut me a slice of string 
# string[first_index:last_index]
first_name = "Rodrigo"
last_name = "Villanueva"

# Create a variable by slicing first five letters
new_account = last_name[0:5]
print(new_account)
temp_password = last_name[2:6]
print(temp_password)



# 4. Concatenating String
# combine two existing strings together into new strings
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):
  return first_name[0:3]+last_name[0:3]

new_account = account_generator(first_name, last_name)
print(new_account)



#5. Length of the string 
# len() 

first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  first = len(first_name)
  last = len(last_name)
  first_last_three = first_name[first-3:]
  last_last_three = last_name[last-3:]
  return first_last_three + last_last_three

temp_password = password_generator(first_name, last_name)
print(temp_password)



# 6. Negative Indices 
# list [-1] => start from the back 
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
print(second_to_last)
final_word = company_motto[-4:]
print(final_word)



# 7.Strings are Immutable
# Cannot change4n a string once it is created.
# Mutability -> Data types that are mutable that can be changed 
# Immutable -> Data types, like strings, that are immutable cannot be changed 

first_name = "Bob"
last_name = "Daily"

# first_name[0] = "R" 
# cannot be changed, cause strings are imutable 

fixed_first_name = "R" + first_name[1:]
print(fixed_first_name)



# 8. Escape Characters
# \"something\" -> emphasis 

favorite_fruit_conversation = "He said, \"blueberries are my favorite!\""
print(favorite_fruit_conversation)
# He said, "blueberries are my favorite!"

password = "theycallme\"crazy\"91"
print(password) # theycallme"crazy"91



# 9. Iterating through Strings 
def print_each_letter(word):
  for letter in word:
    print(letter)

favorite_color = "blue"
print_each_letter(favorite_color)
print("")

def get_length(word):
  count = 0 
  for letter in word:
    count += len(letter)
  return count

print(get_length("test"))



# 10. Strings and Conditions - Part.1
def letter_check(word, letter):
  for character in word:
    if character == letter:
      return True
  return False

print(letter_check("strawberry", "a"))



# 11. Strings and Conditons - Part. 2
# letter in word 
print ("e" in "blueberry") # True
print ("e" in "blueberry" and not "e" in "carrot") #True

def contains(big_string, little_string):
  if little_string in big_string:
    return True
  else:
    return False
  
def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return list(common)

print(contains("watermelon", "melon"))
print(common_letters("banana", "cream"))