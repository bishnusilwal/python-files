#Lab_Excersie_2
#Q.3 Check whether the user input number is even or odd and display it to user.

userInput = int(input("Enter the number to check whether the number is odd or even"))

if userInput % 2 == 0:
    result = 'even'
else:
    result = 'odd'

print('The number you entered ',userInput," is ",result,".")
        