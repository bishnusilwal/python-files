#Lab_Exercise_1
"""
Q10. Write a Python program to convert seconds to day, hour, minutes and seconds.

"""

print("This program will convert seconds to day, hour, minutes and seconds")

givenTime = int(input("Write the second to which you want to convert"))
time = givenTime
day = time // (24*3600) # // Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
time = time % (24*3600) # % Divides and returns the value of the remainder.

hour = time // (3600)
time = time % 3600
minutes = time // 60
time = time % 60
second =time





print("The answer is",day,"days",hour,"hours",minutes,"minutes",second,"seconds")
