#Lab_Exercise_1
"""
Q8. Write a Python program which accepts the radius of a circle from the user and compute the area.
(area of circle = PI * r2)

"""
import math
print("In this program we will print the area of circle by getting radius input from user")

radiusOfCircle = float(input("What is the radius of the circle"))
PI = math.pi
areaOfCircle = PI *(radiusOfCircle ** 2)

print("The area of circle having radius",radiusOfCircle,"is ",areaOfCircle)
