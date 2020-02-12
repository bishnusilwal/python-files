#Lab_Excersie_2
#Q.1 Check whether 5 is in list of first 5 natural numbers or not. Hint: List => [1,2,3,4,5]

naturalNumbers = [1,2,3,4,5]

for item in naturalNumbers:
    if item == 5:
        result = "yes"
if result == 'yes':    
    print("Yes 5 is in the list of first 5 natural numbers")
else:
    print("No, 5 isnot in the list of first 5 natural numbers")
        
        