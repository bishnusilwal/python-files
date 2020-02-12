#Lab_Excersie_2
#Q.10 Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

num1 = int(input("Input the first number"))
num2 = int(input("Input the second number"))
num3 = int(input("Input the third number"))

if (num1 == num2) or (num1 == num3) or (num2 == num3):
    sumOfNum = 0
else:
    sumOfNum = num1 + num2 + num3

print('The sum of numbers is',sumOfNum)