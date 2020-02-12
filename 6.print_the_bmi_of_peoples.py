#Lab_Exercise_1
"""
Q6. Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names and comments.
When there is a final answer have Python print it to the screen.
A person’s body mass index (BMI) is defined as:
BMI=mass in kg / (height in m)2.

"""

print("This program prints the body mass index(BMI) of the person by getting the mass and height of the person")

massOfPerson = float(input("Enter the mass of the person in Kilogram(Kg)"))
heightOfPerson = float(input("Enter the height of the person in metre(m)"))

BMI = massOfPerson / ((heightOfPerson)**2)


print("The BMI of the person is",BMI,"kg/m^2")








