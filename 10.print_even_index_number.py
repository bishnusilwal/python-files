#Lab_Excersie_3
#Q.10 Accept string from the user and display only those characters which are present at an even index?

def evenString(wordS):
    for i in range(0,len(wordS),2):
        print(wordS[i])

userInput = input('Enter a word :')
evenString(userInput)