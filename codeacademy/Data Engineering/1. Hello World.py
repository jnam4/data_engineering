#Chapter1: Hello World
#2024.12.26
#Jiyun Nam
#@codeacademyy


#1. Print : print ("")
print("hello world")
#2. Comments: # - Docuentation purpose
#3. String: '', "" - Does not matter
#4. Assign: = 
#5. Error
    #a.SyntaxError - Mixture of ",'
    #b.NameError -try to print single world, but no quotations 



#6. Numbers
##integer: ex)5, 10, 200
##float: ex)1.2, 3.45, 7.802
###Define the release and runtime integer variables below:
release_year = 2020
runtime = 180
###Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 8.2



#7. Calculations
#print 25*68+13/28
print(25*68+13/28)



#8. Change Numbers
#Create two variablses:quilt_width, quilt_length where should be 8 squares wide and 12 suqares long 
quilt_width=8
quilt_length=12
#Squares quilt 
print(quilt_width*quilt_length)
#Quilt should be only 8 quares long. Replace it 
quilt_length=8
print(quilt_width*quilt_length)



#9. Exponents
# Calculation of squares for: ** same as ^ 
# 6x6 quilt 
print(6 ** 2)
# 7x7 quilt
print(7 ** 2)
# 8x8 quilt
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
#Since each person is requesting 6 and 6 people
# 6*6*6*6
print (6 ** 4)



#10. Modulo 
# % gives remainder of a division calculation 
# Online shop where 10th customers get 10% off off their next order. 
# First order of the day #269! Does people get coupon at the end? 
first_order_remainder = 269%10
print(first_order_remainder)
first_order_coupon = "no"
print(first_order_coupon)
# Second order of the day #270!
second_order_remainder = 270%10
print(second_order_remainder)
second_order_coupon = "yes"
print(second_order_coupon)



#11 Concatenation 
#Using + to combine strings  #only strings. If I want to use int=> str(int)
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."
# Define message below:
message = string1+string2+string3+string4+string5+string6
#print(message)
print(message)



#12 Plus Equals 
#+,-
total_price = 0
new_sneakers = 50.00
total_price += new_sneakers
nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater
total_price += fun_books
print("The total price is", total_price)



#13. Multi-line Strings
# Assign the string here
to_you="""Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""
print(to_you)


#14. Wrap up 
my_age=25
half_my_age=25/2
greeting="It was pleasure to meet you."
name="Jiyun Nam"
greeting_with_name=greeting + " " + name
print(greeting_with_name)



