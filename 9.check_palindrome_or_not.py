#Lab_Excersie_3
#Q.9 Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

def checkString(word):
    word = word.lower()
    if (word == word[::-1]):
        result = 'It is a palindrome'
    else:
        result = 'It is not palindrome'
    return result

userInput = input('Enter the word to check whether it is palindrome or not: ')
print(checkString(userInput))