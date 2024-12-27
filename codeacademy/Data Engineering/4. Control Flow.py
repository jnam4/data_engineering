#Chapter2:  Control Flow 
#Date:      2024.12.26
#Author:    Jiyun Nam
#@codeacademy

#1. Boolean
#Statement that can either True / False
#"The Earth revolves around the Sun."
first_statement = "Yes"
#"The Moon is made of cheese."
second_statement = "Yes"
#"Chocolate ice cream tastes better than vanilla."
third_statement = "No"



#2. Relational Operators
#Compare two values, and return True or False
#Logial operators are used to combined multiple boolean expressions 
# equals to operator (==)
# not equals to operator (!=)
first_expression = 2*2 == 2+2
print(first_expression)

second_expression = 3+3 != 3*3
print(second_expression)

third_expression = 3*3 == '9'
print(third_expression)



#3. Boolean Variables 
#True & False are the only "bool" types 
#Any variable that assigned one of these values = boolean variable 
my_baby_bool = "true"
print(type(my_baby_bool)) #It's string
my_baby_bool_two = True
print(type(my_baby_bool_two)) #It's bool



#4. If Statement
#If [a], then [b] => if a: print (b)
# Enter a user name here, make sure to make it a string
#If name is Dave
user_name = "Dave"
if user_name == "Dave":
  print("Get off my computer Dave!")
#If dave log in angela_catlady_87
user_name = "angela_catlady_87"
if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")



#5 Relational Operators 2
# > greater than, 
# >= greater than or equal to 
# < less than
# <= less than or equal to 
x = 20
y = 20
# Write the first if statement here:
# Check x and y is equal 
if x == y:
  print("These numbers are the same")
credits = 120
# Write the second if statement here:
# Check if student has enough credits to graduate (minimum credits are 120)
if credits >= 120:
  print("You have enough credits to graduate!")



#6.1 Boolean Operators: and
#and: combines two boolean. True True => True
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_one)
print(statement_two)

credits = 120
gpa = 3.4
if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")



#6.2 Boolean Operators: or
#or: combines two expressions into larger expression that is True if either components is True 
#if one is true, it is true
statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
print(statement_one)
print(statement_two)

credits = 118
gpa = 2.0
if credits>=120 or gpa>=2.0:
  print("You have met at least one of the requirements."
)



#6.3 Boolean Operators:not
#not True == False
#not False == True
statement_one = not (4 + 5 <= 9)
statement_two = not (8 * 2) != 20 - 4
print(statement_one)
print(statement_two)

credits = 120
gpa = 1.8
if not credits>=120:
  print("You do not have enough credits to graduate.")
if not gpa >=2.0:
  print("Your GPA is not high enough to graduate.")
if not credits>=120 and not gpa>=2.0:
  print("You do not meet either requirement to graduate!")



#7 else
#use when certain conditions are not met
#use it with "If"

credits = 120
gpa = 1.9
if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")



#8. Else if 
#elif - use it when multiple conditions

grade = 86
if grade >= 90:
  print("A")
elif grade >=80:
   print("B")
elif grade >=70:
    print("C")
elif grade >=60:
    print("D")
else:
    print("F")


#Review 
#space.py
print("I have information for the following planets:\n")
print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 3

# Write an if statement below:

if planet == 1:
  weight = weight * 0.91
elif planet == 2:
  weight = weight * 0.38
elif planet == 3:
  weight = weight * 2.34
elif planet == 4:
  weight = weight * 1.06
elif planet == 5:
  weight = weight * 0.92
elif planet == 6:
  weight = weight * 1.19

print("The planet number is", planet, "and your weight:", weight)
