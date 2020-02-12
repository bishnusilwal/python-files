#Lab_Exercise_1
"""
Q5. A school decided to replace the desks in three classrooms. Each desk sits two students.
Given the number of students in each class, print the smallest possible number of desks that can be purchased.
The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
The second group has 21 students, so they can get by with no fewer than 11 desks.
11 desks are also enough for the third group of 22 students. So, we need 32 desks in total.
"""
import math
print("This program will ask number of students in each classes a,b and c and then calculate the total desks needed")

ClassA = int(input("How many student are there in Class-a"))
ClassB = int(input("How many student are there in Class-b"))
ClassC = int(input("How many student are there in Class-c"))


deskClassA = math.ceil(ClassA/2)
deskClassB = math.ceil(ClassB/2)
deskClassC = math.ceil(ClassC/2)

totalDeskRequired = deskClassA + deskClassB + deskClassC


print("The smallest possible number of desks that can be purchased is",totalDeskRequired,"desks.")







