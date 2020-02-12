#Lab_Exercise_1
"""
Q4. Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).
For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am.
So, the program should print 2 30.
"""

print("This program give the time by the getting the minutes passed since midnight.")

minutesPassed = float(input("How much minutes have passed since midnight"))

time = minutesPassed/60 
hour = int(time) #didnot took decimal number
minutes = int((time - hour)*60)  #converted hour in decimal to the minutes and also made it integer from floating numbers.

print("The minutes passed since midnight is",minutesPassed,"minutes")
print("The time right now is ",hour,":",minutes)






