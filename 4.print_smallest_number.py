#Lab_Excersie_2
#Q.4 Given three integers, print the smallest one. (Three integers should be user input)

firstNum = int(input("Enter the first number "))
secondNum = int(input("Enter the second number "))
thirdNum = int(input("Enter the third number "))


if firstNum < secondNum and firstNum < thirdNum:
    result = firstNum
elif secondNum < thirdNum :
    result = secondNum
else:
    result = thirdNum

print('The smallet number among',firstNum,",",secondNum,"and",thirdNum," is ",result,"." )
        