#Lab_Exercise_1
"""
Q3. N students take K apples and distribute them among each other evenly. 
The remaining (the undivisible) part remains in the basket. How many apples will each single student get?
How many apples will remain in the basket? The program reads the numbers N and K.
It should print the two answers for the questions above.
"""

print("This program distributes the K no. of apples to N no. of students evenly and also prints the remaining number of apples in the basket")

noOfStudents = int(input("Enter the total no. of students"))
noOfApples = int(input("Enter the total number of apples in basket"))

evenlyAmongStudents = int(noOfApples/noOfStudents)
remainedApples = noOfApples-(evenlyAmongStudents*noOfStudents)

print("The total apples",noOfApples,"was distributed among ",noOfStudents," number of students")
print("Each students got equal number of apples which is",evenlyAmongStudents,"apples")
print("The remaining apples or the undivisible apples that remains in the basket is",remainedApples)




