#Chapter4: Review
#2024.12.28
#Jiyun Nam
#@codeacademy

# create list consist of numbers 0-9
single_digits=list(range(0,10))
print(single_digits)

# loop goes thorugh print each one
for digits in single_digits:
  print(digits)

#Squared value
squares=[]

for digits in single_digits:
  digits = digits ** 2
  squares.append(digits)
print(squares)


# List comprehensions-Intro
# new_list = [<expression> for <element> in <collection>]
#Cubes value 
cubes = []
cubes = [digits ** 3 for digits in single_digits]
print(cubes)