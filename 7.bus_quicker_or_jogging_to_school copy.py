#Lab_Exercise_1
"""
Q7. You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? Alternatively, you could run to university.
You jog the first mile at 7mph; then run the next two at15mph; before jogging the last at 7mph again.
Will this be quicker or slower than the bus?

"""

print("This program will calculate whether your bus will be quicker to school or you will be quicker by jogging")

totalMiles = 4
busSpeed = 25
noOfStops = 10
stopsDelay = 2/60 #the speed is in mile per hour so converting minute to hours.

totalTimeForBus = (totalMiles/busSpeed) + (noOfStops * stopsDelay) #velocity=totalDistance/time taken
print("The bus takes",totalTimeForBus*60,"minutes to reach university") #converting hours to minutes

avgSpeedOfMe = (15+15+7+7)/4
meJogging = totalMiles/(avgSpeedOfMe)
print("I will take",meJogging*60,"minutes to reach university") #converting hour to minutes

if totalTimeForBus<meJogging:
    print("The bus will be quicker than me")
else:
    print("I will be quicker than the bus.")





