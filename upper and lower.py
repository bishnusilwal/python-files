#writer a fundtions to pass a letter and check weather the string is upper or lower case
def alpha(x):
    if x.isupper():
        a="it is upper case "
    else:
        a="it is lower case"
    return a

z=str(input("enter the alpha"))
print(alpha(z))
