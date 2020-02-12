#Lab_Excersie_2
#Q.5 For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.

userInput = float(input("Enter the number to check whether the number is positive,negative or zero"))

if userInput == 0:
    result = 'zero'
elif userInput > 0:
    result = 'positive'
else:
    result = 'negative'
print('The number you entered is',result,".")
        