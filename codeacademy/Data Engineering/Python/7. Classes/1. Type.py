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
# Create a Grade class with a class attribute .minimum_passing equal to 65.
class Grade:
  minimum_passing = 65



# 6. Methods
# defined as part of a class
# 1st argument - method always object that calling method  -> name as 'self'

class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."
print(Dog)

# -- Your code below -- 
class Rules:
  def washing_brushes(self):
    return("Point bristles towards the basin while washing your brushes.")



# 7. Methods with Arguments

class DistanceConverter:
  kms_in_a_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_in_a_mile
    # take 2 arguments
    # only pass 2 miles, becuase self is passed and refers to the object converter 

converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"

# -- Your code below --
class Circle:
    pi = 3.14  # Class variable: pi

    def area(self, radius):
        """Calculate the area of the circle based on the radius."""
        return self.pi * (radius ** 2)


circle = Circle()  # Create an instance of Circle

# Diameters of the objects
pizza = 12
table = 36
round_table = 11460
diameters = [pizza, table, round_table]

# Convert diameters to radii
radii = list(map(lambda x: x / 2, diameters))
print("Radii:", radii)

# Calculate areas for each radius
areas = list(map(circle.area, radii))
print("Areas:", areas)

# Assign each area to its respective variable
pizza_area = areas[0]
teaching_table_area = areas[1]
round_room_area = areas[2]

# Print the results
print(f"Pizza Area: {pizza_area}") #without print("Pizza Area: " + str(pizza_area))
print(f"Teaching Table Area: {teaching_table_area}")
print(f"Round Room Area: {round_room_area}")



# 8. Constructors
# dunder methods 
# a. __init__() 
#   initialize a newly created object
#   called every time the class is instantiated

class Shouter:
  def __init__(self):
    print("HELLO?!")

shout1 = Shouter()
# prints "HELLO?!"

shout2 = Shouter()
# prints "HELLO?!"


class Shouter:
  def __init__(self, phrase):
    # make sure phrase is a string
    if type(phrase) == str:

      # then shout it out
      print(phrase.upper())

shout1 = Shouter("shout")
# prints "SHOUT"

shout2 = Shouter("shout")
# prints "SHOUT"

shout3 = Shouter("let it all out")
# prints "LET IT ALL OUT"


class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    self.diameter = diameter #new circle is created
    print (f"New circle with diameter: {diameter}.")

teaching_table=Circle(36)



# 9. Instance Varaibels:

class Store:
  def __init__(self, store_name):
    self.store_name = store_name 

#create two objects from this store class
alternative_rocks = Store("Alternative Rocks")
isabelles_ices = Store("Isabelle's Ice")

print(alternative_rocks.store_name)
print(isabelles_ices.store_name)


print(alternative_rocks.__dict__)  # {'store_name': 'Alternative Rocks'}
print(isabelles_ices.__dict__)    # {'store_name': "Isabelle's Ices"}



#10. Attribute Functions 
class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
  #no fake_attributes that may cause AttributeError
except AttributeError:
  # If we attemp to access an attribute that is netiher class variable or instance variable of object
  print("This text gets printed!")

# prints "This text gets printed!"


hasattr(object, "attribute")
# returns False
# testing if object is exist. If exists, type "attribute"

getattr(object, "attribute", "object")
# object : the object whose attriubte we want to evaluate
# attribute : name of attribute we want to evaluate
# default : value return if the attribute does not exist, but optional

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value
# "other fake attribute" isn't a real attribute on attributeless. So returns 800. 


# -- Your code below -- 
can_we_count_it = [{'s': False}, 
"sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute : (")



# 11. Self
class SearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url

  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
    # Define secure() method to take just one argument, self. 
    # Access 1) class variable - self.secure_preix 2) instance variable - self.url to return a securl URL

codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())
# prints "https://www.codecademy.com"

print(wikipedia.secure())
# prints "https://www.wikipedia.org"

# -- Your Code Below -- 
class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter/2

  def circumference(self):
    return (2 * self.pi * self.radius)

medium_pizza = Circle(12) #take 12 as diameter and put it in def__init__(self, diameter)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference()) #take radius into circumference(self)
print(teaching_table.circumference())
print(round_room.circumference())



# 8. Everything is an Object
# dir() is short for directory and offers as organized presentation of object attributes

print(dir(5))

def this_function_is_an_object(safe):
  everything = 5
  return safe.everything

print(dir(this_function_is_an_object))



# 9. String Representation

class Employee():
  def __init__(self, name):
    self.name = name

argus = Employee("Argus Filch")
print(argus)
# prints "<__main__.Employee object at 0x104e88390>"

class Employee():
  def __init__(self, name):
    self.name = name #initialize newly created object

  def __repr__(self): 
    return self.name
    # name attribute of the object into string

argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"


# -- Your code below -- 

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return f"Circle with radius {self.radius}"
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)