#Lab_Exercise_1
"""
Q9. Write a python program to find sum of the first n positive integers.
sum = (n*(n+1))/2

"""
print("This program will compute the sum of first n positive integers")

lastNum = int(input("Enter the number to which you want to find sum"))
n = lastNum

sumOfNumbers = (n*(n+1))/2

print("The sum of first",n,"positive integers is",sumOfNumbers)
