#Chapter7 : Type
#2024.12.30
#Jiyun Nam
#@codecademy


# 1. Types
# type(variables) -> <class type>
a_string = "Cool String"
an_int = 12

print(type(a_string))
# prints "<class 'str'>"
print(type(an_int))
# prints "<class 'int'>"

# -- Your Code Below -- 
print(type(5)) # <class 'int'>
my_dict = {}
print(type(my_dict)) # <class 'dict'>
my_list = [1,2]
print(type(my_list)) # <class 'list'>



# 2. Class
# Describes the kinds of information that class will hold and how programmer will interact with Data
# Capitalizing the names for classes for easier to identify
# However, there are seperate convention or bulltin names

class CoolClass: #created a class and named it CoolClass 
  pass

# -- Your code below -- 
class Facade :
  pass



# 3. Instantiation 
# A class must be instantiated. 
# looks ike calling a function 
# cool_instance = CoolClass()
# variable = cool_instance 
# class = CoolClass()

# eventhough it is variable, but it is also called "object"

# -- Your code below -- 
class Facade:
  pass 

facade_1 = Facade()



# 4. Object-Oriented Programming 
# Instantiation takes class and turns into object 
# type() does opposite. 

# Defining class & creating objects -> Object Oriented Programming (OOP)

# a. Defining Class 
class Facade:
  pass 

# b. Instantation -> class and turns into object
facade_1 = Facade()
# c. Object-Oriented Programming -> take object into class 
facade_1_type = type(facade_1)
print(facade_1_type)
# Result : <class '__main__.Facade'>
# __main__ means "this current file that we're running "



# 5. Class Vairables 
# class instance -> class variables 
# class variable is a variable that's the same for every instance of class

# a. Defining Class
class Musician:
  title = "Rockstar" #title attribute 

# b. Instantiation -> Assign variables 
drummer = Musician()
guitarist = Musician()
print(drummer.title) #print "Rockstar"
print(guitarist.title) #print "Rockstar"

# class Musicians
# attribute title 
# variables drummer, guitarist

# -- Your Code Below -- 