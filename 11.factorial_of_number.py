#Lab_Excersie_3
#Q.11 Write a program to find the factorial of a number using functions.

def factNum(num):
    if num == 1:
        return num
    else:
        return num * factNum(num-1) #recursive function

userInput = int(input("Input a number to find out the factorial of that number"))
print(factNum(userInput))
