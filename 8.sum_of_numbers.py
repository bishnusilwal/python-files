#Lab_Excersie_2
#Q.8 Given a three-digit number. Find the sum of its digits.

userInput1 = int(input("Input the number"))

strNum = str(userInput1)

sumOfNumbers = int(strNum[0]) + int(strNum[1]) + int(strNum[2])

print('The sum of numbers is ',sumOfNumbers,".")
        