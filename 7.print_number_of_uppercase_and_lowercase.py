#Lab_Excersie_3
#Q.7 Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def countingCases(word):
    u=0
    l=0
    for item in word:
        if item.isupper():
            u = u+1
        elif item.islower():
            l = l+1
    print('The no. of upper case letter in',word,' is ',u," and lower case letter is",l)

wordFet = input('Enter a word')
print(countingCases(wordFet))

