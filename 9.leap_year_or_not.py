#Lab_Excersie_2
#Q.3 Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’.
#Hint: • a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
#• a year is always a leap year if its number is exactly divisible by 400

currentYear = int(input('Enter the year to find whether the year is leap year or not.'))


if currentYear % 4 == 0:
    if currentYear % 100 ==0:
        if currentYear % 400 == 0:
            result = "LEAP YEAR"
        else:
            result = "COMMON YEAR"
    else:
        result = "LEAP YEAR"
else:
    result = "COMMON YEAR"
 
print("The year ",currentYear,"is a",result)