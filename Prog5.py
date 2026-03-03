'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 5
'''
import math
def square(intValue):
    #Returns the suare of the int value
    suare = intValue * intValue
    return suare
def sumOfSquares(intValue):
    #returns the sum of suares from 1 to intvalue
    i = int(0)
    summ = int(0)
    while intValue >= i:
        summ = summ + (i * i)
        i = i + 1
    return summ
def numberOfBuses(numOfStudents):
    stuL = numOfStudents
    bus = int(1)
    if numOfStudents == 0:
        return(0)
    while stuL > 30:
        bus = bus + 1
        stuL = stuL - 30
    return bus

def distance(x1,y1,x2,y2):
    dxS = (x2 - x1) ** 2
    dyS = (y2 - y1) ** 2
    
    return float(math.sqrt(dxS + dyS))
def slope(x1,y1,x2,y2):
    Y = y2 - y1
    X = x2 - x1
    if x1 == x2:
        return("None")
    else:
        return((Y / X))
def compareTo(intValue1, intValue2):
    if intValue1 < intValue2:
        return(-1)
    elif intValue1 > intValue2:
        return(1)
    elif intValue1 == intValue2:
        return(0)
def closeEnough(intValue1, intValue2, tolerance):
    if (abs(intValue1 - intValue2,)) <= tolerance:
        return(True)
    else:
        return(False)
def daysInFebruary(year):
    if (year % 100) == 0:
        if (year % 400) == 0:
            return(29)
    if (year % 4) == 0:
        day = 29
    else:
        day = 28
    return(day)

def daysInMonth(month, year):
    if month == 2:
        day = daysInFebruary(year)
        return(day)
    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return(31)
    else:
        return(30)
    
print(daysInMonth(2,2023))