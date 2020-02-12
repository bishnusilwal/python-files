#Lab_Excersie_3
#Q.8 Write a Python function that takes a number as a parameter and check the number is prime or not.

def checkNumber(num):
    if num > 1:
        for i in range(2,num):
            if num % i != 0:
                result = 'prime'
            else:
                result = 'composite'
                break
    return result

print(checkNumber(14))