#Lab_Excersie_3
#Q.6 Write a Python program to reverse a string.

def reverseString(word):
    return word[::-1]


userInput = input("Write a word")
print(reverseString(userInput))