#using funcions  find sum of all odd no of a range provided by user,


def sum_odd (a):
    sum1=0
    for i in range (a+1):
        if i%2!=0:
            sum1+=i
            print(sum1)
    return sum1
a=int(input("enter your range :"))
print(sum_odd(a))
