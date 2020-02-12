#Lab_Excersie_2
#Q.2 WAP which accepts marks of four subjects and display total marks, percentage and grade. Hint: more than 70%
# –> distinction, more than 60% –> first, more than 40% –> pass, less than 40% –> fail

mathMarks = int(input("What is your mathematics marks in exam"))
socialMarks = int(input("What is your social marks in exam"))
scienceMarks = int(input("What is your science marks in exam"))
englishMarks = int(input("What is your english marks in exam"))

totalMarks = mathMarks + socialMarks + scienceMarks + englishMarks

percentage = (totalMarks/400) *100

if percentage >= 70:
    result = 'distinction'
elif (percentage >=60 and percentage < 70):
    result = 'first division'
elif (percentage >=40 and percentage <60):
    result = 'pass'
else:
    result ='fail'

print("The total marks is",totalMarks)
print("You got ",percentage,"% ", "in the exam")
print("Your grade is ",result)

        