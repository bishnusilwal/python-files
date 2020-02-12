#Lab_Excersie_3
#Q.1 Write a Python function to find the Max of three numbers.

b= int(input('input the first number'))
a = int(input('input the second number'))
c = int(input('input the third number'))

def maxNum(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num2):
        result = num1
    elif num2 >= num3:
        result = num2
    else:
        result = num3
    print('The maximum number among the entered number is',result)

maxNum(a,b,c)
