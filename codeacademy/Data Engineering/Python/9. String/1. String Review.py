#Chapter9 : String Review
#2025.01.02
#Jiyun Nam
#@codecademy


# create two funciton: username_generator, password_generator

first_name = "Abe"
last_name = "Simpson"

def username_generator(first_name, last_name):
  user_name = first_name[0:3] + last_name[0:4]
  return user_name
test1 = username_generator(first_name, last_name)
print(test1)

def password_generator(user_name):
  return user_name[-1] + user_name[:-1] 
print(password_generator(test1))

def password_g(user_name):
  password = ""
  print(len(user_name))
  for i in range(0, len(user_name)):
    password += user_name[i-1]
  return password

print(password_g(test1))

  