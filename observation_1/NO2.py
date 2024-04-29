#2.	A program that computes the real roots of a quadratic equation using an if- el if- el se.
import math

a = float(input("Please enter a"))
b = float(input("Please enter b"))
c = float(input("Please enter c"))

if b**2 - 4*a*c < 0:
    print("No real roots")
elif 2*a == 0:
    print("Division cannot be zero")
else:
    print("Root 1:", (-b+math.sqrt(b**2-4*a*c))/(2*a))
    print("Root 2:", (-b-math.sqrt(b**2-4*a*c))/(2*a))