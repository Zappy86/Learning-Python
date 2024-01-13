from math import sqrt
from sys import exit

a = float(input("A: "))

if(a == 0):
    exit("That is not a quadratic.")

b = float(input("B: "))
c = float(input("C: "))

discriminant = (b*b) + (-4*a*c)

print("Discriminant: " + str(discriminant))

if(discriminant < 0): print("No real roots.")
elif(discriminant == 0): print("X = " + str(-b/(2*a)))
elif(discriminant > 0): print("X = " + str((-b + sqrt(discriminant))/(2*a)) + ", " + str((-b - sqrt(discriminant))/(2*a)))
else: print("Error")