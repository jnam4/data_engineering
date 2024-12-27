#Project:   Sal's Shipping
#Date:      2024.12.27
#Creator:   Jiyun Nam

weight = float(input("How weight it is?"))

#Ground shipping
if weight <= 2:
  costs=weight*1.50+20.00
elif weight >= 2 and weight <= 6:
  costs=weight*3.00+20.00
elif weight >=6 and weight <= 10:
  costs=weight*4.00+20.00
else:
  costs=weight*4.75+20.00
print("Cost of the ground shipping is " + str(costs))

#Ground Shipping Premium
costs_P=125 #Flat rate
print("Cost of the ground shipping premium is "+str(costs_P))

#Ground Shipping Premium
if weight <= 2:
  Dcosts=weight*4.50
elif weight >=2 and weight <=6:
  Dcosts=weight*9.00
elif weight >=6 and weight <=10:
  Dcosts=weight*12.00
else:
  Dcosts=weight*14.25
print("Cost of the Drone shipping  is " + str(Dcosts))
