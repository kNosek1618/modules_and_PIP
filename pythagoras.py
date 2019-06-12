import math
side1 = input("Enter first side: ")
side2 = input("Enter second side: ")
hypotenuse = int(side1) * int(side1) + int(side2) * int(side2)



print("hypotenuse of triangle is " + str(math.sqrt(hypotenuse)))
